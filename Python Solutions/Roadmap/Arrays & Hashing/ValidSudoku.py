from collections import defaultdict

class Solution:
    def isValidSudoku(self, board) -> bool:

        for i in range(9):
            row_seen = {}
            col_seen = {}

            for j in range(9):
                # Check row i
                if board[i][j] in row_seen:
                    if board[i][j] != ".":
                        return False
                else:
                    row_seen[board[i][j]] = 1

                # Check column i
                if board[j][i] in col_seen:
                    if board[j][i] != ".":
                        return False
                else:
                    col_seen[board[j][i]] = 1

        # Now we need to check 3x3 boxes


        for i in range(9):
            seen = {}
            row_start = (i // 3) * 3
            col_start = (i % 3) * 3

            for j in range(3):
                for k in range(3):
                    row = row_start + j
                    col = col_start + k

                    val = board[row][col]
                    if val == ".":
                        continue
                    if val in seen:
                        return False
                    seen[val] = 1

        return True
    

    def isValidSudokuOnePass(self,board) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])