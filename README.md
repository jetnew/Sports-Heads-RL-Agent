# Sports-Heads-RL-Agent
Reinforcement learning agent to play Sports Heads.

![bighead_small](https://user-images.githubusercontent.com/27071473/52899855-dfb8f800-3229-11e9-9a4d-e8b499c53f03.png)

## Experimental settings
* I used a DQN with experience replay (not prioritised), nothing special.
* The ~950x650 screen is shrunk into 200x200 before feeding into 2-hidden-layer Keras model with ReLU activation.
* The agent uses an epsilon-greedy method of selecting its action, with epsilon=1.0 and decay=0.9995 per experience replay.

## Challenges faced
### The Environment
* 15/2/2019: The "environment API" needs to be created from scratch because there was no available API for Sports Heads. I used PyAutoGui to control the agents.
### The Score
* 16/2/2019: The score can only be interpreted off the screen, so I tried OpenCV, along with PyTesseract to perform OCR to obtain the score off the screen. However, PyTesseract takes ~1 second to detect the score, which is not viable for a game which requires fine movement controls, and for a single-thread agent like DQN. Template matching works, at about ~0.2 seconds, enabling for finer movements for the agent.
* 17/2/2019: After 6 hours of training of self-play between 2 agents, both agents seem to learn to stay to the goal in hopes of the other opponent kicking the ball and getting an own-goal. A minimum epsilon of 0 seems to converge the agents to this local minima. I will try a minimum epsilon of 0.2 to allow the agent to explore more.

## References
* [Sports Heads](http://hazardousgames123.weebly.com/sports-heads.html)
* [Template Matching](https://www.geeksforgeeks.org/template-matching-using-opencv-in-python/)
