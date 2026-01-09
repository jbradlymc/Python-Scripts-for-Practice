# Tic Tac Toe Game - Board Display Function

import random

board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]


def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        users_move = input("Enter your move (1-9): ")

        # Check if input is a valid number between 1-9
        if not users_move.isdigit() or int(users_move) < 1 or int(users_move) > 9:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        # Convert the move (1-9) to row and column indices (0-2)
        move_index = int(users_move) - 1
        row = move_index // 3
        col = move_index % 3

        # Check if the square is already taken
        if board[row][col] in ['X', 'O']:
            print("That square is already taken! Choose another.")
            continue

        # Update the board with player's move
        board[row][col] = 'O'
        break


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        # Select a random free field using randrange
        random_index = random.randrange(len(free_fields))
        row, col = free_fields[random_index]
        board[row][col] = 'X'

# def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game


board[1][1] = 'X'
display_board(board)
enter_move(board)
draw_move(board)
display_board(board)
enter_move(board)
draw_move(board)
display_board(board)
enter_move(board)
draw_move(board)
display_board(board)
enter_move(board)
draw_move(board)
display_board(board)
