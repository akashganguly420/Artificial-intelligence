
from  ..module.module import *


def scan():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                            cv2.COLOR_RGB2BGR)

    cv2.imwrite("scan.png", image)
    print('scr taken')
    time.sleep(0.5)

    img = cv2.imread('scan.png')
    config = '-l eng --oem 1 --psm 3'
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(img, config=config)

    # print text
    text = text.split('\n')
    print(text)
