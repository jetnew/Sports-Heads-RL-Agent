# Sports-Heads-RL-Agent
Reinforcement learning agent to play Sports Heads.

## Challenges faced
### The Environment
* The "environment API" needs to be created from scratch because there was no available API for Sports Heads. I used PyAutoGui to control the agents.
### The Score
* The score can only be interpreted off the screen, so I tried OpenCV, along with PyTesseract to perform OCR to obtain the score off the screen. However, PyTesseract takes ~1 second to detect the score, which is not viable for a game which requires fine movement controls.
* I will try Template Matching (even though tedious) to detect the score from the screen (which thankfully only has a max score of 7 per game).


## References
* [Sports Heads](http://hazardousgames123.weebly.com/sports-heads.html)
