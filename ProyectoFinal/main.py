import math

import cv2
import mediapipe as mp
import numpy as np

def spray_paint(x, y):

    # Draw spray paint effect
    radius = 15
    thickness = -1  # Fill the circle
    color = (0, 255, 0)  # Spray paint color

    # Generate random points inside the circle to simulate spray
    for _ in range(20):  # Adjust the number of iterations per tick
         spray_x = x + int(np.random.uniform(-radius, radius))
         spray_y = y + int(np.random.uniform(-radius, radius))
         cv2.circle(canvas, (spray_x, spray_y), 1, color, thickness)

    return frame

# Initialize Mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

canvas = None

# Initialize video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read frame from webcam
    ret, frame = cap.read()

    if canvas is None:
        canvas = np.zeros((frame.shape[0], frame.shape[1], 3), dtype=np.uint8)

    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb_frame = cv2.flip(rgb_frame, 1)
    frame = cv2.flip(frame, 1)

    # Process the frame with Mediapipe hands
    results = hands.process(rgb_frame)
    frameNoMarks = frame.copy()
    # Check if hands are detected
    if results.multi_hand_landmarks:
        for i in range(len(results.multi_hand_landmarks)):

            mp.solutions.drawing_utils.draw_landmarks(frame, results.multi_hand_landmarks[i], mp_hands.HAND_CONNECTIONS)



            hand_label = "Right" if results.multi_handedness[i].classification[0].label == "Right" else "Left"
            cv2.putText(frame, hand_label,
                        (int(results.multi_hand_landmarks[i].landmark[0].x * frame.shape[1]), int(results.multi_hand_landmarks[i].landmark[0].y * frame.shape[0])),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            if hand_label == "Right":
                frame = spray_paint(int(results.multi_hand_landmarks[i].landmark[8].x  * frame.shape[1]), int(results.multi_hand_landmarks[i].landmark[8].y * frame.shape[0]))
            else:

                thumb_tip = results.multi_hand_landmarks[i].landmark[4]  # Thumb tip landmark index
                thumb_up = thumb_tip.y < results.multi_hand_landmarks[i].landmark[3].y and thumb_tip.y < results.multi_hand_landmarks[i].landmark[0].y and thumb_tip.y < results.multi_hand_landmarks[i].landmark[12].y

                small_finger_tip = results.multi_hand_landmarks[i].landmark[20]
                distance_thumb_index = math.sqrt((thumb_tip.x - small_finger_tip.x) ** 2 +
                                                 (thumb_tip.y - small_finger_tip.y) ** 2 +
                                                 (thumb_tip.z - small_finger_tip.z) ** 2)

                # Example: Check if hand is in a closed fist
                is_closed_fist = distance_thumb_index < 0.1  # Adjust the threshold as needed

                is_v_sign = is_closed_fist and abs(thumb_tip.y - results.multi_hand_landmarks[i].landmark[8].y) > 0.1 and abs(thumb_tip.y - results.multi_hand_landmarks[i].landmark[12].y) > 0.1

                is_pinch = (abs(thumb_tip.y - results.multi_hand_landmarks[i].landmark[8].y) < 0.03 and abs(thumb_tip.x - results.multi_hand_landmarks[i].landmark[8].x) < 0.03) and (abs(thumb_tip.y - results.multi_hand_landmarks[i].landmark[12].y) < 0.03 and abs(thumb_tip.x - results.multi_hand_landmarks[i].landmark[12].x) < 0.03) and (abs(thumb_tip.y - results.multi_hand_landmarks[i].landmark[16].y) < 0.06 and abs(thumb_tip.x - results.multi_hand_landmarks[i].landmark[16].x) < 0.06) and (abs(thumb_tip.y - results.multi_hand_landmarks[i].landmark[20].y) < 0.09 and abs(thumb_tip.x - results.multi_hand_landmarks[i].landmark[20].x) < 0.09)

                if is_pinch:
                    print("Pinch")
                elif is_v_sign:
                    print("V sign")
                elif is_closed_fist:
                    print("Cerrado")
                elif thumb_up:
                    print("Ok")

    # Display the frame
    cv2.imshow('Camera with Tracking', frame)
    cv2.imshow('Spray', canvas)
    frame_with_paint = cv2.add(frameNoMarks, canvas)
    cv2.imshow('Painting in camera', frame_with_paint)


    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()