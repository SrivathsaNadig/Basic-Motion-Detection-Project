import threading
import winsound
import cv2
import imutils

# Setting Cam and resolution
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Index of camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Capturing the initial frame
_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (5, 5), 0)

alarm = False
alarm_mode = False
alarm_counter = 0

def beep_alarm():
    global alarm
    while alarm_mode:
        if alarm:
            for i in range(5):
                print("ALARM")
                winsound.Beep(2500, 1000)  # Reduced beep duration to 500ms
            alarm = False

# Comparing the current frame with the previous frame
while True:
    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

        difference = cv2.absdiff(frame_bw, start_frame)
        threshold = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)[1]  # Increased threshold value
        start_frame = frame_bw

        if threshold.sum() > 1000:  # Increased threshold sum value to reduce sensitivity
            alarm_counter += 1
        else:
            if alarm_counter > 0:
                alarm_counter -= 1

        cv2.imshow("Cam", threshold)
    else:
        cv2.imshow("Cam", frame)

    if alarm_counter > 20:
        if not alarm:
            alarm = True
            threading.Thread(target=beep_alarm).start()

    key_pressed = cv2.waitKey(30)
    if key_pressed == ord('t'):
        alarm_mode = not alarm_mode
        alarm_counter = 0
    if key_pressed == ord('q'):
        alarm_mode = False
        break

cap.release()
cv2.destroyAllWindows()
