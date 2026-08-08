import subprocess
import imageio_ffmpeg


def merge_audio(tts_file, user_file, output_file):

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

    command = [
        ffmpeg,
        "-y",
        "-i", tts_file,
        "-i", user_file,
        "-filter_complex",
        "[0:a][1:a]concat=n=2:v=0:a=1[out]",
        "-map", "[out]",
        "-c:a", "libmp3lame",
        "-q:a", "0",
        output_file
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(
            "FFmpeg command:\n"
            + " ".join(command)
            + "\n\nFFmpeg error:\n"
            + result.stderr
        )
