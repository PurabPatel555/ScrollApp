from pynput.mouse import Listener
from pynput.keyboard import Key, Controller
import pyautogui

keyboard = Controller()

def on_scroll(x, y, dx, dy):
    if(dy>0):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    else:
        keyboard.press(Key.left)
        keyboard.release(Key.left)
with Listener(on_scroll=on_scroll) as listener:
    listener.join()
    	
