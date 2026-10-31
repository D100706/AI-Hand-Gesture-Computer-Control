import time
import pyautogui


class SystemController:

    def __init__(self, cooldown=0.25):

        self.cooldown = cooldown
        self.last_action = {
            "up": 0,
            "down": 0
        }

        pyautogui.PAUSE = 0

    def volume(self, direction):

        if direction not in ("up", "down"):
            raise ValueError(
                "Invalid direction. Use 'up' or 'down'."
            )

        now = time.time()

        if now - self.last_action[direction] < self.cooldown:
            return

        try:

            if direction == "up":
                pyautogui.press("volumeup")

            else:
                pyautogui.press("volumedown")

            self.last_action[direction] = now

        except Exception as error:

            print(f"Volume control error: {error}")