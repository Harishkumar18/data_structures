

class check_sudoku:
    def isValidSudoku(self, board):
        if self.is_row_valid(board) and self.is_col_valid(board) and self.is_square_valid(board):
            return True
        return False

    def is_row_valid(self, board):
        for each in board:
            if not self.is_part_valid(each):
                return False
        return True

    def is_col_valid(self, board):
        for each in zip(*board):
            if not self.is_part_valid(each):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square_board = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_part_valid(square_board):
                    return False
        return True

    def is_part_valid(self, elems):
        nums = [num for num in elems if num!='.']
        return len(nums) == len(set(nums))






if __name__ == '__main__':
    a = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","8"]
    ]
    res = check_sudoku()
    # print(res.is_square_valid1(a))
    print(res.isValidSudoku(a))

    # print("res",res)
