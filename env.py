from score_ocr import get_scores
import pyautogui as pag
import time
from get_window import get_frame
from movement import move, action_space
from score_ocr import get_scores

# p1_score, p2_score = get_scores()


class FootballHeadEnv:
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0
        self.start_new_game()
        self.action_space = 4
        self.observation_space = 200*200

    def reset(self):
        """Reset a game while in game."""
        self.go_to_menu()
        self.start_new_game()
        return get_frame()

    def step(self, action):
        """Take an action."""
        move(action_space[action])
        state = get_frame()
        new_p1_score, new_p2_score = get_scores()

        # If: Player 1 scores
        if new_p1_score > self.p1_score:
            reward = 100
            self.p1_score = new_p1_score
        # If: Player 2 scores
        elif new_p2_score > self.p2_score:
            reward = -100
            self.p2_score = new_p2_score
        else:
            reward = -1

        # If: Game ends
        if self.p1_score == 7 or self.p2_score == 7:
            done = True
        else: done = False

        return state, reward, done, None

    @staticmethod
    def start_new_game():
        """Start new game from Menu page."""
        pag.click(x=480, y=600)  # click 'New Game'
        for _ in range(18):
            pag.click(x=275, y=685)  # click 'Change Pitch <-'
        for _ in range(6):
            pag.click(x=450, y=685)  # click 'Change Pitch ->'
        pag.click(x=480, y=770)  # click 'Start'
        pag.keyDown('space')  # start game
        time.sleep(0.2)
        pag.keyUp('space')

    @staticmethod
    def go_to_menu():
        """Go to Menu while in game."""
        time.sleep(0.2)
        pag.click(x=920, y=850)  # click 'Menu'
        time.sleep(4)


env = FootballHeadEnv()
print("resetting")
print(env.reset())
