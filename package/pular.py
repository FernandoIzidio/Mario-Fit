import cv2
import mediapipe as mp
import math
import threading
import pydirectinput
import time

pulo_confirmado = 0
agachar_confirmado = 0
is_jumping = False                      
is_squatting = False                   
key_pressed = False                     


# CONFIG MULTI THREADING
def press_key_in_background(key, command):
    thread = threading.Thread(target=press_key, args=(key, command,))
    thread.start()

# CONFIG INPUT 
def press_key(key, command):
    if command == 'press':
        pydirectinput.keyDown(key)
        time.sleep(0.8)
        pydirectinput.keyUp(key)
    elif command == 'keydown':
        pydirectinput.keyDown(key)
    elif command == 'keyup':
        pydirectinput.keyUp(key)

# Função Pular e Agachar
def pularAgachar(img,width,nose_y,dist_cabeca_teto,dist_mao_nariz,right_eye_y,right_shoulder_y):
    global pulo_confirmado
    global agachar_confirmado
    global is_jumping
    global key_pressed
    global is_squatting

    # Ajuste do pulo / agachameto
    ajuste = 60

    if (dist_cabeca_teto>=76) and (dist_cabeca_teto<=130):  
        ajuste = 30
    elif (dist_cabeca_teto >130):
        ajuste = 14
    elif (dist_cabeca_teto <76) and (dist_cabeca_teto >50):
        ajuste = 40
    elif dist_cabeca_teto <=50:
        ajuste = 50
    
    # Confirmando a posição do pulo
    if (dist_mao_nariz < 40):
        pulo_confirmado = int(right_eye_y*(1-ajuste/100))
        agachar_confirmado = int(right_shoulder_y*(1-0/100))
        print("Posição do pulo alterada")

    cv2.line(img, (0, pulo_confirmado), (width, pulo_confirmado), (0, 0, 255), 1)
    cv2.line(img, (0,agachar_confirmado), (width,agachar_confirmado), (0, 0, 255), 1)

    # Pular
    if pulo_confirmado != 0:
        if nose_y<pulo_confirmado:
            if is_jumping is False:
                press_key_in_background('c', 'press')
                is_jumping = True
        else:
            is_jumping = False
        
        # Agachar
        if nose_y>agachar_confirmado:
            if is_squatting is False:
                press_key_in_background('down', 'keydown')
                is_squatting = True
                key_pressed = True
        else:
            if key_pressed:
                press_key_in_background('down', 'keyup')
                key_pressed = False
            is_squatting = False