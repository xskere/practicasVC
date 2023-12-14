import cv2
import mediapipe as mp

# Initialize Mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe hands
    results = hands.process(rgb_frame)
    
    # Check if hands are detected
    if results.multi_hand_landmarks:
        for i in range(len(results.multi_hand_landmarks)):
            mp.solutions.drawing_utils.draw_landmarks(frame, results.multi_hand_landmarks[i], mp_hands.HAND_CONNECTIONS)

            hand_label = "Right" if results.multi_handedness[i].classification[0].label == "Left" else "Left"

            cv2.putText(frame, hand_label, 
                        (int(results.multi_hand_landmarks[i].landmark[0].x * frame.shape[1]), int(results.multi_hand_landmarks[i].landmark[0].y * frame.shape[0])),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Hand Tracking Demo', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
