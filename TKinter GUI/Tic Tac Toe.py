import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

def on_button_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner(row, col):
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Tic Tac Toe", "This cell is already taken!")

def check_winner(row, col):
    # Check row
    if board[row][0] == board[row][1] == board[row][2] == current_player:
        return True
    # Check column
    if board[0][col] == board[1][col] == board[2][col] == current_player:
        return True
    # Check diagonal
    if row == col and board[0][0] == board[1][1] == board[2][2] == current_player:
        return True
    if row + col == 2 and board[0][2] == board[1][1] == board[2][0] == current_player:
        return True
    return False

def check_draw():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

def reset_game():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                                    command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
