import streamlit as st
import edge_tts
import asyncio

VOICES = {
    "English": "en-US-GuyNeural",
    "Spanish": "es-ES-AlvaroNeural",
    "Russian": "ru-RU-DmitryNeural",
    "Japanese": "ja-JP-KeitaNeural"
}

async def create_audio(text, voice):
    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save("audio/output.mp3")

st.title("My TTS Website")

user_text = st.text_area(
    "Write something here:"

)

language = st.selectbox(
    "Choose a language",
    [
        "English",
        "Spanish",
        "Russian",
        "Japanese"
    ]
)

if st.button("Generate Audio"):

   voice = VOICES[language]

   asyncio.run(
       create_audio(
           user_text,
           voice
       )
   )

   st.success("Audio created!")

   st.audio("audio/output.mp3")