from get_window import get_frame
import pyautogui as pag
import time
import threading
import random

STEP = 0.3  # seconds

# Action space
action_space = ['l', 'r', 'j', 'k']

def _move_direction(duration, key):
    """Move in given direction and duration. Smoother than time.sleep()."""
    def _key_up(key):
        """Key up. Used with threading.Timer()"""
        pag.keyUp(key)

    pag.keyDown(key)
    # time.sleep(duration)
    # pag.keyUp(key)
    timer = threading.Timer(duration, _key_up, [key])
    timer.start()


def move(key, steps=1):
    """Move in direction, given step."""
    directions = {
        'l': 'left',
        'r': 'right',
        'j': 'up',
        'k': 'p'
    }
    for s in range(steps):
        _move_direction(STEP, directions[key])


# # Testing
# time.sleep(3)

# move('l')
# move('k')
# move('j')
# move('r')



# for i in range(3*10):
#     action = action_space[random.randint(0, 3)]
#     print(action)
#     move(action)
# move('l')
# move('k')
# move('j')
# move('k')
