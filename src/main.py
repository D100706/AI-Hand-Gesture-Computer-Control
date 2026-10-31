import cv2
import time
import pyautogui

from hand_tracking import HandTracker
from gesture_recognition import classify_gesture
from mouse_control import MouseController
from system_control import SystemController


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0

# Dark theme colours
BLACK = (12, 12, 12)
CYAN = (255, 200, 0)
WHITE = (245, 245, 245)
GRAY = (150, 150, 150)
GREEN = (70, 230, 100)
RED = (70, 70, 255)
YELLOW = (0, 200, 255)

WINDOW_NAME = "AI Gesture Control | Dark Mode"

# Button positions
PAUSE_BUTTON = (20, 420, 175, 465)
EXIT_BUTTON = (195, 420, 350, 465)


def mouse_callback(event, x, y, flags, state):

    if event != cv2.EVENT_LBUTTONDOWN:
        return

    px1, py1, px2, py2 = PAUSE_BUTTON
    ex1, ey1, ex2, ey2 = EXIT_BUTTON

    # Pause / Resume button
    if px1 <= x <= px2 and py1 <= y <= py2:
        state["paused"] = not state["paused"]

    # Exit button
    elif ex1 <= x <= ex2 and ey1 <= y <= ey2:
        state["exit"] = True


def draw_button(frame, position, text, color):

    x1, y1, x2, y2 = position

    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        color,
        -1
    )

    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        WHITE,
        1
    )

    text_size = cv2.getTextSize(
        text,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        2
    )[0]

    text_x = x1 + (x2 - x1 - text_size[0]) // 2
    text_y = y1 + (y2 - y1 + text_size[1]) // 2

    cv2.putText(
        frame,
        text,
        (text_x, text_y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        WHITE,
        2
    )


def draw_dashboard(frame, gesture, action, fps, paused):

    height, width = frame.shape[:2]

    # Main dark panel
    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (10, 10),
        (405, 205),
        BLACK,
        -1
    )

    cv2.addWeighted(
        overlay,
        0.90,
        frame,
        0.10,
        0,
        frame
    )

    cv2.rectangle(
        frame,
        (10, 10),
        (405, 205),
        CYAN,
        1
    )

    # Header
    cv2.putText(
        frame,
        "AI GESTURE CONTROL",
        (25, 42),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        CYAN,
        2
    )

    cv2.line(
        frame,
        (25, 55),
        (390, 55),
        GRAY,
        1
    )

    # Gesture
    cv2.putText(
        frame,
        "GESTURE",
        (25, 88),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        GRAY,
        1
    )

    cv2.putText(
        frame,
        gesture.upper(),
        (190, 88),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.52,
        GREEN,
        2
    )

    # Action
    cv2.putText(
        frame,
        "ACTION",
        (25, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        GRAY,
        1
    )

    cv2.putText(
        frame,
        action.upper(),
        (190, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.52,
        WHITE,
        1
    )

    # FPS
    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (25, 155),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        CYAN,
        1
    )

    # System status
    status = "PAUSED" if paused else "ACTIVE"
    status_color = RED if paused else GREEN

    cv2.circle(
        frame,
        (205, 150),
        5,
        status_color,
        -1
    )

    cv2.putText(
        frame,
        status,
        (220, 155),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        status_color,
        2
    )

    # Camera indicator
    cv2.circle(
        frame,
        (370, 30),
        5,
        GREEN,
        -1
    )

    cv2.putText(
        frame,
        "CAMERA ON",
        (285, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.35,
        WHITE,
        1
    )

    # Bottom control panel
    cv2.rectangle(
        frame,
        (10, 395),
        (390, 480),
        BLACK,
        -1
    )

    cv2.putText(
        frame,
        "APPLICATION CONTROLS",
        (20, 415),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.4,
        CYAN,
        1
    )

    # Interactive buttons
    if paused:
        draw_button(
            frame,
            PAUSE_BUTTON,
            "RESUME",
            GREEN
        )
    else:
        draw_button(
            frame,
            PAUSE_BUTTON,
            "PAUSE",
            YELLOW
        )

    draw_button(
        frame,
        EXIT_BUTTON,
        "EXIT",
        RED
    )

    return frame


def main():

    tracker = None
    mouse = None
    camera = None

    state = {
        "paused": False,
        "exit": False
    }

    scroll_anchor = None

    previous_time = time.time()
    fps = 0

    try:

        tracker = HandTracker()
        mouse = MouseController()
        system = SystemController()

        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        if not camera.isOpened():
            print("ERROR: Webcam unavailable.")
            return

        cv2.namedWindow(WINDOW_NAME)

        cv2.setMouseCallback(
            WINDOW_NAME,
            mouse_callback,
            state
        )

        print("AI Gesture Control Dashboard Started")
        print("Click PAUSE / RESUME / EXIT")
        print("Keyboard: P = Pause, Q = Exit")

        while True:

            success, frame = camera.read()

            if not success:
                print("Webcam frame unavailable.")
                break

            frame = cv2.flip(frame, 1)

            # FPS calculation
            current_time = time.time()
            delta = current_time - previous_time

            if delta > 0:
                instant_fps = 1 / delta
                fps = (
                    fps * 0.8 + instant_fps * 0.2
                    if fps else instant_fps
                )

            previous_time = current_time

            paused = state["paused"]

            landmarks = (
                tracker.detect(frame)
                if not paused else None
            )

            gesture = (
                classify_gesture(landmarks)
                if landmarks is not None
                else ("PAUSED" if paused else "No hand")
            )

            action = "Waiting"

            if not paused and landmarks is not None:

                if gesture == "Point":

                    mouse.drag(False)
                    mouse.move(landmarks[8])
                    action = "Moving Cursor"

                elif gesture == "Pinch":

                    mouse.drag(False)
                    mouse.click()
                    action = "Left Click"

                elif gesture == "Victory":

                    mouse.drag(False)
                    mouse.double_click()
                    action = "Double Click"

                elif gesture == "Fist":

                    mouse.drag(True)
                    action = "Dragging"

                elif gesture == "Open Palm":

                    mouse.drag(False)

                    current_y = landmarks[9].y

                    if scroll_anchor is not None:

                        if abs(scroll_anchor - current_y) > 0.025:

                            pyautogui.scroll(
                                1 if scroll_anchor > current_y else -1
                            )

                            scroll_anchor = current_y

                    else:
                        scroll_anchor = current_y

                    action = "Scrolling"

                elif gesture == "Thumbs Up":

                    mouse.drag(False)
                    system.volume("up")
                    action = "Volume Up"

                elif gesture == "Thumbs Down":

                    mouse.drag(False)
                    system.volume("down")
                    action = "Volume Down"

                else:

                    mouse.drag(False)
                    scroll_anchor = None
                    action = "No Action"

            else:

                mouse.drag(False)
                scroll_anchor = None

            # Release mouse when paused
            if paused:
                mouse.release()

            frame = draw_dashboard(
                frame,
                gesture,
                action,
                fps,
                paused
            )

            cv2.imshow(WINDOW_NAME, frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

            elif key == ord("p"):

                state["paused"] = not state["paused"]
                scroll_anchor = None

                if state["paused"]:
                    mouse.release()

            if state["exit"]:
                break

    except pyautogui.FailSafeException:

        print("Emergency failsafe activated.")

    except Exception as error:

        print(f"ERROR: {error}")

    finally:

        if mouse is not None:
            mouse.release()

        if camera is not None:
            camera.release()

        if tracker is not None:
            tracker.close()

        cv2.destroyAllWindows()

        print("Dashboard closed successfully.")


if __name__ == "__main__":
    main()