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
end with Streamlit's `AppTest`.

## Project layout

| Path | What it is |
| --- | --- |
| `streamlit_app.py` | The app: layout, image upload and prediction |
| `content.py` | All user-facing text, per language |
| `best.pt` | The trained YOLO classification model (stored in Git LFS) |
| `assets/` | Logo, favicon and page images |
| `assets/samples/` | One sample photo per disease, used in the gallery and tests |
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
