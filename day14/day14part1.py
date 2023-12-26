

def move_line_north(start_coordinates, board):
    current_row = start_coordinates[0]
    current_column = start_coordinates[1]
    # check if character is rounded stone O
    if(board[current_row][current_column] == 'O'):
        while(board[current_row - 1][current_column] == '.'):
            # move 'O' further up
            current_row -= 1
        # save 'O' to final position
        board[current_row] = board[current_row][:current_column] + 'O' + board[current_row][current_column:]
        # delete 'O' from start position
        board[start_coordinates[0]] = board[start_coordinates[0]][:start_coordinates[1]] + '.' + board[:start_coordinates[0]][start_coordinates[1]:]


def tilt_board(board):
    for line_index, line in enumerate(board):
        for character_index, character in enumerate(line):
            move_line_north([line_index, character_index], board)

with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day14/debug.txt') as f:
    board = f.read().split()
    for line in board:
        print(line)
    print('________')
    tilt_board(board)