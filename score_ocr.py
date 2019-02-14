import pytesseract
from PIL import ImageGrab
import numpy as np
import cv2
import sys


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def get_img(player, dims=(200,200)):
    """Given player number, return score image from screen."""
    if player == 0:
        boundary = (0, 300, 50, 350)
    else:
        boundary = (920, 300, 955, 350)
    # bbox= x,y,width,height *starts top-left)
    img = ImageGrab.grab(bbox=boundary)
    img = np.array(img) #this is the array obtained from conversion
    img = cv2.resize(img, dims, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("test", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img


def get_scores():
    """Return scores for players 1 and 2."""
    img0 = get_img(player=0)
    img1 = get_img(player=1)
    config = ('--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    text0 = pytesseract.image_to_string(img0, lang="eng", config=config)
    text1 = pytesseract.image_to_string(img1, lang="eng", config=config)

    return int(text0), int(text1)
