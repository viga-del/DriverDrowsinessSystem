import cv2
import time
from pygame import mixer
import csv
from datetime import datetime

# -------------------- Alarm Setup --------------------
mixer.init()
alarm_sound = mixer.Sound("alarm.wav")

# -------------------- Haar Cascades --------------------
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')

# -------------------- Video Capture --------------------
cap = cv2.VideoCapture(0)
cv2.namedWindow("Driver Monitor", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Driver Monitor", 900, 600)

# -------------------- Variables --------------------
closed_frames = 0
alarm_playing = False
blink_count = 0
prev_eye_closed = False
start_time = time.time()

# -------------------- CSV Setup --------------------
filename = "driver_data.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Eye Status", "Blink Count", "Closed Frames"])  # header

# -------------------- Main Loop --------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (900, 600))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eye_status = "NO FACE"

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) == 0:
            closed_frames += 1
            eye_status = "CLOSED"
        else:
            if prev_eye_closed:
                blink_count += 1
            closed_frames = 0
            alarm_playing = False
            eye_status = "OPEN"

        prev_eye_closed = (len(eyes) == 0)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # -------------------- FPS Calculation --------------------
    fps = int(1 / max(time.time() - start_time, 0.001))
    start_time = time.time()

    # -------------------- Progress Bar --------------------
    bar_length = min(closed_frames * 10, 200)
    cv2.rectangle(frame, (10, 80), (10 + bar_length, 100), (0, 0, 255), -1)

    # -------------------- Info Panel --------------------
    cv2.putText(frame, f"Score: {closed_frames}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"Eye Status: {eye_status}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"Blinks: {blink_count}", (10, 130),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"FPS: {fps}", (750, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # -------------------- Drowsiness Alert --------------------
    if closed_frames > 20:
        cv2.putText(frame, "STATUS: DROWSY!", (250, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        if not alarm_playing:
            alarm_sound.play()
            alarm_playing = True
    else:
        cv2.putText(frame, "STATUS: ALERT", (250, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # -------------------- Store Data to CSV --------------------
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, eye_status, blink_count, closed_frames])

    # -------------------- Display --------------------
    cv2.imshow("Driver Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------- Cleanup --------------------
cap.release()
cv2.destroyAllWindows()