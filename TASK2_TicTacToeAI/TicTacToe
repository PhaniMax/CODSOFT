import random
import math


human_player = 'X'
computer_player = 'O'

def printing_board(board):
    for j in range(0, 9, 3):
        print("|".join(board[j:j+3]))
    print("\n")


def checking_winner(board,player):
    winner_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]        
    ]
    for one in winner_combinations:
        if all(board[j] == player for j in one):
            return True
    return False


def board_full(board):
    return ' ' not in board


def player_movement(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))-1
            if move in range(0,9) and board[move] == ' ':
                return move
            else:                print("Invalid move! Please enter a number between 1 and 9 !!!!!!!!!")
        except ValueError:
            print("Invalid input! Please enter a number.")


def minimax(board,depth,is_maximizing):
    
    if checking_winner(board,human_player):
        return -1
        
    elif checking_winner(board,computer_player):
        return 1
        
    elif board_full(board):
        return 0

    if is_maximizing:
        max_evaluation = -math.inf
        for j in range(9):
            if board[j] == ' ':
                board[j] = 'O'
                evaluation = minimax(board, depth - 1, False)
                board[j] = ' '
                max_evaluation = max(max_evaluation, evaluation)
        return max_evaluation
        
    else:
        min_evaluation = math.inf
        for j in range(9):
            if board[j] == ' ':
                board[j] = 'X'
                evaluation = minimax(board,depth + 1, True)
                board[j] = ' '
                min_evaluation = min(min_evaluation, evaluation)
        return min_evaluation


def ai_move(board):
    best_movement = -1
    best_evaluation = -math.inf
    for j in range(9):
        if board[j] == ' ':
            board[j] = 'O'
            evaluation = minimax(board,9,False)
            board[j] = ' '
            if evaluation > best_evaluation:
                best_evaluation = evaluation
                best_movement = j
    return best_movement


def play():
    
    print("Welcome to Tic Tac Toe!!!!!!!!!!!!!!!!!!!")
    print("Who wants to play first ? 1. Player(X)  2. AI(O) ")
    choice = input("Enter your choice : ")
    
    if choice == '1':
        current_player = 'X'
    elif choice == '2':
        current_player = 'O'
    else:
        print("Invalid choice! Please enter '1' or '2'.")
        return

    while True:
        if current_player == 'X':
            player_movement_index = player_movement(board)
            board[player_movement_index] = 'X'
            printing_board(board)
            if checking_winner(board, 'X'):
                print("Congratulations! You win!")
                break
            if board_full(board):
                print("It's a draw!")
                break
            current_player = 'O'

        elif current_player == 'O':
            print("AI's turn:")
            ai_move_index = ai_move(board)
            board[ai_move_index] = 'O'
            printing_board(board)
            
            if checking_winner(board, 'O'):
                print("AI wins!")
                break
            if board_full(board):
                print("It's a draw!")
                break
            current_player = 'X'


board = [' ' for _ in range(9)]
print("The initial board is :\n")
printing_board(board)
play()



