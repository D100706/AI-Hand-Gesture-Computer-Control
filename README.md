# AI Hand Gesture Computer Control System

A webcam-based Python application that maps hand gestures to basic computer actions.

## Features
- Live hand landmark tracking with MediaPipe
- Mouse cursor movement
- Left click and double click
- Drag / hold
- Vertical scrolling
- System volume up/down
- Pause and quit keyboard shortcuts

## Requirements
- Windows 10/11
- Python 3.11
- Webcam

## Setup
1. Extract the ZIP and open the folder in VS Code.
2. Install Python 3.11 if required.
3. Double-click `run.bat`, or use the terminal commands:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python src\main.py
```

4. Allow webcam access when prompted.

## Gesture mapping
See `docs/gesture_mapping.md`.

## Keyboard controls
- `P`: Pause/resume.
- `Q`: Quit.
- Move the mouse to the top-left screen corner to trigger PyAutoGUI's emergency failsafe.

## How it works
OpenCV reads webcam frames. MediaPipe estimates 21 hand landmarks. Geometric rules classify the hand pose, and PyAutoGUI sends the matching mouse or media-key input.

## Safety
This prototype controls your actual mouse and media keys. Test with non-sensitive windows closed. Keep the pause/quit controls available. Detection can vary with lighting, camera angle and hand orientation. It is not intended for safety-critical use.

## Screenshots and demo
Save your own working screenshots in `screenshots/`. Add your demo video link here after recording. No demo video is included in this starter ZIP.
