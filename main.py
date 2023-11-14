import cv2
import mediapipe as mp
import math
from os import system
VIDEO_PATH = 'Video4.mp4'

video = cv2.VideoCapture(VIDEO_PATH)
pose = mp.solutions.pose
mp_pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

pulo_confirmado = 0
agachar_confirmado = 0

while True:
    success, img = video.read()
    video_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = mp_pose.process(video_rgb)
    points = results.pose_landmarks
    mp_draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    height, width, _ = img.shape

    if points:
        right_index_y = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y * height)
        right_index_x = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x * width)
        right_shoulder_y = int(points.landmark[pose.PoseLandmark.RIGHT_SHOULDER].y * height)
        right_shoulder_x = int(points.landmark[pose.PoseLandmark.RIGHT_SHOULDER].x * width)
        right_elbow_x = int(points.landmark[pose.PoseLandmark.RIGHT_ELBOW].x * width)
        right_elbow_y = int(points.landmark[pose.PoseLandmark.RIGHT_ELBOW].y * height)
        left_elbow_x = int(points.landmark[pose.PoseLandmark.LEFT_ELBOW].x * width)
        left_elbow_y = int(points.landmark[pose.PoseLandmark.LEFT_ELBOW].y * height)
        left_index_y = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y * height)
        left_index_x = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x * width)
        left_shoulder_y = int(points.landmark[pose.PoseLandmark.LEFT_SHOULDER].y * height)
        left_shoulder_x = int(points.landmark[pose.PoseLandmark.LEFT_SHOULDER].x * width)
        nose_y = int(points.landmark[pose.PoseLandmark.NOSE].y * height)
        nose_x = int(points.landmark[pose.PoseLandmark.NOSE].x * width)
        right_eye_x = int(points.landmark[pose.PoseLandmark.RIGHT_EYE].x * width)
        right_eye_y = int(points.landmark[pose.PoseLandmark.RIGHT_EYE].y * height)


        # Pegando as distancias
        dist_maoDireita_ombro = int(
            math.hypot(right_index_x - right_shoulder_x, right_index_y - right_shoulder_y))

        dist_maoEsquerda_ombro = int(
            math.hypot(left_index_x-left_shoulder_x, left_index_y-left_shoulder_y))
        
        dist_entreMaos = int(
            math.hypot(right_index_x-left_index_x, right_index_y-left_index_y))

        dist_cabeca_teto = int(
            math.hypot(right_eye_y,0))

        dist_mao_nariz = int(
            math.hypot(right_index_x-nose_x, right_index_y-nose_y))
 
        
        # Andar 
        if (right_index_x > right_elbow_x) and (dist_maoDireita_ombro < 100) and (dist_entreMaos > 100):
            print("Andando Pra Frente")

        if (left_index_x < left_elbow_x) and (dist_maoEsquerda_ombro < 100) and (dist_entreMaos > 100):
            print("Andando Pra Trás")


        # Soltar poder
        if dist_entreMaos < 20:
            print("Soltar Poder")


        # Desenha uma linha na altura do nariz
        cv2.line(img, (0, nose_y), (width, nose_y), (0, 255, 0), 1)

        # Ajuste do pulo / agachameto
        ajuste = 60

        if (dist_cabeca_teto>=76):  
            ajuste = 30
        elif (dist_cabeca_teto <76) and (dist_cabeca_teto >50):
            ajuste = 40
        elif dist_cabeca_teto <=50:
            ajuste = 50
        
        # Confirmando a posição do pulo
        if (dist_mao_nariz < 20):
            pulo_confirmado = int(right_eye_y*(1-ajuste/100))
            agachar_confirmado = int(right_shoulder_y*(1-0/100))
            print("Posição do pulo alterada")

        cv2.line(img, (0, pulo_confirmado), (width, pulo_confirmado), (0, 0, 255), 1)
        cv2.line(img, (0,agachar_confirmado), (width,agachar_confirmado), (0, 0, 255), 1)

        # Pular
        if pulo_confirmado != 0:
            if nose_y<pulo_confirmado:
                print("Pulo")
            
            # Agachar
            if nose_y>agachar_confirmado:
                print("Agachar")


        # Desenha uma linha vertical sobre os cotovelos
        cv2.line(img, (right_elbow_x, 0), (right_elbow_x, height), (0, 255, 0), 1)
        cv2.line(img, (left_elbow_x, 0), (left_elbow_x, height), (0, 255, 0), 1)


    cv2.imshow("Image", img)

    # Aperte ESC para fechar o app
    if cv2.waitKey(10) == 27:
        break
