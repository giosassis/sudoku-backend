from pydantic import BaseModel
from typing import List

class SudokuPuzzle(BaseModel):
    board: List[List[int]]