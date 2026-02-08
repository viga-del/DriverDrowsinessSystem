# Driver Drowsiness Detection System

A real-time Driver Drowsiness Detection System built using Python and OpenCV that monitors a driver's eye activity through a webcam and detects signs of fatigue. The system triggers an alarm when prolonged eye closure is detected and logs driver activity data for later analysis.

This project demonstrates the use of computer vision techniques for building a basic driver safety monitoring system.

---

## Project Description

Driver fatigue is one of the leading causes of road accidents worldwide. This project implements a vision-based monitoring system that continuously tracks the driver's face and eyes using a webcam feed.

The system analyzes consecutive frames to determine whether the driver’s eyes are open or closed. If the eyes remain closed beyond a predefined threshold, the system classifies the driver as drowsy and activates an alert mechanism.

In addition to real-time monitoring, the system records driver status information into a CSV file for tracking and analysis.

---

## Key Features

- Real-time webcam monitoring
- Face detection using Haar Cascade classifier
- Eye detection and tracking
- Blink detection using frame transitions
- Drowsiness detection using closed-eye frame threshold
- Alarm alert when drowsiness is detected
- Visual monitoring dashboard
- FPS (Frames Per Second) display
- Progress indicator for eye-closure duration
- Driver activity logging in CSV format

---

## System Workflow

1. Capture live video from webcam.
2. Convert frame to grayscale.
3. Detect face region.
4. Detect eyes inside the face region.
5. Monitor consecutive frames where eyes are not detected.
6. Trigger alarm if threshold is exceeded.
7. Display driver status on screen.
8. Store driver monitoring data in CSV file.

---

## Technologies Used

- Python
- OpenCV
- Pygame (for alarm sound)
- Haar Cascade Classifiers
- CSV File Handling

---

## Project Structure

DriverDrowsinessSystem/
│
├── main.py
├── alarm.wav
├── driver_data.csv
└── haarcascade/
├── haarcascade_frontalface_default.xml
└── haarcascade_eye.xml


---

## Installation and Setup

### Install dependencies
pip install opencv-python pygame


### Run the application
python main.py


Press **Q** to exit the system.

---

## Output

The system generates a CSV file:

driver_data.csv


Each row contains:
- Timestamp
- Eye Status (OPEN / CLOSED)
- Blink Count
- Closed Frame Count

This data can be used to analyze driver alertness patterns.

---

## Detection Logic

The drowsiness detection mechanism is based on consecutive frames where eyes are not detected.

- Eye closure is confirmed only after multiple consecutive frames.
- Blink detection is implemented using OPEN → CLOSED → OPEN transitions.
- Alarm is triggered when closed-eye frames exceed the threshold.
- Alarm stops automatically when the driver becomes alert again.

---

## Future Enhancements

- Facial landmark detection using dlib
- Eye Aspect Ratio (EAR)–based detection
- Deep learning–based eye detection
- Low-light performance improvements
- Head pose estimation
- Raspberry Pi deployment
- Mobile application integration
- Driver identity tracking
- Cloud-based monitoring system

---

## Learning Outcomes

Through this project, the following concepts were implemented:

- Real-time video processing
- Object detection using OpenCV
- Event detection using frame analysis
- Human alertness monitoring logic
- Alarm integration
- Data logging and monitoring system design

---

## Author

Vigashini S  
Engineering Student
