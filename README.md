# AI Hand Gesture Computer Control System 🖐️

### Control your computer using hand gestures — no physical mouse required!

## 📌 Project Overview

The AI Hand Gesture Computer Control System is a real-time computer vision application that allows users to interact with their computer using simple hand gestures.

Using a webcam, the system detects and recognizes hand movements and translates them into computer operations such as cursor movement, clicking, scrolling, dragging and volume adjustment.

## ✨ Key Features

* Real-time hand detection and tracking.
* Touchless mouse cursor control.
* Left-click and double-click functionality.
* Drag and drop operations.
* Scroll control using hand gestures.
* Volume adjustment through thumb gestures.
* Interactive dashboard with live gesture recognition.
* Pause and resume functionality.

## 🖐️ Gesture Controls

| Hand Gesture           | Computer Action |
| ---------------------- | --------------- |
| ☝️ Index Finger        | Move Cursor     |
| 🤏 Thumb + Index Pinch | Left Click      |
| ✌️ Victory / Peace     | Double Click    |
| ✊ Closed Fist          | Drag and Drop   |
| 🖐️ Open Palm          | Scroll          |
| 👍 Thumbs Up           | Volume Up       |
| 👎 Thumbs Down         | Volume Down     |

## 🛠️ Technologies Used

* **Python** – Core programming language.
* **OpenCV** – Webcam access and image processing.
* **MediaPipe** – Real-time hand landmark detection.
* **NumPy** – Numerical operations.
* **PyAutoGUI** – Mouse and system control.

## ⚙️ System Requirements

* Windows 10/11
* Python 3.10 or compatible version
* Webcam
* Working internet connection for initial dependency installation

## 📂 Project Structure

```text
AI-Hand-Gesture-Computer-Control/
│
├── src/
│   ├── main.py
│   ├── hand_tracking.py
│   ├── gesture_recognition.py
│   ├── mouse_control.py
│   └── system_control.py
│
├── docs/
│   └── gesture_mapping.md
│
├── screenshots/
│
├── requirements.txt
├── run.bat
├── README.md
├── START_HERE.txt
└── .gitignore
```

## 🚀 Installation and Execution

### Step 1: Clone the repository

```bash
git clone https://github.com/D100706/AI-Hand-Gesture-Computer-Control.git
```

### Step 2: Open the project folder

```bash
cd AI-Hand-Gesture-Computer-Control
```

### Step 3: Create a virtual environment

```bash
python -m venv .venv
```

### Step 4: Activate the environment

```bash
.venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the application

```bash
python src\main.py
```

Allow webcam access when prompted.

## 🧠 Working Principle

1. The webcam captures live video of the user's hand.
2. OpenCV processes the video frames.
3. MediaPipe detects 21 hand landmarks.
4. The gesture recognition module analyses landmark positions.
5. The system identifies the corresponding hand gesture.
6. PyAutoGUI executes the associated computer operation.
7. The dashboard displays the detected gesture and current action.

## ⌨️ Keyboard Controls

| Key | Function         |
| --- | ---------------- |
| P   | Pause / Resume   |
| Q   | Quit Application |

The PyAutoGUI failsafe is enabled. Moving the physical mouse to the top-left corner can trigger its failsafe.

## 🔮 Future Enhancements

* Support for multiple hand gestures.
* Voice-based computer control.
* Customizable gesture mappings.
* Improved gesture recognition accuracy.
* Cross-platform compatibility.
* Accessibility-focused features.

## 🎯 Project Objective

The primary objective is to develop an intelligent, touchless computer interaction system that improves accessibility and provides an alternative method of controlling computers using artificial intelligence and computer vision.

## 👩‍💻 Developer

**Dhanushree**

AI & Data Science Engineering Student

GitHub: [D100706](https://github.com/D100706)

---

⭐ If you find this project interesting, consider starring the repository!
