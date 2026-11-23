"""Tests for WheatCheck: the YOLO classifier, the text content and the Streamlit app."""
import contextlib
import sys
from pathlib import Path
from unittest import mock

import pytest
import streamlit as st
from streamlit.testing.v1 import AppTest
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from content import GALLERY, LANGUAGES, PRODUCTS, SHOPS, TEXT  # noqa: E402
from howto import howto_html  # noqa: E402

APP = ROOT / "streamlit_app.py"
MODEL = ROOT / "best.pt"
CONFIDENCE_THRESHOLD = 0.70


@pytest.fixture(autouse=True)
def _run_from_repo_root(monkeypatch):
    # The app loads best.pt and assets/ by relative path.
    monkeypatch.chdir(ROOT)


@pytest.fixture(scope="session")
def model():
    return YOLO(str(MODEL))


# --- Model -----------------------------------------------------------------

def test_model_is_classifier_with_expected_classes(model):
    assert model.task == "classify"
    assert set(model.names.values()) == set(GALLERY) | {"Healthy"}


@pytest.mark.parametrize("cls", list(GALLERY))
def test_model_classifies_sample_image(model, cls):
    result = model.predict(str(ROOT / GALLERY[cls]), verbose=False)[0]
    assert result.names[result.probs.top1] == cls
    assert float(result.probs.top1conf) >= CONFIDENCE_THRESHOLD


# --- Content -----------------------------------------------------------------

@pytest.mark.parametrize("lang", list(TEXT))
def test_every_disease_has_name_and_info(model, lang):
    diseases = set(model.names.values()) - {"Healthy"}
    assert set(TEXT[lang]["disease_names"]) == diseases
    assert set(TEXT[lang]["diseases"]) == diseases
    for cls, info in TEXT[lang]["diseases"].items():
        assert info["description"], cls
        for key in ("causes", "preventions", "remedies"):
            assert info[key], (cls, key)


def test_languages_have_the_same_keys():
    assert set(LANGUAGES.values()) == set(TEXT)
    keys = set(TEXT["en"])
    for lang, text in TEXT.items():
        assert set(text) == keys, lang
        assert len(text["intro"]) == len(TEXT["en"]["intro"]), lang
        assert len(text["about"]) == len(TEXT["en"]["about"]), lang


def test_every_class_has_products_to_buy(model):
    for cls in model.names.values():
        assert PRODUCTS[cls], cls
        for name, ingredient, kind in PRODUCTS[cls]:
            assert name and ingredient, cls
            for lang in TEXT:
                assert TEXT[lang]["product_types"][kind], (lang, kind)


def test_shop_urls_are_searches_or_home_pages():
    for shop, url in SHOPS.items():
        assert url.startswith("https://") and url.count("{}") <= 1, shop


def test_howto_animation_has_translated_text():
    for text in TEXT.values():
        html = howto_html(text["animation_captions"], text["analyze_button"],
                          text["disease_names"]["Yellow Rust"], text["buy_heading"])
        for caption in text["animation_captions"]:
            assert caption.replace('"', "&quot;") in html
        assert text["analyze_button"] in html


def test_referenced_images_exist():
    paths = list(GALLERY.values()) + [
        s["image"] for t in TEXT.values() for s in t["intro"] + t["about"] if "image" in s
    ]
    for path in paths:
        assert (ROOT / path).is_file(), path


# --- App end to end ----------------------------------------------------------

def _screen(width, height):
    fake = mock.MagicMock()
    data = None if width is None else {"screen": {"width": width, "height": height}}
    fake.return_value.st_screen_data.return_value = data
    return fake


def _fake_yolo(cls, conf):
    """A YOLO stand-in whose prediction is always `cls` with confidence `conf`."""
    result = mock.MagicMock()
    result.names = {0: cls}
    result.probs.top1 = 0
    result.probs.top1conf = conf
    yolo = mock.MagicMock()
    yolo.return_value.predict.return_value = [result]
    return yolo


def _run_app(screen=(1920, 1080), language=None, upload=None, click=False,
             prediction=None, analytics=False, press=None):
    """Run the app with the screen-size component faked.

    upload: sample image to feed the file uploader. click: press Analyze.
    press: key of another button to press, such as "how_to".
    prediction: (class, confidence) to fake the model; real model otherwise.
    Analytics tracking is stubbed unless analytics=True: it records usage and
    wraps st.button with a copy saved on first use, which bypasses our mocks.
    """
    patches = [mock.patch("st_screen_stats.ScreenData", _screen(*screen))]
    if not analytics:
        patches.append(mock.patch("streamlit_analytics2.track", lambda **kw: contextlib.nullcontext()))
    if upload is not None:
        patches.append(mock.patch("streamlit.file_uploader", return_value=open(ROOT / upload, "rb")))
    pressed = {"analyze"} if click else set()
    if press:
        pressed.add(press)
    if pressed:
        patches.append(mock.patch("streamlit.button", side_effect=lambda *a, **kw: kw.get("key") in pressed))
    if prediction is not None:
        patches.append(mock.patch("ultralytics.YOLO", _fake_yolo(*prediction)))
    st.cache_resource.clear()  # don't reuse a model loaded under a different patch
    for p in patches:
        p.start()
    try:
        at = AppTest.from_file(str(APP), default_timeout=120)
        if language is not None:
            at.session_state["selected_language"] = language
        at.run()
        return at
    finally:
        for p in patches:
            p.stop()
        st.cache_resource.clear()


def _text(at):
    return "\n".join(
        str(e.value) for e in [*at.markdown, *at.header, *at.subheader, *at.warning, *at.success]
    )


@pytest.mark.parametrize("screen", [(1920, 1080), (390, 844), (None, None)],
                         ids=["landscape", "portrait", "unknown"])
@pytest.mark.parametrize("language", list(LANGUAGES))
def test_app_renders(screen, language):
    at = _run_app(screen=screen, language=language)
    assert not at.exception
    text = TEXT[LANGUAGES[language]]
    assert text["title"] in _text(at)
    assert text["steps_heading"] in _text(at)


def test_app_runs_with_analytics_tracking():
    at = _run_app(analytics=True)
    assert not at.exception, at.exception[0].message


def _link_buttons(at):
    return [e for e in at.get("link_button")]


@pytest.mark.parametrize("press", ["how_to", "samples", "about"])
@pytest.mark.parametrize("screen", [(1920, 1080), (390, 844)], ids=["landscape", "portrait"])
def test_help_buttons_open_without_errors(press, screen):
    at = _run_app(screen=screen, press=press)
    assert not at.exception, at.exception[0].message


def test_upload_page_hides_background_info_until_asked():
    at = _run_app()
    text = _text(at)
    assert TEXT["en"]["intro"][0]["heading"] not in text
    assert TEXT["en"]["samples_intro"] not in text
    at = _run_app(press="about")
    assert TEXT["en"]["intro"][0]["heading"] in _text(at)


def test_remedies_link_to_shops():
    at = _run_app(upload=GALLERY["Aphid"], click=True, prediction=("Aphid", 0.95))
    assert not at.exception
    urls = [b.proto.url for b in _link_buttons(at)]
    assert len(urls) == len(PRODUCTS["Aphid"]) * len(SHOPS)
    assert "https://www.amazon.in/s?k=Confidor+Imidacloprid" in urls
    assert "https://www.bighaat.com/" in urls
    assert TEXT["en"]["shop_search_hint"] in "\n".join(c.value for c in at.caption)


def test_analyze_without_upload_asks_for_image():
    at = _run_app(click=True)
    assert not at.exception
    assert TEXT["en"]["upload_first"] in _text(at)


def test_app_reports_disease_for_uploaded_image():
    at = _run_app(upload=GALLERY["Aphid"], click=True)
    assert not at.exception
    text = _text(at)
    assert "Disease: Aphid" in text
    for item in TEXT["en"]["diseases"]["Aphid"]["causes"] + TEXT["en"]["diseases"]["Aphid"]["remedies"]:
        assert item in text
    assert [t.label for t in at.tabs] == ["💊 Remedies", "🛡️ Preventions", "🔍 Causes"]


def test_app_uses_translated_disease_name():
    at = _run_app(language="हिंदी", upload=GALLERY["Mite"], click=True, prediction=("Mite", 0.95))
    assert not at.exception
    assert "बीमारी: घुन" in _text(at)


def test_low_confidence_is_not_reported_as_healthy():
    at = _run_app(upload=GALLERY["Aphid"], click=True, prediction=("Aphid", 0.4))
    assert not at.exception
    text = _text(at)
    assert TEXT["en"]["low_confidence"] in text
    assert TEXT["en"]["no_disease"] not in text
    assert "Disease:" not in text


def test_healthy_prediction_shows_no_disease():
    at = _run_app(upload=GALLERY["Aphid"], click=True, prediction=("Healthy", 0.99))
    assert not at.exception
    text = _text(at)
    assert TEXT["en"]["no_disease"] in text
    assert "Disease:" not in text
    assert len(_link_buttons(at)) == len(PRODUCTS["Healthy"]) * len(SHOPS)
