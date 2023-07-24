# Tic-Tac-Toe AI - Play Against the Optimal AI!

Welcome to the Tic-Tac-Toe AI project! In this project, we've implemented a powerful AI that plays Tic-Tac-Toe optimally using the Minimax algorithm. The AI will never lose a game if it plays optimally, and you can test your skills by playing against it!

## Project Files

There are two main files in this project:
1. `tictactoe.py`: Contains all the logic for playing the game and making optimal moves. All required functions have been implemented for a flawless gaming experience.
2. `runner.py`: Implements the graphical interface for the game.
3.  pip install -r requirements.txt and Run `python runner.py` to play against the AI!

## Functions

The following functions have been successfully implemented in `tictactoe.py`:

1. `player`: Determines which player's turn it is (either X or O).
2. `actions`: Returns a set of all possible actions that can be taken on the current board.
3. `result`: Returns a new board state after making a valid move.
4. `winner`: Determines the winner of the game (either X or O), if there is one.
5. `terminal`: Checks if the game is over or still in progress.
6. `utility`: Returns the utility of a terminal board (1 if X wins, -1 if O wins, 0 for a tie).
7. `minimax`: Finds the optimal move for the player to move on the current board.

## How to Play

1. Clone this repository to your local machine using `git clone`.

2. Navigate to the project directory.

3. Run the graphical interface by executing `python runner.py`.

4. Play against the AI and test your strategic skills! The AI will play optimally, so you'll need to play strategically to beat it!

## Notes

- If you play optimally as well, the game will end in a tie.
- The AI will never lose if it plays optimally.


## License

This project is open-source and released under the [MIT License](https://opensource.org/licenses/MIT).

Challenge yourself against our Tic-Tac-Toe AI and enjoy the strategic gameplay! Can you outsmart the AI? Let the games begin! 🎮✨
