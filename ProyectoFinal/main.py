import math

import cv2
import mediapipe as mp
import numpy as np
import time

def spray_paint(x, y):

    # Draw spray paint effect
    radius = 15
    thickness = -1  # Fill the circle

    # Generate random points inside the circle to simulate spray

    if color == (0,0,0):
        cv2.circle(canvas, (x, y), 15, (color), thickness)
    else:
        for _ in range(20):  # Adjust the number of iterations per tick
         spray_x = x + int(np.random.uniform(-radius, radius))
         spray_y = y + int(np.random.uniform(-radius, radius))
         cv2.circle(canvas, (spray_x, spray_y), 1, (color), thickness)


    return frame

def brush_paint(x, y):
    radius = 5
    thickness = -1  # Fill the circle

    cv2.circle(canvas, (x, y), radius, (color), thickness)

    return frame

def timer_check(ind):
    global timers_signs
    t = time.time()
    auxT = timers_signs[ind]
    timers_signs = [0,0,0,0,0]
    timers_signs[ind] = auxT
    if timers_signs[ind] == 0:
        timers_signs[ind] = t
        return False
    else:
        if t - timers_signs[ind] < 2:
            return False
        else:
            timers_signs[ind] = 0
            return True


# Initialize Mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

canvas = None
color = (0, 255, 0)  # Spray paint color
paint_type = "spray"
timers_signs = [0,0,0,0,0]
msg_change = ""
t0 = 0

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
                if paint_type == "spray":
                    frame = spray_paint(int(results.multi_hand_landmarks[i].landmark[8].x  * frame.shape[1]), 
                                        int(results.multi_hand_landmarks[i].landmark[8].y * frame.shape[0]))
                elif paint_type == "brush":
                    frame = brush_paint(int(results.multi_hand_landmarks[i].landmark[8].x  * frame.shape[1]), 
                                        int(results.multi_hand_landmarks[i].landmark[8].y * frame.shape[0]))
                    
            else:

                thumb_tip = results.multi_hand_landmarks[i].landmark[4]  # Thumb tip landmark index

                distance_thumb_pointer = math.sqrt((thumb_tip.x - results.multi_hand_landmarks[i].landmark[8].x) ** 2 +
                                                 (thumb_tip.y - results.multi_hand_landmarks[i].landmark[8].y) ** 2 +
                                                 (thumb_tip.z - results.multi_hand_landmarks[i].landmark[8].z) ** 2)

                is_thumb_up = (thumb_tip.y < results.multi_hand_landmarks[i].landmark[3].y 
                               and thumb_tip.y < results.multi_hand_landmarks[i].landmark[0].y 
                               and thumb_tip.y < results.multi_hand_landmarks[i].landmark[12].y 
                               and (distance_thumb_pointer > 0.1))

                small_finger_tip = results.multi_hand_landmarks[i].landmark[20]
                distance_thumb_small = math.sqrt((thumb_tip.x - small_finger_tip.x) ** 2 +
                                                 (thumb_tip.y - small_finger_tip.y) ** 2 +
                                                 (thumb_tip.z - small_finger_tip.z) ** 2)

                is_closed_fist = distance_thumb_small < 0.2

                is_v_sign = (is_closed_fist and abs(thumb_tip.y - results.multi_hand_landmarks[i].landmark[8].y) > 0.1 
                                            and abs(thumb_tip.y - results.multi_hand_landmarks[i].landmark[12].y) > 0.1)

                is_three_fingers = (is_closed_fist and abs(thumb_tip.y - results.multi_hand_landmarks[i].landmark[8].y) > 0.1 
                                                   and abs(thumb_tip.y - results.multi_hand_landmarks[i].landmark[12].y) > 0.1 
                                                   and abs(thumb_tip.y - results.multi_hand_landmarks[i].landmark[16].y) > 0.1)

                is_pinch = (results.multi_hand_landmarks[i].landmark[8].y < results.multi_hand_landmarks[i].landmark[7].y
                            and results.multi_hand_landmarks[i].landmark[12].y < results.multi_hand_landmarks[i].landmark[11].y
                            and results.multi_hand_landmarks[i].landmark[16].y < results.multi_hand_landmarks[i].landmark[15].y
                            and results.multi_hand_landmarks[i].landmark[20].y < results.multi_hand_landmarks[i].landmark[19].y
                            and abs(results.multi_hand_landmarks[i].landmark[8].x - results.multi_hand_landmarks[i].landmark[20].x) < 0.1)

                sign = ""
                if is_three_fingers:
                    sign = "Three Fingers"
                    if timer_check(0):
                        if paint_type == "spray":
                            paint_type = "brush"
                            msg_change = "Cambio a pincel"
                        elif paint_type == "brush":
                            paint_type = "spray"
                            msg_change = "Cambio a spray"
                        t0 = time.time()
                elif is_v_sign:
                    sign = "V sign"
                    if timer_check(1):
                        color = (255,0,0)
                        msg_change = "Cambio a azul"
                        t0 = time.time()
                elif is_thumb_up:
                    sign = "Ok"
                    if timer_check(2):
                        color = (0,0,255)
                        msg_change = "Cambio a rojo"
                        t0 = time.time()
                elif is_pinch:
                    sign = "Pinch"
                    if timer_check(3):
                        color = (0,0,0)
                        msg_change = "Cambio a borrar"
                        t0 = time.time()
                elif is_closed_fist:
                    sign = "Cerrado"
                    if timer_check(4):
                        color = (0,255,0)
                        msg_change = "Cambio a verde"
                        t0 = time.time()
                if sign != "":
                    print(sign)
                    cv2.putText(frame, sign, [20, 30], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the frame
    if msg_change != "":
        cv2.putText(frame, msg_change, [20, 60], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        if time.time() - t0 > 3:
            msg_change = ""
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