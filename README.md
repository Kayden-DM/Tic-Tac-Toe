## Tic Tac Toe
A desktop tic tac toe game built with CustomTkinter. It uses a 3x3 grid of buttons and alternates turns between X and O, checking for a winner or draw after every move.

## Features
3x3 Grid — Creates nine buttons arranged with .grid() and stores them in a dictionary keyed by row and column.

Alternating Turns — Switches between X and O after each valid move and updates the turn label.

Occupied Cell Check — Ignores clicks on buttons that already contain a mark.

Win Detection — Checks all eight winning lines (rows, columns, diagonals) after every move and announces the winner.

Draw Detection — Ends the game with "Draw!" when every cell is filled and no one has won.

Game Over Lock — Ignores further clicks once the game has ended.

Dark Mode UI — CustomTkinter dark appearance with a blue accent theme.

## Technologies Used
text
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `customtkinter` | Desktop GUI |
| `CTkButton` | Each cell of the grid |
| `.grid()` | Positions the 3x3 board |
| `lambda` | Passes row and column to each button |
| `dict` (`board`) | Maps `(row, col)` to each button |
| `cget("text")` | Reads the current mark in a cell |
| `global` | Updates `current_player` and `game_over` |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Install CustomTkinter by running pip install customtkinter.

Save the code as tic_tac_toe.py.

Open a terminal in the folder containing the file.

Run python tic_tac_toe.py.

Click any empty cell to place your mark; X and O alternate turns until someone wins or the board fills up.

## Improvements
Add a restart button — once the game ends there is no way to play again without closing the program; a reset function that clears the board and sets current_player back to "X" would fix that.

Store marks in a list — reading state with cget("text") works but is roundabout; keeping a separate 2D list of "X", "O", or "" would make check_winner() simpler and decouple game logic from the UI.

