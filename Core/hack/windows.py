
from  ..module.module import *

def windows():
    pyautogui.hotkey('ctrl', 'alt', 'z')
    time.sleep(5)
    
    pyautogui.write("windows", interval=0.25)
    time.sleep(1)
    pyautogui.press("enter", interval=0.25)
    
    