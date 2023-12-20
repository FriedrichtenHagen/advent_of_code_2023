# Find the single giant loop starting at S. 
# How many steps along the loop does it take to get from the starting position
# to the point farthest from the starting position?


def read_input():
    with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day10/input.txt') as f:
        maze_matrix = f.read().split('\n')
        # print(maze_matrix)


        return maze_matrix

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

possible_directions = {
    '|' : [[-1, 0], [1, 0]],
    '-' : [[0, -1], [0, 1]],
    'L' : [[0, 1], [-1, 0]],
    'J' : [[-1, 0], [0, -1]],
    '7' : [[0, -1], [1, 0]],
    'F' : [[0, 1], [1, 0]],
    '.' : [],
    'S' : [[-1, 0], [1, 0], [0, -1], [0, 1]] # S has no fix directions
}
    # moves starting from N clockwise
    # list_of_all_moves = [[-1,0], [0,1], [1,0], [0,-1]]

def stepper(position, step_counter, path, previous_move):
    # read current character [y, x]
    current_character = maze_matrix[position[0]][position[1]]
    # look up possible moves in dict
    possible_moves_current_character = possible_directions[current_character]
    # exclude the inverted previous move! We do not want to go backwards
    if(previous_move):
        possible_moves_current_character = [arr for arr in possible_moves_current_character if arr != [-previous_move[0], -previous_move[1]]]

    # go through possible moves
    for move in possible_moves_current_character:
        # check if move is legal
        new_position_y = position[0] + move[0]
        new_position_x = position[1] + move[1]
        # end condition: S is reached again
        if(maze_matrix[new_position_y][new_position_x] == 'S'):
            print(f'Step:{step_counter}. Character: {current_character}')
            return {
                'position': position,
                'steps': step_counter,
                'path': path
            }
        new_character = maze_matrix[new_position_y][new_position_x]
        # look up moves of new character
        possible_moves_new_character = possible_directions[new_character]
        # check if move from current character matches an inverted move from new character
        if([-move[0], -move[1]] in possible_moves_new_character):
            step_counter += 1
            path.append(current_character)
            print(path)
            print(step_counter)
            # valid move: keep goin'
            stepper([new_position_y, new_position_x], step_counter, path, move)


def loop_stepper(start_position):
    position = start_position
    move_stack = []
    path = []
    step_counter = 0
    while(maze_matrix[position[0]][position[1]] != 'S' or step_counter == 0):
        # read current character [y, x]
        current_character = maze_matrix[position[0]][position[1]]
        # look up possible moves in dict
        possible_moves_current_character = possible_directions[current_character]
        # exclude the inverted previous move! We do not want to go backwards
        if move_stack:
            previous_move = move_stack[-1]
            if(previous_move):
                possible_moves_current_character = [arr for arr in possible_moves_current_character if arr != [-previous_move[0], -previous_move[1]]]

        # go through possible moves
        # for start on S only take one path of two possible paths
        if current_character == 'S':
            move = possible_moves_current_character[0]
            new_position_y = position[0] + move[0]
            new_position_x = position[1] + move[1]
            new_character = maze_matrix[new_position_y][new_position_x]
            # look up moves of new character
            possible_moves_new_character = possible_directions[new_character]
            # check if move from current character matches an inverted move from new character
            if([-move[0], -move[1]] in possible_moves_new_character):
                path.append(current_character)
                step_counter += 1
                move_stack.append(move)
                position = [new_position_y, new_position_x]
                print(path)
                print(step_counter)

                print(f'move_stack: {move_stack}')
                # valid move: keep goin'
        else:
            for move in possible_moves_current_character:
                new_position_y = position[0] + move[0]
                new_position_x = position[1] + move[1]
                new_character = maze_matrix[new_position_y][new_position_x]
                # look up moves of new character
                possible_moves_new_character = possible_directions[new_character]
                # check if move from current character matches an inverted move from new character
                if([-move[0], -move[1]] in possible_moves_new_character):
                    path.append(current_character)
                    step_counter += 1
                    move_stack.append(move)
                    position = [new_position_y, new_position_x]
                    # print(path)
                    print(step_counter)

                    # print(f'move_stack: {move_stack}')
                    # valid move: keep goin'
    # S has been reached
    return {
                'position': position,
                'steps': step_counter,
                'path': path
            }

maze_matrix = read_input()

# find position of S [x, y]
def find_s(searched_character):
    for y_index, row in enumerate(maze_matrix):
        for x_index, character in enumerate(row):
            if(maze_matrix[y_index][x_index] == searched_character):
                return [y_index, x_index]

position_of_s = find_s('S')


result = loop_stepper(position_of_s)
print(result)

# what letter is S?