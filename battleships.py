#!/usr/bin/python3
"""
A simple command line battleships game.
"""
from random import randint

# Create an empty list for ocean grid
board = []

# Add five "O"'s to empty list five times eg, five lists in a list
for x in range(5):
    board.append(["O"] * 5)


# Print out ocean grid in pretty format
def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)


# Generate random numbers in grid where ship will be located
def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
# Display location of battleship, remove when playing
# print("Co-ordinates of the battleship")
# print(ship_row)
# print(ship_col)

# Allow the player four guesses, checking their inputs for every guess
for turn in range(4):
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        print("Turn", turn + 1)
        break
    else:
        if ((guess_row < 0 or guess_row > 4) or
            (guess_col < 0 or guess_col > 4)):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        # Print their current turn
        print("Turn", turn + 1)
        print_board(board)
        # Print "Game Over" if player guesses wrong on their last turn
        if turn == 3:
            print("Game Over")
