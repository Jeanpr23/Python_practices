import cv2
import time
last_alert = 0
last_no_motion = 0

camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

ret, frame = camera.read()
if not ret:
    print("Camera error")
    exit()


sky = frame[0:300, :]
prev_frame = cv2.cvtColor(sky, cv2.COLOR_BGR2GRAY)

while True: 
    ret, frame = camera.read()

    sky = frame[0:300, :]

    gray = cv2.cvtColor(sky, cv2.COLOR_BGR2GRAY)

    # sharpening kernel
    import numpy as np
    kernel = [[0, -1, 0],
              [-1, 5, -1],
              [0, -1, 0]]
    kernel = np.array(kernel)
    gray = cv2.filter2D(gray, -1, kernel)

    diff = cv2.absdiff(prev_frame, gray)

    if diff.mean() > 5:
        if time.time() - last_alert > 2:
            print("Sky movement detected!")
            last_alert = time.time()
            last_no_motion = time.time()
    
    else:
        if time.time() - last_no_motion > 3:
            print("No movement detected in sky.")
            last_no_motion = time.time()

    prev_frame = gray

    cv2.imshow("sky Detector", frame)
               
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()