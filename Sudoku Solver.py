def is_valid_move(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_cell(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(sudoku):
    empty_cell = find_empty_cell(sudoku)
    if not empty_cell:
        return True
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(sudoku, row, col, num):
            sudoku[row][col] = num

            if solve_sudoku(sudoku):
                return True

            sudoku[row][col] = 0

    return False

if __name__ == "__main__":
    sudoku = [
        [0,0,0,8,0,4,5,0,0],
        [0,1,9,0,2,0,0,0,0],
        [0,0,0,0,1,0,3,0,0],
        [7,0,4,0,0,9,0,8,6],
        [0,0,3,0,8,0,4,0,0],
        [0,0,0,0,0,0,0,0,0],
        [2,7,0,0,0,0,0,4,0],
        [5,0,0,0,0,2,7,1,0],
        [0,9,0,5,0,0,0,0,0]
    ]

    if solve_sudoku(sudoku):
        for row in sudoku:
            print(*row)
    else:
        print("No Solution Found!")