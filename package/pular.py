import cv2
import mediapipe as mp
import math

global pulo_confirmado
global agachar_confirmado
pulo_confirmado = 0
agachar_confirmado = 0

def pular(img,width,nose_y,dist_cabeca_teto,dist_mao_nariz,right_eye_y,right_shoulder_y):
    global pulo_confirmado
    global agachar_confirmado

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