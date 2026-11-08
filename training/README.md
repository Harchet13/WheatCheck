# Training record

This folder documents how the shipped model (`../best.pt`) was trained, what
data it saw, and how the previous model compared.

## Current model: 8 November 2026

`run-2026-11-08/` is the Ultralytics output from running `train.py`, which
produced the current `best.pt` (MD5 `cbfd8a8cc5e86b4c27bb4f4789ac46ff`). The
weights themselves aren't duplicated here.

| Setting | Value |
| --- | --- |
| Model | YOLOv8s-cls (`yolov8s-cls.pt`, ImageNet-pretrained) |
| Data | Kaggle train + test pooled, exact duplicates removed, fresh 80/10/10 split |
| Split | 8,712 train / 1,088 validation / 1,088 test images |
| Epochs | 20 |
| Image size | 224 px |
| Batch size | 32 |
| Seed | 0 |
| Hardware | Apple M2, `--device mps`, PyTorch 2.5.1 |

The small model (YOLOv8s) was used because the large one would have taken
about 15 hours on this laptop, against about 2 hours for the small one. Newer
PyTorch releases crashed during training on the Apple GPU; 2.5.1 works.

### Result

On the 1,088 held-out test images, which the model never trained on:
**88.6% top-1 accuracy** (964/1,088). Per-class results are in
[`test_results.txt`](run-2026-11-08/test_results.txt). Healthy wheat is now
98% correct (102/104), and Yellow Rust 96%. The weakest classes are Leaf
Blight (68%, often confused with Tan spot) and Tan spot (70%).

Only 29 of the new test images were also unseen by the previous model. On
those, the previous model scored 23/29 and called 6 of 7 Healthy images
Yellow Rust; the new model scored 29/29.

The run folder has the same kinds of files as the 2024 run below.

## Previous model: 21 June 2024

`run-2024-06-21/` is the output Ultralytics wrote for the training run that
produced the previous `best.pt`. That model's MD5 was `91595abf6564917640f3ee4fc696dda6`; it can be recovered from the git history.

| Setting | Value |
| --- | --- |
| Model | YOLOv8l-cls (`yolov8l-cls.pt`, ImageNet-pretrained) |
| Epochs | 20 |
| Image size | 224 px |
| Batch size | 32 |
| Optimizer | auto (Ultralytics default) |
| Seed | 0 |

Full settings are in [`args.yaml`](run-2024-06-21/args.yaml).

| File | What it shows |
| --- | --- |
| `results.csv`, `results.png` | Loss and accuracy for each epoch |
| `confusion_matrix.png`, `confusion_matrix_normalized.png` | Predicted vs. true class on the evaluation images |
| `train_batch*.jpg` | Augmented training images, as the model saw them |
| `val_batch*_labels.jpg`, `val_batch*_pred.jpg` | Evaluation images with their true and predicted labels |

### Result

After 20 epochs: **90.7% top-1** and **99.7% top-5** accuracy
([`results.csv`](run-2024-06-21/results.csv)).

## The data

The images come from the Kaggle
[Wheat Plant Diseases](https://www.kaggle.com/datasets/kushagra3204/wheat-plant-diseases)
dataset, which has a `train/` folder (13,104 images) and a `test/` folder
(748 images) across 15 classes. The current Kaggle version (v6) also
has a `valid/` folder of 300 images, but every one of them is a copy of a
`train/` or `test/` image, so it adds nothing. A November 2026 check also found
that 40 images in v6 are re-saved copies of the same photos as here (different
bytes, same picture). At 6.3 GB, the dataset is too large to keep
in this repo. Instead:

- [`dataset_manifest.csv`](dataset_manifest.csv) lists every image used,
  with its split, class folder, file name, size and MD5 checksum. You can use
  it to check that a downloaded copy matches exactly.
- [`dataset_summary.csv`](dataset_summary.csv) gives per-class counts.

## Caveat: the reported accuracy is optimistic

The dataset has no validation folder, so Ultralytics evaluated on `test/`.
Comparing checksums shows that **491 of the 748 test images (66%) are exact
copies of training images**. For 10 of the 15 classes, almost every test
image also appears in training, so the model had already seen it.

Only 257 test images are truly unseen, and they come mostly from 5 classes:
Brown Rust, Fusarium Head Blight, Healthy, Mildew and Yellow Rust. On those
257 images, the previous model scored about **80%**. Healthy wheat is its main
weakness: it calls 43 of 50 unseen Healthy images Yellow Rust.

`../train.py` fixes this for future runs. It pools both folders, removes
duplicate images and makes a fresh train/val/test split, so the test score
measures images the model has never seen.
