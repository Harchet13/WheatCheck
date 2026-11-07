# Training record

This folder documents how the shipped model (`../best.pt`) was trained and
what data it saw.

## The run: 21 June 2024

`run-2024-06-21/` is the output Ultralytics wrote for the training run that
produced `best.pt`. The run's `weights/best.pt` is byte-for-byte identical to
the model in this repo (MD5 `91595abf6564917640f3ee4fc696dda6`). The weights
themselves aren't duplicated here.

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
(748 images) across 15 classes. At 6.3 GB, the dataset is too large to keep
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
257 images, the shipped model scores about **80%**. Healthy wheat is its main
weakness: it calls 43 of 50 unseen Healthy images Yellow Rust.

`../train.py` fixes this for future runs. It pools both folders, removes
duplicate images and makes a fresh train/val/test split, so the test score
measures images the model has never seen.
