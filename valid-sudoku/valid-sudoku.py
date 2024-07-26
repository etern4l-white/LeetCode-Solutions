class Solution:
    def check_valid(self, l):
        d = {}
        for i in l:
            if i in d and i != '.':
                return False
            else:
                d[i] = 1
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            if not self.check_valid(board[row]):
                return False
        for column in range(9):
            if not self.check_valid([i[column] for i in board]):
                return False
        for i in range(3):
            for j in range(3):
                d = {}
                for x in range(3):
                    for y in range(3):
                        if board[3*i + x][3*j + y] in d and board[3*i + x][3*j + y] != ".":
                            return False
                        else:
                            d[board[3*i + x][3*j + y]] = 1
        return True
