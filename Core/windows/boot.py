from  ..module.module import *




def boot():
    os.system("start rufus.exe")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write("F:\windows_10\window_10", interval=0.15)
    pyautogui.press("enter", interval=0.25)
    pyautogui.write("windows 10 final.iso", interval=0.10)
    pyautogui.press("enter", interval=0.10)