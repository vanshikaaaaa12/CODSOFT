# tic_tac_toe.py

import math

# Game board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    for cond in win_conditions:
        if all(board[i] == player for i in cond):
            return True
    return False

# Check for draw
def is_draw():
    return ' ' not in board

# Human move
def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1,10):
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Cell already taken!")
        else:
            print("Invalid input!")

# AI move using Minimax
def ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

# Minimax algorithm
def minimax(state, depth, is_maximizing):
    if check_winner('O'):
        return 1
    elif check_winner('X'):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if state[i] == ' ':
                state[i] = 'O'
                score = minimax(state, depth + 1, False)
                state[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if state[i] == ' ':
                state[i] = 'X'
                score = minimax(state, depth + 1, True)
                state[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Game loop
def play():
    print("🎮 Tic Tac Toe vs AI")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner('X'):
            print("🎉 You win!")
            break
        if is_draw():
            print("😐 It's a draw!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()
        if check_winner('O'):
            print("💻 AI wins! Better luck next time.")
            break
        if is_draw():
            print("😐 It's a draw!")
            break

play()
