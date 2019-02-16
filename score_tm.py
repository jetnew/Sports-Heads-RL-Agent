# Python program to illustrate  
# template matching 
import cv2
import numpy as np
from PIL import ImageGrab, Image
from get_window import get_frame


def search_score(number_img, game_img):
    """Search for a given score image."""
    # Read the main image
    img_rgb = cv2.imread(game_img)

    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # Read the template
    template = cv2.imread(number_img, 0)

    # Store width and heigth of template in w and h
    w, h = template.shape[::-1]

    # Perform match operations.
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    # Specify a threshold
    threshold = 0.9

    # Store the coordinates of matched area in a numpy array
    loc = np.where(res >= threshold)

    return loc


def get_score():
    game_img = get_frame(dims=(958, 675), get_score=True)
    im = Image.fromarray(game_img)
    im.save('gameimg.png')

    p1, p2 = 0, 0
    score_occurence = []
    for i in range(8):
        loc = search_score('score_img/'+str(i)+'.png', 'gameimg.png')
        if len(loc[0]) != 0 and len(loc[1]) != 0:
            # Left player
            if loc[1][0] < 10:
                p2 = i
            # Right player
            if loc[1][0] > 900:
                p1 = i
        score_occurence.append(loc)

    return p1, p2



"""
# Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
# Show the final image with the matched area. 
cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""