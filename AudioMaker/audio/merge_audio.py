from pydub import AudioSegment


def merge_audio(tts_file, user_file, output_file):

    tts_audio = AudioSegment.from_file(
        tts_file
    )

    user_audio = AudioSegment.from_file(
        user_file
    )

    final_audio = tts_audio + user_audio

    final_audio.export(
        output_file,
        format="mp3"
    )