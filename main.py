import cv2
import pyautogui
import time
from gestures import count_fingers

from mediapipe.python.solutions import hands as mp_hands
from mediapipe.python.solutions import drawing_utils as mp_draw

cap = cv2.VideoCapture(0)

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

last_action_time = 0
cooldown = 2

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    gesture_text = "None"

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            fingers = count_fingers(handLms)
            total = sum(fingers)

            current_time = time.time()

            if current_time - last_action_time > cooldown:
                if total == 0:
                    pyautogui.press("playpause")
                    gesture_text = "Play/Pause"
                elif total == 1:
                    pyautogui.press("volumeup")
                    gesture_text = "Volume Up"
                elif total == 2:
                    pyautogui.press("volumedown")
                    gesture_text = "Volume Down"
                elif total == 5:
                    pyautogui.press("space")
                    gesture_text = "Pause"
                last_action_time = current_time

    cv2.putText(
        img,
        f"Gesture: {gesture_text}",
        (10, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Gesture Media Player", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()