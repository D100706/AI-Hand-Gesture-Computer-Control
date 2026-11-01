import math

def classify_gesture(lm):
    if lm is None:
        return "No hand"

    index_up = lm[8].y < lm[6].y
    middle_up = lm[12].y < lm[10].y
    ring_up = lm[16].y < lm[14].y
    pinky_up = lm[20].y < lm[18].y
    pinch = math.hypot(lm[4].x - lm[8].x, lm[4].y - lm[8].y) < 0.045

    if pinch:
        return "Pinch"
    thumb_up = lm[4].y < lm[3].y < lm[2].y
    thumb_down = lm[4].y > lm[3].y > lm[2].y

    if thumb_up and not any((index_up, middle_up, ring_up, pinky_up)):
        return "Thumbs Up"
    if thumb_down and not any((index_up, middle_up, ring_up, pinky_up)):
        return "Thumbs Down"
    if index_up and middle_up and not ring_up and not pinky_up:
        return "Victory"
    if index_up and not middle_up and not ring_up and not pinky_up:
        return "Point"
    if all((index_up, middle_up, ring_up, pinky_up)):
        return "Open Palm"
    if not any((index_up, middle_up, ring_up, pinky_up)):
        return "Fist"
    return "Unknown"
