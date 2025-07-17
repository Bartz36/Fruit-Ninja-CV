# 🍉 Play Fruit Ninja with Your Hand!

> Control your computer's mouse using hand gestures and finger tracking in real time — built with Python, OpenCV, and MediaPipe.

## Overview

This project leverages computer vision and hand-tracking to simulate mouse movement and clicks using just your hand in front of a webcam. The system detects your index finger to move the cursor and your pinky to simulate clicking, enabling intuitive, touchless control.

Ideal for experimenting with human-computer interaction (HCI), gesture-based interfaces, or prototyping accessibility tools.

## Tech Stack

- **Python**
- **OpenCV** for image processing
- **MediaPipe** + **cvzone** for hand tracking
- **pyautogui** & **pynput** for simulating mouse control
- **NumPy**

## How It Works

- Uses your **webcam** to capture real-time video.
- Detects and tracks hand landmarks (21 key points).
- Converts the **index finger tip** position to mouse cursor coordinates.
- Simulates mouse **click/unclick** based on the **pinky finger's** position.
- Draws visual markers and a boundary box on the webcam feed.

