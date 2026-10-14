This README is made with AI

❌⭕ Python Tic Tac Toe
A modern desktop Tic Tac Toe game built with Python and CustomTkinter. Two players take turns clicking a 3×3 grid to place their mark (X or O). The game automatically detects wins, draws, and whose turn it is. It's a great beginner project for learning about modern GUI programming, event handling, grid layouts, and game state management in Python.

📖 Python Tic Tac Toe
The Python Tic Tac Toe game is a graphical two-player game built with CustomTkinter — a modern, themeable wrapper around Tkinter. The app launches in dark mode with a blue color theme, giving it a sleek, contemporary look.

The board is a 3×3 grid of buttons, and players alternate placing X and O by clicking an empty square. The game checks for a winner after every move by scanning all eight possible winning lines — three rows, three columns, and two diagonals. If a player gets three in a row, the game announces the winner and locks the board. If all nine squares are filled with no winner, the game declares a draw.

A label beneath the grid shows whose turn it is, and the game stops accepting clicks once it's over. The interface is built with CustomTkinter widgets, so the only external dependency is the customtkinter library.

This project is a polished, modern take on the classic Tic Tac Toe game, ideal for anyone wanting to build sleek-looking Python GUIs.

✨ Features
Dark mode by default – Uses CustomTkinter's built-in appearance mode.

Blue color theme – Applied globally for a modern, cohesive look.

3×3 clickable grid – Nine buttons arranged in a classic Tic Tac Toe layout.

Two-player turn system – Alternates between X and O automatically.

Turn indicator label – Shows whose turn it is at all times.

Win detection – Scans all eight winning lines (rows, columns, diagonals).

Draw detection – Declares a draw when all squares are filled with no winner.

Prevents overwriting moves – Clicking an occupied square does nothing.

Locks the board after game over – No further moves are accepted once a winner or draw is declared.

Winning message – Displays "{X/O} wins!" when a player completes a line.

Clean grid layout – Uses CustomTkinter's .grid() for precise positioning.

Global game state – Tracks the current player and whether the game has ended.

🛠️ What It Uses
Language & Library
Python 3

CustomTkinter – A modern, themeable wrapper for Tkinter.

Install with: pip install customtkinter

Key Variables
Variable	Purpose
current_player	Tracks whose turn it is ("X" or "O").
game_over	Boolean flag that stops the game once it has ended.
board	A dictionary mapping (row, col) tuples to their corresponding button widgets.
Key Functions
Function	Purpose
on_click(row, col)	Handles a player's move — places their mark, checks for a winner or draw, and switches turns.
check_winner()	Scans all eight winning lines and returns "X", "O", or None.
CustomTkinter Widgets & Methods Used
ctk.set_appearance_mode("dark") – Sets the global theme to dark mode.

ctk.set_default_color_theme("blue") – Applies the blue color scheme.

ctk.CTk() – Main application window.

ctk.CTkLabel – Displays the current turn or the result.

ctk.CTkButton – The nine clickable squares on the board.

.grid() – Geometry manager for laying out widgets in a grid.

.configure() – Dynamically updates button text and label text.

.cget("text") – Reads the current text of a widget.

root.mainloop() – Starts the CustomTkinter event loop.

Python Concepts Demonstrated
Global variables – Sharing current_player and game_over across functions.

Dictionaries – Mapping coordinate tuples to button widgets.

Lambda functions – Capturing row and col for each button's command.

Nested loops – Building the 3×3 grid programmatically.

Conditional logic – Checking for wins, draws, and occupied squares.

Chained comparisons – board[a].cget("text") == board[b].cget("text") == board[c].cget("text").

List of tuples – Defining all eight winning lines.

F-strings – Formatted output for turn and win messages.

all() with generator expression – Checking whether every square is filled.

Event-driven programming – Buttons trigger functions when clicked.

Built-in Functions Used
range() – Iterating over the 3×3 grid coordinates.

all() – Testing whether every square on the board is occupied.

f"{...}" – String formatting for labels.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
tic_tac_toe.py
Then install the required library:

bash
pip install customtkinter
▶️ How to Run
Make sure you have Python 3 installed (python.org).

Install CustomTkinter:

bash
pip install customtkinter
Save the code as tic_tac_toe.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python tic_tac_toe.py
The game window will open. Player X goes first — click any empty square to place your mark. The label below the grid shows whose turn it is, and the result is announced when the game ends.

🐍 Made with Python
This project is written in Python 3 and uses CustomTkinter to give the interface a modern, polished look. It's a clean, approachable example of how a classic two-player game can be built with a modern-themed GUI library.

Whether you're a beginner exploring GUI development or someone who just wants a quick game of Tic Tac Toe, this project is a great starting point.

💡 Possible Future Improvements
Reset button – Add a button to restart the game without closing and reopening the app.

Score tracking – Keep a running tally of wins for X, wins for O, and draws.

Play against the computer – Add a simple AI opponent (random, or minimax for unbeatable play).

Highlight the winning line – Change the background color of the three winning buttons.

Custom player names – Let players enter their names instead of "X" and "O".

Larger boards – Support 4×4 or 5×5 grids with adjustable win conditions.

Sound effects – Play a click sound on each move and a victory sound on a win.

Theme switcher – Add a toggle between light and dark modes at runtime.

Animations – Add subtle fade-ins or scaling effects when a mark is placed.

📄 License
This project is free to use, modify, and distribute for personal or educational purposes.

