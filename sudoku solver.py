# 0's represent empty spaces in the board
sample_board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def display_board(board):
    for k in range(len(board)):
        if k > 0 and k % 3 == 0:
            print('------ ------- ------')
        for i in range(len(board[0])):
            if i > 0 and i % 3 == 0:
                print('| ', end='')
            if i != 8:
                print(str(board[k][i]) + ' ', end='')
            else:
                print(board[k][i])


def empty_spaces(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return r, c
    return None


def check_valid(board, possible_num, position):

    # Check if the number is unique in the column
    for r in range(len(board)):
        if board[r][position[1]] == possible_num:
            return False

    # Check if the number is unique in the row
    if possible_num in board[position[0]]:
        return False

    # Find position of top left corner of the 3 x 3 box our possible number
    # is in on the grid
    column = position[1] // 3 * 3
    row = position[0] // 3 * 3

    # Check to see if number is unique in its 3 x 3 box
    for r in range(row, row + 3):
        for c in range(column, column + 3):
            if board[r][c] == possible_num:
                return False
    return True


def complete_puzzle(board):
    # If there's no empty spaces our puzzle is complete!
    empty = empty_spaces(board)
    if empty is None:
        return True

    # Recursively fill in the empty spaces in the puzzle
    row, column = empty
    for j in range(1, 10):
        if check_valid(board, j, (row, column)):
            board[row][column] = j
            if complete_puzzle(board):
                return True
            else:
                board[row][column] = 0
    return False


print('Unsolved Puzzle:')
display_board(sample_board)
print('\n')
complete_puzzle(sample_board)
print('Solved Puzzle:')
display_board(sample_board)
