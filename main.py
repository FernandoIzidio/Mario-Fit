import cv2
import mediapipe as mp
import math
from os import system
VIDEO_PATH = 0

video = cv2.VideoCapture(VIDEO_PATH)
pose = mp.solutions.pose
mp_pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

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
        left_index_y = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y * height)
        left_index_x = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x * width)
        left_shoulder_y = int(points.landmark[pose.PoseLandmark.LEFT_SHOULDER].y * height)
        left_shoulder_x = int(points.landmark[pose.PoseLandmark.LEFT_SHOULDER].x * width)
        nose_y = int(points.landmark[pose.PoseLandmark.NOSE].y * height)
        nose_x = int(points.landmark[pose.PoseLandmark.NOSE].x * width)

        dist_maoDireita_ombro = int(
            math.hypot(right_index_x - right_shoulder_x, right_index_y - right_shoulder_y))

        print(f"Hypot: {dist_maoDireita_ombro}")


        # Desenha uma linha na altura do nariz
        cv2.line(img, (0, nose_y), (640, nose_y), (0, 255, 0), 1)

        # Desenha uma linha vertical sobre o elbow
        cv2.line(img, (right_elbow_x, 0), (right_elbow_x, 480), (0, 255, 0), 1)

    cv2.imshow("Image", img)
    cv2.waitKey(10)
