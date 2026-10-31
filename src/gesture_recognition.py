import math


def classify_gesture(lm):

    if lm is None or len(lm) < 21:
        return "No hand"

    # Finger detection
    index_up = lm[8].y < lm[6].y
    middle_up = lm[12].y < lm[10].y
    ring_up = lm[16].y < lm[14].y
    pinky_up = lm[20].y < lm[18].y

    fingers = (index_up, middle_up, ring_up, pinky_up)

    # Thumb and index finger distance
    pinch_distance = math.hypot(
        lm[4].x - lm[8].x,
        lm[4].y - lm[8].y
    )

    pinch = pinch_distance < 0.045

    # Thumb direction
    thumb_up = lm[4].y < lm[3].y < lm[2].y
    thumb_down = lm[4].y > lm[3].y > lm[2].y

    # Gesture classification

    if pinch:
        return "Pinch"

    if thumb_up and not any(fingers):
        return "Thumbs Up"

    if thumb_down and not any(fingers):
        return "Thumbs Down"

    if index_up and middle_up and not ring_up and not pinky_up:
        return "Victory"

    if index_up and not middle_up and not ring_up and not pinky_up:
        return "Point"

    if all(fingers):
        return "Open Palm"

    if not any(fingers):
        return "Fist"

    return "Unknown"