

def move_line_north(start_coordinates, board):
    current_row = start_coordinates[0]
    current_column = start_coordinates[1]
    rock_was_moved = False
    # check if character is rounded stone O
    if board[current_row][current_column] == 'O':
        # check if field above current field exists and is a empty space '.'
        while(current_row - 1) >= 0 and board[current_row - 1][current_column] == '.':
            # move 'O' further up
            current_row -= 1
            rock_was_moved = True
        # save 'O' to final position
        board[current_row] = board[current_row][:current_column] + 'O' + board[current_row][current_column + 1:]
        # delete 'O' from start position if O was moved
        if rock_was_moved:
            board[start_coordinates[0]] = board[start_coordinates[0]][:start_coordinates[1]] + '.' + board[start_coordinates[0]][start_coordinates[1] + 1:]

def tilt_board(board):
    for line_index, line in enumerate(board):
        for character_index, character in enumerate(line):
            move_line_north([line_index, character_index], board)

def calculate_load(tilted_board):
    # multiple the number of rocks in each row with the inverted index and sum these values up
    total_result = 0
    for row_index, row in enumerate(tilted_board):
        for column_index, character in enumerate(row):
            if tilted_board[row_index][column_index] == 'O':
                total_result += len(tilted_board) - row_index
    return total_result

with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day14/input.txt') as f:
    board = f.read().split()
    print('original board')
    for line in board:
        print(line)
    print('________')

    # board is list of lists
    tilt_board(board)

    print('final board:')
    for line in board:
        print(line)
    
    result = calculate_load(board)
    print(result)