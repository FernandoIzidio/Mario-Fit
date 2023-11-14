import threading
import pydirectinput
import time

key_pressed = False                    
key_run_right = False
key_run_left = False         

# CONFIG MULTI THREADING
def press_key_in_background(key, command):
    thread = threading.Thread(target=press_key, args=(key, command,))
    thread.start()

def press_key(key, command):
    if command == 'press':
        pydirectinput.keyDown(key)
        time.sleep(0.8)
        pydirectinput.keyUp(key)
    elif command == 'keydown':
        pydirectinput.keyDown(key)
    elif command == 'keyup':
        pydirectinput.keyUp(key)

def correrFrente(maoDireita_x,cotoveloDireito_x,dist_maoDireita_cintura):
    global key_pressed
    global key_run_right

    if maoDireita_x < cotoveloDireito_x and dist_maoDireita_cintura > 110:
        if key_run_right is False:
            press_key_in_background('x', 'keydown')
            press_key_in_background('right', 'keydown')
            key_run_right = True
    else:
        if key_run_right:
            if key_run_right:
                press_key_in_background('x', 'keyup')
                press_key_in_background('right', 'keyup')
            key_run_right = False

def correrTras(maoEsquerda_x,cotoveloEsquerdo_x,dist_maoEsquerda_cintura):
    global key_pressed
    global key_run_left

    if maoEsquerda_x > cotoveloEsquerdo_x and dist_maoEsquerda_cintura > 110:
        if key_run_left is False:
            press_key_in_background('x', 'keydown')
            press_key_in_background('left', 'keydown')
            key_run_left = True
    else:
        if key_run_left:
            if key_run_left:
                press_key_in_background('x', 'keyup')
                press_key_in_background('left', 'keyup')
            key_run_left = False