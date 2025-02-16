from fastapi import APIRouter
from fastapi.responses import JSONResponse
from solver import solve_sudoku
from generator import generate_sudoku
from models import SudokuPuzzle

router = APIRouter()

@router.post("/solve")
def solve(board: SudokuPuzzle):
    solution = solve_sudoku(board.board)
    if solution:
        return {"solved_board": solution}
    return {"error": "No solution found"}

@router.get("/generate")
def generate(difficulty: str = "medium"):
    board = generate_sudoku(difficulty)
    solution = solve_sudoku([row.copy() for row in board])  
    print(solution)
    return JSONResponse(content={"generated_board": board, "solution": solution})