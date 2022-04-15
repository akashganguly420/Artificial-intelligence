import pyautogui
import time

def android():
    pyautogui.hotkey('ctrl', 'alt', 'z')
    time.sleep(5)
    
    pyautogui.write("android", interval=0.25)
    time.sleep(1)
    pyautogui.press("enter", interval=0.25)
    
