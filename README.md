Tic Tac Toe
A GUI Python game built with CustomTkinter where two players take turns placing X and O on a 3×3 grid.

Concepts Used
Dictionaries — board maps (row, col) tuples to their button widgets for easy lookup.

Lambda Closures — lambda r=row, c=col: on_click(r, c) binds each button to its own coordinates.

Grid Layout — grid() positions the 3×3 buttons plus a status label across three columns.

Features
Two-Player Turns — alternates between X and O, updating a label each turn.

Win Detection — checks all 8 winning lines (rows, columns, diagonals) after every move.

Draw Handling — detects a full board with no winner and ends the game.

Improvements
Add a Reset Button — once the game ends there's no way to play again without restarting the app.

Cache Button Text — cget("text") is called repeatedly in check_winner() and the draw check; storing moves in a plain list/dict would be faster and cleaner.

Refactor Turn Label — the initial label says "Turn: X" but later shows "Player X's turn"; standardize the wording, and consider showing whose turn it is before the first move consistently.
