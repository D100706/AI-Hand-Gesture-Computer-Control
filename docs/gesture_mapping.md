# Gesture-to-Action Mapping

| Gesture | Computer action |
|---|---|
| Index finger only (Point) | Move mouse cursor |
| Thumb and index fingertips pinched | Left click |
| Index + middle fingers raised (Victory) | Double click |
| Closed fist | Hold left mouse button / drag |
| Open palm | Scroll vertically |
| Thumbs up | Increase system volume |
| Thumbs down | Decrease system volume |

Keyboard shortcuts:
- `P`: Pause/resume gesture control.
- `Q`: Quit the application.

MediaPipe detects 21 hand landmarks. The application uses landmark positions and distances for rule-based gesture classification; it does not train a custom model.
