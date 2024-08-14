# Basic-Motion-Detection-Project
Basic motion detector. Detects motion, triggers alarm. Uses OpenCV, imutils, threading. Press 't' to toggle, 'q' to quit. Requires Python, OpenCV, imutils, winsound.



Code Breakdown
The provided Python code implements a basic motion detection system using OpenCV, imutils, and the threading module. Here's a breakdown of its components:

Import necessary libraries:

threading: For handling the alarm sound in a separate thread.
winsound: For generating the alarm sound.
cv2: For image processing and video capturing.
imutils: For image utility functions.
Camera setup and initialization:

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW): Opens the default camera (index 0) using DirectShow.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640): Sets the frame width to 640 pixels.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480): Sets the frame height to 480 pixels.
Captures the initial frame, resizes it, converts it to grayscale, and applies Gaussian blur for noise reduction.
Variable initialization:

alarm: A flag to indicate whether the alarm should be sounding.
alarm_mode: A flag to control whether the motion detection system is active.
alarm_counter: A counter to track the number of consecutive frames with significant motion.
Alarm function:

beep_alarm(): Plays a continuous beeping sound using winsound.Beep() while alarm_mode is active and alarm is True.
Main loop:

Continuously captures frames from the camera.
If alarm_mode is active:
Converts the frame to grayscale, applies Gaussian blur.
Calculates the difference between the current frame and the previous frame.
Applies thresholding to detect significant changes.
Updates the reference frame.
If the number of changed pixels exceeds a threshold, increments alarm_counter.
If alarm_counter decreases below 0, resets it to 0.
Displays the threshold image or the original frame based on alarm_mode.
If alarm_counter exceeds a certain threshold, sets alarm to True and starts a new thread for the alarm sound.
Handles keyboard input to toggle alarm_mode and quit the program.
How it Works
The code initializes the camera and captures the initial frame as a reference.
It enters a loop that continuously captures frames from the camera.
If alarm_mode is active, it compares the current frame with the previous frame to detect motion.
If significant motion is detected, the alarm_counter is incremented.
If alarm_counter reaches a certain threshold, the alarm is triggered.
The code displays the processed image or the original frame based on alarm_mode.
Keyboard input is used to control the alarm mode and exit the program.
Potential Improvements
Adjust sensitivity: The threshold values for motion detection and alarm triggering can be fine-tuned based on the environment.
Error handling: Add error handling for camera access and file operations.
Alarm customization: Allow users to customize the alarm sound, duration, and frequency.
Video recording: Implement video recording when motion is detected.
Image analysis: Perform more advanced image analysis techniques for object detection or tracking.
