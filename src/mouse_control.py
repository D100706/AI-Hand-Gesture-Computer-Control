import time
import pyautogui

class MouseController:
    def __init__(self, smoothing=5):
        self.width, self.height = pyautogui.size()
        self.smoothing = smoothing
        self.x, self.y = self.width / 2, self.height / 2
        self.last_click = 0
        self.last_double = 0
        self.dragging = False

    def move(self, landmark):
        tx = (1 - landmark.x) * self.width
        ty = landmark.y * self.height
        self.x += (tx - self.x) / self.smoothing
        self.y += (ty - self.y) / self.smoothing
        pyautogui.moveTo(self.x, self.y, duration=0)

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
