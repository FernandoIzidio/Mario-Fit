import threading
import pydirectinput
import time
               
key_right_pressed = False             
key_left_pressed = False               

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

# Função Andar Pra Frente
def andarFrente(maoDireita_x,cotoveloDireito_x,dist_maoDireita_ombro,dist_entreMaos):
    global key_right_pressed

    if (maoDireita_x > cotoveloDireito_x) and (dist_maoDireita_ombro < 100) and (dist_entreMaos > 100):
        if key_right_pressed is False:
            press_key_in_background('right', 'keydown')
            key_right_pressed = True
    else:
        if key_right_pressed:
            if key_right_pressed:
                press_key_in_background('right', 'keyup')
            key_right_pressed = False

# Função Andar Pra Tras
def andarTras(maoEsquerda_x,cotoveloEsquerdo_x,dist_maoEsquerda_ombro,dist_entreMaos):
    global key_left_pressed

    if (maoEsquerda_x < cotoveloEsquerdo_x) and (dist_maoEsquerda_ombro < 100) and (dist_entreMaos > 100):
        if key_left_pressed is False:
            press_key_in_background('left', 'keydown')
            key_left_pressed = True
    else:
        if key_left_pressed:
            if key_left_pressed:
                press_key_in_background('left', 'keyup')
            key_left_pressed = False