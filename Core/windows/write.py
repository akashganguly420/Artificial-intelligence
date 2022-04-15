from  ..module.ai import *


def write():
    speak('write mode for speak to write on notepad')
    speak('say back for go back')

    write = statement = takeCommand().lower()
    mode = 'open'
    if write == mode:
        os.system('start notepad')
        while True:
            say = statement = takeCommand().lower()
            pyautogui.press('space')
            pyautogui.write(say)
    
    else:
        pyautogui.write(' ')