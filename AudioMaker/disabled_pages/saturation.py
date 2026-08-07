import streamlit as st
from config import ENABLE_SATURATION

if not ENABLE_SATURATION:
   st.warning("Saturation page is currently disabled.")
   st.stop()
import os
from cleanup import clean_folder
from pydub import AudioSegment
from effects.saturation import apply_saturation
from components.info_box import show_info_box


clean_folder("uploads", 24)
clean_folder("generated", 24)

st.set_page_config(
    page_title="Saturation",
    page_icon="🔉",
    layout="centered"
)


st.markdown(
    "<h1 style='text-align: center;'>Saturation</h1>",
    unsafe_allow_html=True
)

show_info_box(
   "What is Saturation?",
   """
   “This saturation function evens out peaks, reduces excess bass, and adds a controlled warm
    tone that keeps the audio stable, helping it pass Roblox’s moderation.”

    “For best results, avoid using overly noisy audio before applying saturation, as it can amplify
     the noise and increase the chances of Roblox flagging it as disruptive.”
   """
)

audio_file = st.file_uploader(
    "📂 Upload audio file",
    type=["mp3", "wav", "ogg"]
)

drive = st.slider(
    "Saturation Level",
    min_value=1.0,
    max_value=5.0,
    value=2.0,
    step=1.0
)

apply_button = st.button("Apply Saturation")

if apply_button:

    if audio_file is None:

        st.warning("Please upload an audio file first")

    else:

        os.makedirs("uploads", exist_ok=True)
        os.makedirs("generated", exist_ok=True)

        input_path = os.path.join(
            "uploads",
            audio_file.name
        )


        with open(input_path, "wb") as file:

            file.write(audio_file.getbuffer())


        audio = AudioSegment.from_file(
            input_path
        )

        processed_audio = apply_saturation(
            audio,
            drive
        )

        output_path = os.path.join(
            "generated",
            "saturated_audio.mp3"
        )

        processed_audio.export(
            output_path,
            format="mp3"

        )

        st.success("Saturation applied successfully!")

        st.audio(
            output_path
        )

if audio_file:
    st.success("File received successfully")

    st.audio(audio_file)
