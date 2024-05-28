import cv2
import time

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

start_time = time.time()
frames = 0
fps=0
scritta = ''
    
while True:
    esito, immagine = webcam.read()

    immagine = cv2.flip(immagine,1)

    frame_rgb = cv2.cvtColor(immagine, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                immagine, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmark_point = hand_landmarks.landmark[8]
            height, width, _ = immagine.shape
            cx, cy = int(landmark_point.x * width), int(landmark_point.y * height)
            cv2.circle(immagine, (cx, cy), 10, (0, 255, 0), -1)

            landmark_point = hand_landmarks.landmark[4]
            height, width, _ = immagine.shape
            cx, cy = int(landmark_point.x * width), int(landmark_point.y * height)
            cv2.circle(immagine, (cx, cy), 10, (0, 255, 0), -1)

            landmark_point = hand_landmarks.landmark[0]
            height, width, _ = immagine.shape
            cx, cy = int(landmark_point.x * width), int(landmark_point.y * height)
            cv2.circle(immagine, (cx, cy), 10, (255, 255, 255), -1)

    results = pose.process(frame_rgb)

    # Disegna le pose del corpo sul frame
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            immagine, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)


    
    frames += 1
    if time.time() - start_time >= 1:
        # Calcola i frame per secondo
        fps = frames / (time.time() - start_time)
        
        # Resetta il contatore dei frame e il tempo di inizio
        frames = 0
        start_time = time.time()

        
    scritta = f'FPS: {fps} sono le {time.time()}'
    cv2.putText(
            immagine,
            scritta,
            (50,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            3)

    cv2.imshow('in diretta', immagine)

    pippo = cv2.waitKey(1)
    if pippo == 27: # tasto ESC
        break

webcam.release()
cv2.destroyAllWindows()