"""Tests for the dataset preparation in train.py (no training is run)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import train  # noqa: E402


def _write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def _dataset(tmp_path):
    """Mimics the Kaggle layout: train/<Class>/ and test/<class>_test/."""
    data = tmp_path / "data"
    for i in range(20):
        _write(data / "train" / "Stem fly" / f"s{i}.png", f"stem {i}".encode())
        _write(data / "train" / "Healthy" / f"h{i}.png", f"healthy {i}".encode())
    # Test copies of training images, plus one genuinely new image.
    _write(data / "test" / "stem_fly_test" / "s0.png", b"stem 0")
    _write(data / "test" / "stem_fly_test" / "new.png", b"stem new")
    # The same bytes under two classes are ambiguous.
    _write(data / "train" / "Healthy" / "dup.png", b"both")
    _write(data / "train" / "Stem fly" / "dup.png", b"both")
    _write(data / "train" / "Healthy" / "notes.txt", b"not an image")
    return data


def test_test_folders_are_matched_to_train_classes(tmp_path):
    dirs = train.find_class_dirs(_dataset(tmp_path))
    assert set(dirs) == {"Stem fly", "Healthy"}
    assert {d.name for d in dirs["Stem fly"]} == {"Stem fly", "stem_fly_test"}


def test_duplicates_and_ambiguous_images_are_dropped(tmp_path):
    images = train.unique_images(train.find_class_dirs(_dataset(tmp_path)))
    assert len(images["Stem fly"]) == 21  # 20 + new.png; the s0.png copy is dropped
    assert len(images["Healthy"]) == 20
    assert not any(p.name in ("dup.png", "notes.txt") for ps in images.values() for p in ps)


def test_splits_do_not_overlap_and_are_reproducible(tmp_path):
    images = train.unique_images(train.find_class_dirs(_dataset(tmp_path)))
    splits = train.split(images, seed=0)
    for cls, paths in images.items():
        parts = [set(splits[s][cls]) for s in ("train", "val", "test")]
        assert set().union(*parts) == set(paths)
        assert sum(map(len, parts)) == len(paths)
        assert all(parts[2])  # every class has test images
    assert train.split(images, seed=0) == splits


def test_build_lays_out_ultralytics_folders(tmp_path):
    images = train.unique_images(train.find_class_dirs(_dataset(tmp_path)))
    out = train.build(train.split(images), tmp_path / "built")
    assert {p.name for p in out.iterdir()} == {"train", "val", "test"}
    assert {p.name for p in (out / "train").iterdir()} == {"Stem fly", "Healthy"}
    linked = next((out / "train" / "Healthy").iterdir())
    assert linked.is_symlink() and linked.read_bytes().startswith(b"healthy")
