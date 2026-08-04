import os 
import time

def clean_folder(folder, hours=24):

    current_time = time.time()

    if not os.path.exists(folder):
        return

    for filename in os.listdir(folder):

        file_path = os.path.join(
            folder,
            filename
        )

        if os.path.isfile(file_path):

            file_age = current_time - os.path.getmtime(file_path)

            if file_age > hours * 3600:

                os.remove(file_path)