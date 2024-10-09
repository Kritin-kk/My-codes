import tkinter as tk
from tkinter import messagebox

current_player = "X"
moves = 0
board = [["" for _ in range(3)] for _ in range(3)]

def on_button_click(row, col):
    global current_player, moves

    if board[row][col] == "":
        moves += 1
        board[row][col] = current_player
        button = buttons[row][col]
        button.config(text=current_player)
        button.config(state="disabled")
        check_game_result(row, col)

        current_player = "O" if current_player == "X" else "X"

def check_game_result(row, col):
    global moves

    # Check row
    if board[row][0] == board[row][1] == board[row][2] == current_player:
        show_winner_dialog(current_player)
    # Check column
    elif board[0][col] == board[1][col] == board[2][col] == current_player:
        show_winner_dialog(current_player)
    # Check diagonal
    elif (row == col and
            board[0][0] == board[1][1] == board[2][2] == current_player):
        show_winner_dialog(current_player)
    # Check anti-diagonal
    elif (row + col == 2 and
            board[0][2] == board[1][1] == board[2][0] == current_player):
        show_winner_dialog(current_player)
    # Check for a tie
    elif moves == 9:
        show_winner_dialog("Tie")

def show_winner_dialog(winner):
    if winner == "Tie":
        messagebox.showinfo("Game Over", "It's a tie!")
    else:
        messagebox.showinfo("Game Over", f"{winner} wins!")
    reset_game()

def reset_game():
    global current_player, moves, board

    current_player = "X"
    moves = 0
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            button = buttons[i][j]
            button.config(text="")
            button.config(state="normal")

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        button = tk.Button(root, width=10, height=5,
                           command=lambda row=i, col=j: on_button_click(row, col))
        button.grid(row=i, column=j)
        buttons[i][j] = button

root.mainloop()