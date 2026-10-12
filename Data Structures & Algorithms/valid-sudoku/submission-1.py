from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        # 1. Check every row
        for r in range(rows):
            rowSet = set()
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowSet:
                    return False
                rowSet.add(board[r][c])

        # 2. Check every column
        for c in range(cols):
            colSet = set()
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                if board[r][c] in colSet:
                    return False
                colSet.add(board[r][c])

        # 3. Check every 3x3 sub-box
        for box_r in range(0, rows, 3):
            for box_c in range(0, cols, 3):
                boxSet = set()
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in boxSet:
                            return False
                        boxSet.add(board[r][c])

        return True