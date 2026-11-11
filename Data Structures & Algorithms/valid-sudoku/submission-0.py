class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isRowValid(row):
                return False
        
        for col in range(9):
            if not self.isColumnValid(board, col):
                return False
        
        for x in range(3):
            for y in range(3):
                if not self.isBoxValid(board, x, y):
                    return False
        
        return True

        
    def isRowValid(self, row):
        frequencies = {}

        for num in row:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        
        for key, value in frequencies.items():
            if key != "." and value > 1:
                return False
        
        return True
    
    def isColumnValid(self, board, col):
        frequencies = {}

        for row in board:
            if row[col] not in frequencies:
                frequencies[row[col]] = 1
            else:
                frequencies[row[col]] += 1
        
        for key, value in frequencies.items():
            if key != "." and value > 1:
                return False
        
        return True
    
    def isBoxValid(self, board, x, y):
        frequencies = {}

        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if j // 3 == x and i // 3 == y:
                    if board[i][j] not in frequencies:
                        frequencies[board[i][j]] = 1
                    else:
                        frequencies[board[i][j]] += 1
        
        for key, value in frequencies.items():
            if key != "." and value > 1:
                return False
        
        return True

        
                    



            