from  ..module.module import *

def akash():
    pyautogui.press('win')
    time.sleep(2)
    pyautogui.write('skype')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'shift', 'k')