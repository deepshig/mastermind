# Mastermind

Mastermind is a code-breaking game for two players. The modern game with pegs was invented in 1970 by Mordecai Meirowitz, an Israeli postmaster and telecommunications expert. The Mastermind game, as known today, consists of a decoding board, code pegs of k colors, and feedback pegs of red and white. There are two players, the code-maker, who chooses a secret pattern of code pegs, and the code-breaker, who guesses the pattern, in a given n rounds. Each round consists of code-breaker making a guess by placing a row of code pegs, and of code-maker providing the feedback of zero to key pegs: a red key for each code peg of correct color and position, and a white key for each peg of correct color but wrong position. After that another guess is made. Guesses and feedbacks continue to alternate until either the code-breaker guesses correctly, or n incorrect guesses have been made. The code-breaker wins if he obtains the solution within n rounds; the code-maker wins otherwise. For this analysis, we assume that duplicate colors are not allowed in a code.

This project is an analysis in terms of multi agent systems. It identifies the code breaker and the code maker as two agents, and keeps a track of their knowledge at every state in the game.

## Dependencies

* [Python 3.7.7](https://www.python.org/downloads/release/python-377/)
* [Pytest 5.4.2](https://pypi.org/project/pytest/)
* [import_from_github](https://github.com/nvbn/import_from_github_com)
* [ML Solver](https://github.com/erohkohl/mlsolver)

## Strategies

The project analyses 3 different strategies for code-breaker.
* Mathematician
* Logician
* Random

More details about the project can be found in the [documentation](documentation.md)

## Assumptions

* A code is built up of 4 colors
* Code breaker gets a total of 3 chances to guess the code
* Repetition of colors in the code is not allowed
* For every move of code breaker, code maker provides feeback as an array of 4 elements, as follows :
   * If element value = 1 : It means the color and position both are correctly guessed for the element at this position.
   * If element value = 0 : It means an element of this color is present somewhere in the code, but not at this position.
   * If element value = -1 : It means there is no element of this color in the code.
* Default game runs with `Mathematician Code-breaker` strategy.
* Strategy Analyser simulation runs 20 games for each strategy, with the same code in a game across the 3 strategies.
* Kripke Model about the state of the game is maintained in the KnowledgeManager.
* Agent knowledge is modelled as follows :
   * A knowledge proposition known with surety is expressed as `<position>:<color>`.
   * A negation known with surety is expressed as `~(<position>:<color>)`.
   * An unsure knowledge proposition which may or may not hold is expressed as `*(<position>:<color>)`.

## Implementation

We have implemented the game in python.

We have two classes, one each for code-maker and the code-breaker. Although, code-breaker is available in three variants according to the three strategies decribed above. When a game starts, code-breaker class initialises by randomly generating a code. Code-breaker attempts to guess this code within 3 moves. Code-maker analyses each of these moves and generates a feedback, which is passed onto the code-breaker.

We use a knowledge-manager class to represent the Kripke Model (possible worlds and their relations) according to the current state of the game. There is also an agent-knowledge class which maintains the commong knowledge and individual knowledge propositions for both agents at every state of the game.

The game class takes the responsibility to bring all these features together, and conduct a game. In each move, code-breaker makes a guess, and code-maker provides feedback. The knowledge base in Kripke model and agent knowledge is updated accordingly. We have three strategies in place for code-breaker, however the game by default runs for mathematician code-breaker.

Strategy analyser class provides an interface to run simulation games to compare the three strategies available.

We have written unit tests for most of the logic in the code. These ensure that no unintentional changes can take place in the code. Thus, it is recommended to run the tests everytime before starting off with the project.

## Running the program

* To run the code : `python game.py`
* To run strategy analyser : `python strategy_analyser.py`
* To run the tests : `cd tests && py.test && cd ../`
