from pydub.effects import compress_dynamic_range

def saturation_effect(audio, drive):

     # Main Saturation

    amount = drive * 2.0

    processed = audio + amount 

    # Control of high frecuences
    processed = processed.low_pass_filter(14000)

    return processed

def control_bass(audio):

    audio = audio.high_pass_filter(100)

    return audio


def make_loud(audio, drive):

    gain = drive * 4

    louder = audio + gain

    return louder



def final_tape(audio):

    # Final tape to control range

    covered = compress_dynamic_range(

        audio,

        threshold=-18.0,

        ratio=10.0,

        attack=5,

        release=150
    )

    return covered

def apply_saturation(audio, drive):

    # 1 - Strong effect

    processed = saturation_effect(
        audio,
        drive
    )

    processed = control_bass(
        processed
    )

    processed = make_loud(
        processed,
        drive
    )

    # 2 Final tape
    processed = final_tape(
        processed
    )

    return processed