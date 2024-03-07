import os
import io
import cv2
import warnings
from PIL import Image
import streamlit as st
from groundingdino.util.inference import (
    load_model,
    load_image,
    predict,
    annotate,
)

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="GroundingDINO - WebApp",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="auto",
)

CONFIG_PATH = "groundingdino/config/GroundingDINO_SwinT_OGC.py"
WEIGHTS_PATH = "weights/groundingdino_swint_ogc.pth"
BOX_TRESHOLD = 0.35
TEXT_TRESHOLD = 0.25
upload_path = "uploads/"


@st.cache_resource(show_spinner=True)
def init_model():
    model = load_model(CONFIG_PATH, WEIGHTS_PATH)
    model = model.to("cuda:0")
    return model


def download_output_image(image_np, mime_type):
    image_pil = Image.fromarray(image_np)
    image_stream = io.BytesIO()
    if mime_type == "image/jpeg":
        image_format = "JPEG"
    elif mime_type == "image/png":
        image_format = "PNG"
    elif mime_type == "image/bmp":
        image_format = "BMP"
    else:
        raise ValueError("Unsupported MIME type")
    image_pil.save(image_stream, format="JPEG")
    image_bytes = image_stream.getvalue()
    return image_bytes


st.title("✨ GroundingDINO - Zero Shot Object Detection 🐱‍🐉")
st.info(" Let me help you in Zero Shot Object Detection 😉")
col_a, col_b = st.columns(2)

text_prompt = st.text_input(
    "Enter what all do you want me to detect 📝",
    "orange, pear, bowl, plum, pomegranate",
)
image_path = st.file_uploader("Upload Image 🚀", type=["png", "jpg", "bmp", "jpeg"])
if image_path is not None and (
    text_prompt is not None or len(text_prompt.strip()) != 0
):
    with open(os.path.join(upload_path, image_path.name), "wb") as f:
        f.write((image_path).getbuffer())
        uploaded_image_path = os.path.abspath(
            os.path.join(upload_path, image_path.name)
        )
        with st.spinner("Working... 💫"):
            model = init_model()
            image_source, image = load_image(uploaded_image_path)

            boxes, logits, phrases = predict(
                model=model,
                image=image,
                caption=text_prompt,
                box_threshold=BOX_TRESHOLD,
                text_threshold=TEXT_TRESHOLD,
            )

            annotated_frame = annotate(
                image_source=image_source,
                boxes=boxes,
                logits=logits,
                phrases=phrases,
            )
            left_co, cent_co, last_co = st.columns(3)
            with cent_co:
                st.image(
                    annotated_frame[:, :, ::-1],
                    use_column_width=True,
                    caption=f'One Shot Object Detection based output for "{text_prompt}"',
                )
                extension_to_mime = {
                    ".jpeg": "image/jpeg",
                    ".JPEG": "image/jpeg",
                    ".jpg": "image/jpg",
                    ".JPG": "image/jpg",
                    ".png": "image/png",
                    ".PNG": "image/png",
                    ".bmp": "image/bmp",
                    ".BMP": "image/bmp",
                }

                for extension, mime_type in extension_to_mime.items():
                    if image_path.name.endswith(extension):
                        if st.download_button(
                            label="Download Image 📷",
                            data=download_output_image(
                                annotated_frame[:, :, ::-1], mime_type
                            ),
                            file_name=str("output_" + image_path.name),
                            mime=mime_type,
                            use_container_width=True,
                        ):
                            st.success("✅ Download Successful !")
                        break
else:
    st.warning("⚠ Please upload your Image! 😯")

st.markdown(
    "<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=GroundingDINO WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a> with the help of [GroundingDINO](https://github.com/IDEA-Research/GroundingDINO) built by [IDEA-Research](https://github.com/IDEA-Research)✨</center><hr>",
    unsafe_allow_html=True,
)
