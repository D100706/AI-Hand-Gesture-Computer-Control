import cv2
import mediapipe as mp


class HandTracker:

    def __init__(self):
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            model_complexity=0,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )

        self.drawer = mp.solutions.drawing_utils

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb.flags.writeable = False

        results = self.hands.process(rgb)

        rgb.flags.writeable = True

        if results.multi_hand_landmarks:

            hand = results.multi_hand_landmarks[0]

            self.drawer.draw_landmarks(
                frame,
                hand,
                self.mp_hands.HAND_CONNECTIONS
            )

            return hand.landmark

        return None

    def close(self):
        self.hands.close()