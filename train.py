"""Train the WheatCheck classifier on the Kaggle wheat plant diseases dataset.

Dataset: https://www.kaggle.com/datasets/kushagra3204/wheat-plant-diseases

The dataset's own test split mostly repeats training images, so scores on it
are inflated. This script pools every image, drops exact duplicates, and makes
a fresh per-class train/val/test split with no overlap.

    pip install -r requirements-train.txt
    python train.py                         # download from Kaggle
    python train.py --data ~/Downloads/data # use a local copy

Training writes to runs/; copy the printed best.pt over ./best.pt to ship it.
"""
import argparse
import hashlib
import os
import random
import shutil
from collections import Counter, defaultdict
from pathlib import Path

KAGGLE_DATASET = "kushagra3204/wheat-plant-diseases"
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
# Predictions below this are shown as "not confident" in the app.
CONFIDENCE_THRESHOLD = 0.70


def class_key(folder_name):
    """'stem_fly_test' and 'Stem fly' -> 'stem fly'."""
    name = folder_name.lower().replace("_", " ").strip()
    return name.removesuffix(" test").removesuffix(" valid").removesuffix(" val")


def find_class_dirs(root):
    """Map each class (by train-folder name) to every folder holding its images."""
    root = Path(root)
    train = next((p for p in root.rglob("train") if p.is_dir()), None)
    if train is None:
        raise SystemExit(f"No 'train' folder found under {root}")
    names = {class_key(d.name): d.name for d in train.iterdir() if d.is_dir()}
    dirs = defaultdict(list)
    for split in train.parent.iterdir():
        if not split.is_dir():
            continue
        for d in split.iterdir():
            if d.is_dir() and class_key(d.name) in names:
                dirs[names[class_key(d.name)]].append(d)
    return dict(dirs)


def unique_images(class_dirs):
    """{class: [paths]} with byte-identical images kept once.

    An image found under two different classes is dropped as ambiguous.
    """
    owner = {}
    for cls, dirs in sorted(class_dirs.items()):
        for d in dirs:
            for p in sorted(d.iterdir()):
                if p.suffix.lower() not in IMAGE_SUFFIXES:
                    continue
                digest = hashlib.md5(p.read_bytes()).hexdigest()
                if digest not in owner:
                    owner[digest] = (cls, p)
                elif owner[digest] is not None and owner[digest][0] != cls:
                    owner[digest] = None
    images = defaultdict(list)
    for entry in owner.values():
        if entry is not None:
            images[entry[0]].append(entry[1])
    return dict(images)


def split(images, val=0.1, test=0.1, seed=0):
    """Shuffle each class and cut it into train/val/test."""
    rng = random.Random(seed)
    splits = {"train": {}, "val": {}, "test": {}}
    for cls, paths in images.items():
        paths = sorted(paths)
        rng.shuffle(paths)
        n_test, n_val = round(len(paths) * test), round(len(paths) * val)
        splits["test"][cls] = paths[:n_test]
        splits["val"][cls] = paths[n_test:n_test + n_val]
        splits["train"][cls] = paths[n_test + n_val:]
    return splits


def build(splits, out):
    """Lay out the splits as out/<split>/<class>/<image>, using symlinks."""
    out = Path(out)
    if out.exists():
        shutil.rmtree(out)
    for split_name, classes in splits.items():
        for cls, paths in classes.items():
            d = out / split_name / cls
            d.mkdir(parents=True)
            for i, p in enumerate(paths):
                # Prefix with an index: different source folders reuse file names.
                os.symlink(p.resolve(), d / f"{i:05d}_{p.name}")
    return out


def evaluate(model, test_split):
    """Print per-class accuracy on the held-out test split."""
    print(f"\n{'class':22s} {'n':>4s} {'correct':>8s} {'shown':>6s}  most common mistakes")
    total = total_ok = 0
    for cls, paths in sorted(test_split.items()):
        ok = shown = 0
        mistakes = Counter()
        for i in range(0, len(paths), 32):
            for r in model.predict([str(p) for p in paths[i:i + 32]], verbose=False):
                pred = r.names[r.probs.top1]
                if pred == cls:
                    ok += 1
                    shown += float(r.probs.top1conf) >= CONFIDENCE_THRESHOLD
                else:
                    mistakes[pred] += 1
        n = len(paths)
        total, total_ok = total + n, total_ok + ok
        print(f"{cls:22s} {n:4d} {ok / n:8.0%} {shown / n:6.0%}  {mistakes.most_common(2)}")
    print(f"\noverall accuracy: {total_ok}/{total} = {total_ok / total:.1%}")
    print(f"('shown' = correct with confidence >= {CONFIDENCE_THRESHOLD:.0%}, so the app displays it)")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data", help="local copy of the dataset (default: download from Kaggle)")
    parser.add_argument("--out", default="datasets/wheat", help="where to build the deduplicated split")
    parser.add_argument("--model", default="yolov8s-cls.pt", help="pretrained weights to start from")
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--imgsz", type=int, default=224)
    parser.add_argument("--batch", type=int, default=32)
    parser.add_argument("--device", default=None, help="e.g. 0 for the first GPU, mps, or cpu")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    if args.data:
        root = Path(args.data).expanduser()
    else:
        import kagglehub
        root = Path(kagglehub.dataset_download(KAGGLE_DATASET))

    images = unique_images(find_class_dirs(root))
    splits = split(images, seed=args.seed)
    data = build(splits, args.out)
    for name, classes in splits.items():
        print(f"{name}: {sum(map(len, classes.values()))} images")

    from ultralytics import YOLO
    model = YOLO(args.model)
    model.train(data=str(data.resolve()), epochs=args.epochs, imgsz=args.imgsz,
                batch=args.batch, device=args.device, seed=args.seed)
    best = Path(model.trainer.best)
    evaluate(YOLO(str(best)), splits["test"])
    print(f"\nBest weights: {best}\nTo ship them: cp '{best}' best.pt")


if __name__ == "__main__":
    main()
