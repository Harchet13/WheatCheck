# WheatCheck

A Streamlit web app that identifies wheat diseases and pests from a photo and
explains their causes, prevention and remedies, in English, Hindi and Punjabi.

It uses a YOLO image classifier (`best.pt`) trained on 15 classes: Aphid, Black
Rust, Blast, Brown Rust, Common Root Rot, Fusarium Head Blight, Healthy, Leaf
Blight, Mildew, Mite, Septoria, Smut, Stem fly, Tan spot and Yellow Rust.

## Run locally

Requires Python 3.10+ and [Git LFS](https://git-lfs.com), which stores the
model file. Run `git lfs install` once before cloning; in an existing clone,
run `git lfs pull` to fetch `best.pt`.

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Tests

```sh
pip install -r requirements-dev.txt
pytest
```

The tests check the model against the sample images in `assets/samples/`,
check that every disease has text in every language, and drive the app end to
end with Streamlit's `AppTest`. They run on every push and pull request via
GitHub Actions.

## Training

The model was trained on the Kaggle
[Wheat Plant Diseases](https://www.kaggle.com/datasets/kushagra3204/wheat-plant-diseases)
dataset (about 6 GB, so it isn't stored in this repo). To retrain:

```sh
pip install -r requirements-train.txt
python train.py                          # downloads the dataset from Kaggle
python train.py --data path/to/data      # or use a local copy
```

The dataset's own test split mostly repeats training images, so `train.py`
pools all images, removes exact duplicates and makes a fresh train/val/test
split before training. It finishes by printing per-class accuracy on the
held-out test images. Defaults match the current model (YOLOv8s-cls, 20 epochs,
224 px); training on a CPU is slow, so pass `--device 0` on a CUDA GPU or
`--device mps` on Apple Silicon. Copy the printed `best.pt` over `./best.pt`
to ship it.

[`training/`](training/README.md) holds the records of the current and previous training runs: their
settings, per-epoch metrics, confusion matrices, and a checksum manifest of
every training and test image.

## Project layout

| Path | What it is |
| --- | --- |
| `streamlit_app.py` | The app: layout, image upload and prediction |
| `content.py` | All user-facing text, per language |
| `best.pt` | The trained YOLO classification model (stored in Git LFS) |
| `assets/` | Logo, favicon and page images |
| `assets/samples/` | One sample photo per disease, used in the gallery and tests |
| `train.py` | Rebuilds the dataset split and retrains the model |
| `training/` | Record of the run that produced `best.pt`, and a dataset manifest |
| `.streamlit/config.toml` | The app's colour theme and font |
| `packages.txt` | System packages for Streamlit Community Cloud |

## Editing text or adding a language

All wording lives in `content.py`. To add a language, add its label to
`LANGUAGES` and a matching entry to `TEXT` with the same keys as the existing
ones; `pytest` will tell you if anything is missing.

## Analytics

Usage is counted with `streamlit-analytics2`. The dashboard is at
`?analytics=on`; set the `ANALYTICS_PASSWORD` environment variable (or a
top-level secret of that name on Streamlit Cloud) to require a password for it.
Counts are kept in memory and reset when the app restarts.
