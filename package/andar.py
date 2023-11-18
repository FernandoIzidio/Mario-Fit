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
def frente(maoDireita_x,cotoveloDireito_x,dist_maoDireita_cintura,dist_entreMaos, altura_maoDireita, altura_cintura):
    global key_right_pressed

    if (dist_maoDireita_cintura > 90) and (dist_entreMaos > 100 ) and (altura_maoDireita < (altura_cintura-30)):
        
        if key_right_pressed is False:
            press_key_in_background('right', 'keydown')
            key_right_pressed = True

        if (maoDireita_x < cotoveloDireito_x):
            press_key_in_background('x', 'keydown')      
        else:
            press_key_in_background('x', 'keyup')

                        
    else:
        if key_right_pressed:
            if key_right_pressed:
                press_key_in_background('x', 'keyup')
                press_key_in_background('right', 'keyup')
            key_right_pressed = False

# Função Andar/Correr Pra Tras
def tras(maoEsquerda_x,cotoveloEsquerdo_x,dist_maoEsquerda_cintura,dist_entreMaos,altura_maoEsquerda,altura_cintura):
    global key_left_pressed
    
    if (dist_maoEsquerda_cintura > 90) and (dist_entreMaos > 100) and (altura_maoEsquerda < (altura_cintura-30)):

        if key_left_pressed is False:
            press_key_in_background('left', 'keydown')
            key_left_pressed = True

        if (maoEsquerda_x > cotoveloEsquerdo_x):
            press_key_in_background('x', 'keydown')      
        else:
            press_key_in_background('x', 'keyup')

    else:
        if key_left_pressed:
            if key_left_pressed:
                press_key_in_background('x', 'keyup')
                press_key_in_background('left', 'keyup')
            key_left_pressed = False