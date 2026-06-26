class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".": continue
                elif board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[row // 3, col // 3]: return False
                else: 
                    rows[row].append(board[row][col])
                    cols[col].append(board[row][col])
                    squares[row // 3, col // 3].append(board[row][col])
        return True


                    
        