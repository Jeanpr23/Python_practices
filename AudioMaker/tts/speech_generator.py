import edge_tts
import asyncio

VOICES = {

    "Russian": "ru-RU-DmitryNeural",

    "Japanese": "ja-JP-KeitaNeural"

}


REPEAT_TIMES = {

    "Russian": 4,

    "Japanese": 6
}

def repeat_text(text, language):

    times = REPEAT_TIMES[language]

    repeated_text = " ".join(
        [text] * times
    )

    return repeated_text


async def create_tts(text, language, output_file):

    voice = VOICES[language]

    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save(output_file)


def generate_audio(text, language, filename):


    text = repeat_text(
        text,
        language
    )

    asyncio.run(
        create_tts(
            text,
            language,
            filename
        )
    )