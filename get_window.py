from PIL import ImageGrab
import numpy as np
import cv2


def get_frame(dims=(200, 200), show_state=False):
    """Get the state of the game."""
    # bbox = x, y, width, height
    img = ImageGrab.grab(bbox=(0,190,958,865))
    img_np = np.array(img) #this is the array obtained from conversion
    img_np = cv2.resize(img_np, dims, interpolation=cv2.INTER_CUBIC)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    # Display state
    if show_state:
        cv2.imshow("test", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return frame
