# Mastermind

Mastermind is a code-breaking game for two players. The modern game with pegs was invented in 1970 by Mordecai Meirowitz, an Israeli postmaster and telecommunications expert. The Mastermind game, as known today, consists of a decoding board, code pegs of k colors, and feedback pegs of red and white. There are two players, the code-maker, who chooses a secret pattern of code pegs, and the code-breaker, who guesses the pattern, in a given n rounds. Each round consists of code-breaker making a guess by placing a row of code pegs, and of code-maker providing the feedback of zero to key pegs: a red key for each code peg of correct color and position, and a white key for each peg of correct color but wrong position. After that another guess is made. Guesses and feedbacks continue to alternate until either the code-breaker guesses correctly, or n incorrect guesses have been made. The code-breaker wins if he obtains the solution within n rounds; the code-maker wins otherwise. For this analysis, we assume that duplicate colors are not allowed in a code.

## Dependencies

* [Python 3.7.7](https://www.python.org/downloads/release/python-377/)
* [Pytest 5.4.2](https://pypi.org/project/pytest/)

## Assumptions

* A code is built up of 4 colors
* Code breaker gets a total of 5 chances to guess the code
* Repetition of colors in the code is not allowed
* For every move of code breaker, code maker provides feeback as an array of 4 elements, as follows :
   * If element value = 1 : It means the color and position both are correctly guessed for the element at this position.
   * If element value = 0 : It means an element of this color is present somewhere in the code, but not at this position.
   * If element value = -1 : It means there is no element of this color in the code.
