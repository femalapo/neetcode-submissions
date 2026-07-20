class Solution:
    def checkRow(self, row, board):
        seen = set()
        for val in board[row]:
            if val != "." and val in seen:
                return False

            seen.add(val)
        
        return True

    def checkCol(self, col, board):
        seen = set()
        for row in range(len(board)):
            val = board[row][col]
            if val != "." and val in seen:
                return False

            seen.add(val)

        return True

    # Assume top-left is given
    def checkBox(self, row, col, board):
        seen = set()
        for r in range(row, row+3):
            for c in range(col, col+3):
                val = board[r][c]
                if val != "." and val in seen:
                    
                    return False

                seen.add(val)

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            if self.checkRow(row, board) == False:
                return False
            
        for col in range(len(board[0])):
            if self.checkCol(col, board) == False:
                return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if self.checkBox(row, col, board) == False:
                    return False

        return True
        