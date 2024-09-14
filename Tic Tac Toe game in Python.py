import tkinter as tk
from tkinter import messagebox
import random

# Function to check for a win
def check_win():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# Function to check for a draw
def check_draw():
    for row in board:
        if "" in row:
            return False
    return True

# Function to handle button click
def on_click(row, col):
    global current_player
    if board[row][col] == "" and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_win():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            if current_player == "O":
                computer_move()

# Function for computer's move
def computer_move():
    global current_player
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_win():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
            current_player = "X"

# Function to reset the game
def reset_game():
    global board, current_player, game_over
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize the game variables
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

# Create the buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", width=10, height=3, command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Start the main event loop
root.mainloop()
