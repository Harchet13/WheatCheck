"""WheatCheck: identify wheat diseases and pests from a photo."""
import base64 # allows you to encode and decode binary data into a safe, text-only format.
import io
import os
from urllib.parse import quote_plus

import streamlit as st # for the web page
import streamlit.components.v1 as components
import streamlit_analytics2 as streamlit_analytics
from PIL import Image # for opening images
from st_screen_stats import ScreenData
from streamlit_carousel import carousel
from ultralytics import YOLO # for the model

# GALLERY: sample pics, LANGUAGES: list of languages, TEXT: all the text in English, Hindi and Punjabi,
# PRODUCTS/SHOPS: what to buy for each disease and where.
from content import GALLERY, LANGUAGES, PRODUCTS, SHOPS, TEXT
from howto import howto_html

MODEL_PATH = "best.pt"
# Predictions below this top-1 confidence are not shown to the user.
CONFIDENCE_THRESHOLD = 0.70
# Shown in every language so anyone can find the language picker.
LANGUAGE_LABEL = "🌐 Language · भाषा · ਭਾਸ਼ਾ"

st.set_page_config(page_title="WheatCheck", page_icon="assets/icon.png", layout="centered")

# The language bar is a bright gold strip so it stands out against the teal page.
st.html("""<style>
.st-key-lang_bar { background: #F5C518; border-radius: 14px; padding: 10px 14px 12px;
                   box-shadow: 0 4px 14px rgba(0,0,0,.25); }
.st-key-lang_bar label, .st-key-lang_bar label p { color: #1b1b1b !important; font-weight: 700; font-size: 1.05rem; }
.st-key-lang_bar button { background: #fffdf3; border: 2px solid #1b1b1b; min-height: 2.6rem; padding: 0 1.1rem; }
.st-key-lang_bar button * { color: #1b1b1b !important; font-size: 1.1rem; font-weight: 600; }
.st-key-lang_bar button[aria-checked="true"] { background: #1b1b1b !important; border-color: #1b1b1b !important; }
.st-key-lang_bar button[aria-checked="true"] * { color: #F5C518 !important; }
[data-testid="stMainBlockContainer"] { padding-top: 2.5rem; }
.st-key-upload_card { background: rgba(0,0,0,.18); }
.st-key-upload_card h3 { font-size: 1.3rem; }
/* The main action: gold like the language bar, with dark text for contrast. */
.st-key-analyze button { background: #F5C518; border-color: #F5C518; min-height: 3rem; }
.st-key-analyze button:hover { background: #ffd84d; border-color: #ffd84d; }
.st-key-analyze button p { color: #1b1b1b; font-weight: 700; font-size: 1.15rem; }
/* Keep the help buttons and each product's shop buttons side by side on phones,
   instead of Streamlit stacking every column. */
.st-key-help_row [data-testid="stHorizontalBlock"],
[class*="st-key-product_"] [data-testid="stHorizontalBlock"] { flex-wrap: nowrap !important; gap: .5rem; }
.st-key-help_row [data-testid="stColumn"],
[class*="st-key-product_"] [data-testid="stColumn"] { min-width: 0 !important; width: auto !important; flex: 1 1 0 !important; }
.st-key-help_row button { min-height: 3.2rem; padding: .25rem .4rem; }
.st-key-help_row button p { font-size: .9rem; line-height: 1.25; white-space: normal; }
.wc-header { display: flex; align-items: center; gap: 14px; margin: .5rem 0 .25rem; }
.wc-header img { width: 72px; height: 72px; flex: none; border-radius: 50%; }
.wc-title { margin: 0; padding: 0 !important; font-size: clamp(1.3rem, 5.5vw, 2rem) !important; line-height: 1.25 !important; }
.wc-tagline { opacity: .9; margin: .2rem 0 0; font-size: .95rem; }
</style>""")


# Helper functions
@st.cache_resource # model loaded once and reused, not reloaded on every click.
def load_model():
    return YOLO(MODEL_PATH) # loads the model from best.pt


@st.cache_data
def thumbnail(path, width=400): # Taking long to load so shrinks a gallery photo to a small JPEG
    """JPEG bytes of a gallery image, scaled down from the multi-megabyte original."""
    img = Image.open(path).convert("RGB")
    img.thumbnail((width, width * 2))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=85)
    return buf.getvalue()


@st.cache_data
def logo_base64():
    return base64.b64encode(thumbnail("assets/logo.png", width=160)).decode()


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
        for start in range(0, len(items), 4):
            for col, (cls, path) in zip(st.columns(4), items[start:start + 4]):
                col.image(thumbnail(path), caption=names[cls])


def render_photo_tips(text):
    st.markdown(f"**📷 {text['photo_tips_heading']}**\n\n" + "\n".join(f"- {tip}" for tip in text["photo_tips"]))


# Pop-up windows opened by the help buttons; only one is open at a time.
@st.dialog("WheatCheck", width="large")
def howto_dialog(text):
    st.subheader(text["how_to_button"])
    components.html(
        howto_html(text["animation_captions"], text["analyze_button"],
                   text["disease_names"]["Yellow Rust"], text["buy_heading"]),
        height=500,
    )
    render_photo_tips(text)


@st.dialog("WheatCheck", width="large")
def samples_dialog(text, portrait):
    st.subheader(text["samples_button"])
    st.caption(text["samples_intro"])
    render_gallery(text, portrait)


@st.dialog("WheatCheck", width="large")
def about_dialog(text):
    for section in text["intro"] + text["about"]:
        render_section(section)


def search_words(name, ingredient):
    """What to type into a shop's search for a product.

    Brand names are paired with their active ingredient's first word (e.g.
    "Tilt Propiconazole") so the search finds the right product; generic
    products are searched by name alone.
    """
    word = ingredient.split()[0]
    return f"{name} {word}" if "%" in ingredient and word.lower() not in name.lower() else name


def shop_url(url, name, ingredient):
    """A shop link: a product search where the shop supports it, else its home page."""
    return url.format(quote_plus(search_words(name, ingredient))) if "{}" in url else url


def render_products(text, cls):
    """Buy links for the products that act on the remedies for `cls`."""
    st.markdown(f"**{text['buy_heading']}**")
    if any("{}" not in url for url in SHOPS.values()):
        st.caption(text["shop_search_hint"])
    for i, (name, ingredient, kind) in enumerate(PRODUCTS[cls]):
        with st.container(border=True, key=f"product_{i}"):
            st.markdown(f"**{name}** · {ingredient}  \n:gray[{text['product_types'][kind]}]")
            for col, (shop, url) in zip(st.columns(len(SHOPS)), SHOPS.items()):
                col.link_button(f"{shop} ↗", shop_url(url, name, ingredient), use_container_width=True)
    st.caption(text["buy_note"])


def render_result(text, upload):
    image = Image.open(upload).convert("RGB")
    result = load_model().predict(image, verbose=False)[0]
    cls = result.names[result.probs.top1]
    conf = float(result.probs.top1conf)

    photo, details = st.columns([2, 3])
    photo.markdown(text["image_heading"])
    photo.image(image)

    with details:
        if conf < CONFIDENCE_THRESHOLD:
            st.warning(text["low_confidence"])
            render_photo_tips(text)
            return
        if cls == "Healthy":
            st.success(text["no_disease"])
            st.write(text["healthy_tip"])
            render_products(text, cls)
            return
        info = text["diseases"][cls]
        st.subheader(f"{text['disease_label']}: {text['disease_names'][cls]}")
        st.progress(conf, text=f"{text['confidence_label']}: {conf:.0%}")
        st.write(info["description"])

    # The most actionable tab, remedies with buy links, comes first.
    remedies, preventions, causes = st.tabs(
        [f"💊 {text['remedies_label']}", f"🛡️ {text['preventions_label']}", f"🔍 {text['causes_label']}"]
    )
    with remedies:
        st.markdown("\n".join(f"- {item}" for item in info["remedies"]))
        render_products(text, cls)
    preventions.markdown("\n".join(f"- {item}" for item in info["preventions"]))
    causes.markdown("\n".join(f"- {item}" for item in info["causes"]))


def keep_a_language():
    """Clicking the selected language again would clear it; restore the last one instead."""
    if st.session_state["selected_language"] is None:
        st.session_state["selected_language"] = st.session_state.get("last_language", "English")


portrait = is_portrait()

# The language can be preset with ?lang=pa (or hi, en), so links can be shared in any language.
if "selected_language" not in st.session_state:
    by_code = {code: label for label, code in LANGUAGES.items()}
    st.session_state["selected_language"] = by_code.get(st.query_params.get("lang"), "English")

# The analytics dashboard is at ?analytics=on; set ANALYTICS_PASSWORD to protect it.
with streamlit_analytics.track(unsafe_password=os.environ.get("ANALYTICS_PASSWORD")):
    with st.container(key="lang_bar"):
        language = st.segmented_control(
            LANGUAGE_LABEL, options=list(LANGUAGES), key="selected_language", on_change=keep_a_language,
        )
    st.session_state["last_language"] = language
    lang = LANGUAGES[language or "English"]
    st.query_params["lang"] = lang
    text = TEXT[lang]

    # Logo and title stay side by side, even on phones.
    st.markdown(
        f"<div class='wc-header'><img src='data:image/jpeg;base64,{logo_base64()}' alt=''>"
        f"<div><h1 class='wc-title'>{text['title']}</h1><p class='wc-tagline'>{text['tagline']}</p></div></div>",
        unsafe_allow_html=True,
    )

    # Everything except the upload steps lives behind these buttons.
    how_col, samples_col, about_col = st.container(key="help_row").columns(3)
    with how_col:
        if st.button(text["how_to_button"], key="how_to", use_container_width=True):
            howto_dialog(text)
    with samples_col:
        if st.button(text["samples_button"], key="samples", use_container_width=True):
            samples_dialog(text, portrait)
    with about_col:
        if st.button(text["about_button"], key="about", use_container_width=True):
            about_dialog(text)

    with st.container(border=True, key="upload_card"):
        st.subheader(text["steps_heading"])
        st.markdown("\n".join(f"{i}. {step}" for i, step in enumerate(text["steps"], 1)))
        upload = st.file_uploader(text["upload_label"], type=["jpg", "jpeg", "png"])
        analyze = st.button(text["analyze_button"], key="analyze", type="primary",
                            use_container_width=True)

    if analyze:
        if upload is None:
            st.warning(text["upload_first"])
        else:
            render_result(text, upload)
