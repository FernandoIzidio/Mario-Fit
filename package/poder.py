import threading
import pydirectinput
import time
               
usou_poder = False       

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

# Soltar poder
def soltarPoder(dist_entreMaos):
    global usou_poder

    if dist_entreMaos < 20:
        if usou_poder is False:
            press_key_in_background('d', 'press')
            usou_poder = True
    else:
        usou_poder = False