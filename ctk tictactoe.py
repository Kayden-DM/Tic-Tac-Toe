import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

current_player = "X"
game_over = False


def on_click(row, col):
    global current_player, game_over
    if game_over:
        return

    btn = board[(row, col)]
    if btn.cget("text") != "":
        return

    btn.configure(text=current_player)

    winner = check_winner()
    if winner:
        turn_label.configure(text=f"{winner} wins!")
        game_over = True
        return
    if all(board[(r, c)].cget("text") != "" for r in range(3) for c in range(3)):
        turn_label.configure(text="Draw!")
        game_over = True
        return

    current_player = "O" if current_player == "X" else "X"
    turn_label.configure(text=f"Player {current_player}'s turn")


def check_winner():
    lines = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)],
    ]
    for line in lines:
        a, b, c = line
        if (board[a].cget("text") == board[b].cget("text") == board[c].cget("text")
                and board[a].cget("text") != ""):
            return board[a].cget("text")
    return None


root = ctk.CTk()
root.title("Tic Tac Toe")

turn_label = ctk.CTkLabel(root, text="Turn: X", font=("Arial", 16))
turn_label.grid(row=3, column=0, columnspan=3, pady=10)

board = {}
for row in range(3):
    for col in range(3):
        btn = ctk.CTkButton(root, text="", font=("Arial", 30),
                            width=80, height=80,
                            command=lambda r=row, c=col: on_click(r, c))
        btn.grid(row=row, column=col, padx=3, pady=3)
        board[(row, col)] = btn

root.mainloop()