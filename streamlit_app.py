"""WheatCheck: identify wheat diseases and pests from a photo."""
import base64
import io
import os

import streamlit as st
import streamlit_analytics2 as streamlit_analytics
from PIL import Image
from st_screen_stats import ScreenData
from streamlit_carousel import carousel
from ultralytics import YOLO

from content import GALLERY, LANGUAGES, TEXT

MODEL_PATH = "best.pt"
# Predictions below this top-1 confidence are not shown to the user.
CONFIDENCE_THRESHOLD = 0.70

st.set_page_config(page_title="WheatCheck", page_icon="assets/icon.png", layout="wide")


@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)


@st.cache_data
def thumbnail(path, width=400):
    """JPEG bytes of a gallery image, scaled down from the multi-megabyte original."""
    img = Image.open(path).convert("RGB")
    img.thumbnail((width, width * 2))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=85)
    return buf.getvalue()


def is_portrait():
    """True on tall screens such as phones.

    Falls back to the wide layout if the browser doesn't report its size in time.
    """
    screen = ScreenData(setTimeout=3000).st_screen_data()
    if not screen:
        return False
    return screen["screen"]["height"] >= screen["screen"]["width"]


def render_section(section, heading=st.subheader):
    heading(section["heading"])
    for paragraph in section.get("paragraphs", []):
        st.write(paragraph)
    if "items" in section:
        marker = "1." if section.get("numbered") else "-"
        st.markdown("\n".join(f"{marker} {item}" for item in section["items"]))
    if "image" in section:
        st.image(section["image"])


def render_gallery(text, portrait):
    names = text["disease_names"]
    if portrait:
        carousel(items=[
            dict(
                title=names[cls],
                text="",
                img="data:image/jpeg;base64," + base64.b64encode(thumbnail(path)).decode(),
            )
            for cls, path in GALLERY.items()
        ])
    else:
        items = list(GALLERY.items())
        for row in (items[:7], items[7:]):
            for col, (cls, path) in zip(st.columns(7), row):
                col.image(thumbnail(path), caption=names[cls])


def render_result(text, upload):
    image = Image.open(upload).convert("RGB")
    st.markdown(text["image_heading"])
    st.image(image)

    result = load_model().predict(image, verbose=False)[0]
    cls = result.names[result.probs.top1]
    conf = float(result.probs.top1conf)

    if conf < CONFIDENCE_THRESHOLD:
        st.warning(text["low_confidence"])
    elif cls == "Healthy":
        st.success(text["no_disease"])
    else:
        info = text["diseases"][cls]
        st.subheader(text["result_heading"])
        st.write(f"{text['disease_label']}: {text['disease_names'][cls]}")
        st.write(f"{text['confidence_label']}: {conf:.0%}")
        st.write(info["description"])
        for key in ("causes", "preventions", "remedies"):
            st.markdown(f"{text[key + '_label']}:\n\n" + "\n".join(f"- {item}" for item in info[key]))


portrait = is_portrait()

# The analytics dashboard is at ?analytics=on; set ANALYTICS_PASSWORD to protect it.
with streamlit_analytics.track(unsafe_password=os.environ.get("ANALYTICS_PASSWORD")):
    language = st.radio("Language", options=list(LANGUAGES), horizontal=True, key="selected_language")
    text = TEXT[LANGUAGES[language]]

    logo, title = st.columns([1, 3] if portrait else [3, 9], vertical_alignment="center")
    logo.image("assets/logo.png")
    title.markdown(f"<h1 style='text-align: center;'>{text['title']}</h1>", unsafe_allow_html=True)

    for i, section in enumerate(text["intro"]):
        render_section(section, st.header if i == 0 else st.subheader)

    render_gallery(text, portrait)

    for section in text["about"]:
        render_section(section)

    st.subheader(text["steps_heading"])
    st.markdown("\n".join(f"- {step}" for step in text["steps"]))

    upload = st.file_uploader(text["upload_label"], type=["jpg", "jpeg", "png"])
    if st.button(text["analyze_button"]):
        if upload is None:
            st.warning(text["upload_first"])
        else:
            render_result(text, upload)
