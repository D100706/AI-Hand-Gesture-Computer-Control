import time
import pyautogui

class SystemController:
    def __init__(self):
        self.last_action = 0

    def volume(self, direction):
        now = time.time()
        if now - self.last_action < 0.25:
            return
        pyautogui.press("volumeup" if direction == "up" else "volumedown")
        self.last_action = now
