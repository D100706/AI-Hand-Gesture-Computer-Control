import time
import pyautogui


class MouseController:

    def __init__(self, smoothing=2):

        self.width, self.height = pyautogui.size()

        self.smoothing = max(1, smoothing)

        self.x = self.width / 2
        self.y = self.height / 2

        self.last_click = 0
        self.last_double = 0

        self.dragging = False

        pyautogui.PAUSE = 0
        pyautogui.FAILSAFE = True

    def move(self, landmark):

        # Correct horizontal direction for mirrored webcam
        target_x = landmark.x * self.width

        target_y = landmark.y * self.height

        target_x = max(0, min(target_x, self.width - 1))
        target_y = max(0, min(target_y, self.height - 1))

        self.x += (target_x - self.x) / self.smoothing
        self.y += (target_y - self.y) / self.smoothing

        pyautogui.moveTo(
            int(self.x),
            int(self.y),
            duration=0
        )

    def click(self):

        now = time.time()

        if now - self.last_click > 0.6:

            pyautogui.click()
            self.last_click = now

    def double_click(self):

        now = time.time()

        if now - self.last_double > 1.0:

            pyautogui.doubleClick(interval=0.12)
            self.last_double = now

    def drag(self, enabled):

        if enabled and not self.dragging:

            pyautogui.mouseDown()
            self.dragging = True

        elif not enabled and self.dragging:

            pyautogui.mouseUp()
            self.dragging = False

    def release(self):

        if self.dragging:

            pyautogui.mouseUp()
            self.dragging = False