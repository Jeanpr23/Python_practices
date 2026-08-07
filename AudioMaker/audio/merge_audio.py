from pydub import AudioSegment
import imageio_ffmpeg
from pydub import utils
import shulil

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

AudioSegment.converter = ffmpeg
utils.get_prober_name = lambda: ffmpeg

ffprobe = shutlil.wich("ffprobe")

if ffprobe:
    AudioSegment.ffprobe = ffprobe
    
def merge_audio(tts_file, user_file, output_file):

    tts_audio = AudioSegment.from_file(
        tts_file,
        format="mp3"
    )

    user_audio = AudioSegment.from_file(
        user_file
    )

    final_audio = tts_audio + user_audio

    final_audio.export(
        output_file,
        format="mp3"
    )
