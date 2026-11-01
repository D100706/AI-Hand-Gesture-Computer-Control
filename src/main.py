import cv2
import pyautogui

from hand_tracking import HandTracker
from gesture_recognition import classify_gesture
from mouse_control import MouseController
from system_control import SystemController

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.02

def main():
    tracker = HandTracker()
    mouse = MouseController()
    system = SystemController()
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("ERROR: Webcam unavailable. Check Windows camera permissions.")
        tracker.close()
        return

    paused = False
    scroll_anchor = None
    print("Gesture control active. P = pause/resume, Q = quit.")
    print("Emergency stop: move mouse to the top-left screen corner.")

    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                break
            frame = cv2.flip(frame, 1)
            height, width = frame.shape[:2]
            landmarks = tracker.detect(frame) if not paused else None
            gesture = classify_gesture(landmarks) if landmarks else ("PAUSED" if paused else "No hand")
            action = "None"

            if not paused and landmarks:
                if gesture == "Point":
                    mouse.drag(False)
                    mouse.move(landmarks[8])
                    action = "Move cursor"
                elif gesture == "Pinch":
                    mouse.drag(False)
                    mouse.click()
                    action = "Left click"
                elif gesture == "Victory":
                    mouse.drag(False)
                    mouse.double_click()
                    action = "Double click"
                elif gesture == "Fist":
                    mouse.drag(True)
                    action = "Drag / hold"
                elif gesture == "Open Palm":
                    mouse.drag(False)
                    y = landmarks[9].y
                    if scroll_anchor is not None and abs(scroll_anchor - y) > 0.025:
                        pyautogui.scroll(1 if scroll_anchor > y else -1)
                        scroll_anchor = y
                    elif scroll_anchor is None:
                        scroll_anchor = y
                    action = "Scroll"
                elif gesture == "Thumbs Up":
                    mouse.drag(False)
                    system.volume("up")
                    action = "Volume up"
                elif gesture == "Thumbs Down":
                    mouse.drag(False)
                    system.volume("down")
                    action = "Volume down"
                else:
                    mouse.drag(False)
                    scroll_anchor = None
            else:
                mouse.drag(False)
                scroll_anchor = None

            cv2.rectangle(frame, (10, 10), (405, 112), (25, 25, 25), -1)
            cv2.putText(frame, "AI HAND COMPUTER CONTROL", (22, 36),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.58, (80, 220, 255), 2)
            cv2.putText(frame, f"Gesture: {gesture}", (22, 66),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)
            cv2.putText(frame, f"Action: {action}", (22, 94),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.52, (100, 255, 130), 1)
            cv2.putText(frame, "P: Pause/Resume   Q: Quit", (10, height - 18),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)
            cv2.imshow("AI Hand Gesture Computer Control", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            if key == ord("p"):
                paused = not paused
                if paused:
                    mouse.release()
    except pyautogui.FailSafeException:
        print("Emergency failsafe activated. Application stopping.")
    finally:
        mouse.release()
        camera.release()
        tracker.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
