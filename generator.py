import random
from solver import is_valid

def generate_sudoku(difficulty="medium"):
    board = [[0] * 9 for _ in range(9)]
    fill_board(board)
    remove_numbers(board, difficulty)
    return board

def fill_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if fill_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def remove_numbers(board, difficulty):
    difficulty_levels = {
        "beginner": 41,  
        "easy": 46,      
        "medium": 51,
        "hard": 53,      
        "master": 57     
    }
    num_to_remove = difficulty_levels.get(difficulty, 51)
    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)
    for _ in range(num_to_remove):
        row, col = positions.pop()
        board[row][col] = 0
