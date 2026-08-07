shutil
import streamlit as st

st.write("FFMPEG:", shutil.wich("ffmpeg"))
st.write("FFPROBE:", shutil.wich("ffprobe"))

import os

os.makedirs("uploads", exist_ok=True)
os.makedirs("generated", exist_ok=True)

from config import ENABLE_MANIPULATION

if not ENABLE_MANIPULATION:
    st.warning("This pae is currently disabled.")
    st.stop()

    
from russian_twisters import generate_russian_twister
from japanese_twisters import generate_japanese_twister
from tts.speech_generator import generate_audio
from audio.merge_audio import merge_audio
from cleanup import clean_folder
from components.info_box import show_info_box


clean_folder("uploads", 24)
clean_folder("generated", 24)



st.set_page_config(
    page_title="Manipulation",
    page_icon="🗣️",
    layout="centered"
)


st.markdown(
    "<h1 style='text-align: center;'>Manipulation</h1>",
    unsafe_allow_html=True
)

show_info_box(
    "What is Manipulation?",
    """
    “Audio manipulation can alter a recording in ways that make it more difficult for Roblox’s
     moderation systems to detect offensive language present in a song when the audio is
     uploaded.”
    """
)

audio_file = st.file_uploader(
    "📂 Upload audio file",
    type=["mp3", "wav", "ogg"]
)

if audio_file:

    user_audio_path = "uploads/user_audio.mp3"

    with open(user_audio_path, "wb") as f:
        f.write(audio_file.getbuffer())

language = st.selectbox(
    "Choose manipulation language",
    [
        "Russian",
        "Japanese"
    ]
)

generate_button = st.button("Generate manipulation")

if generate_button:

    if not audio_file:

        st.warning(
            "Please upload an audio file first"
        )


    else:

        # Generate tongue twister

        if language == "Russian":

            twister = generate_russian_twister()

        else:

            twister = generate_japanese_twister()



        # Create tts

        tts_path = "generated/tongue_twister.mp3"


        generate_audio(
           twister,
           language,
           tts_path
        )

        final_path = "generated/finished.mp3"

        merge_audio(
            tts_path,
            user_audio_path,
            final_path
        )
            

        st.success("Manipulation applied successfully!")

        st.audio(final_path)


if audio_file:
    st.success("File received successfully")

    st.audio(audio_file)
