import numpy as np

# directions
directions = {
    'v': [1, 0],
    '^': [-1, 0],
    '>': [0, 1],
    '<': [0, -1]
}


def mirror_stepper(current_pos: list, direction: list):
    # check current character
    current_character = layout[current_pos[0]][current_pos[1]]

    # next step depending on the character
    if(current_character == '.'):
        # keep going in same direction
        layout[current_pos[0]][current_pos[1]] = '#'
        mirror_stepper(current_pos[0] + direction[0], current_pos[1] + direction[1] )
    else:
        print('END')





with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day16/debug.txt') as input:
    input = input.read().splitlines()
    layout = []
    for line in input:
        char_list = [char for char in line]
        layout.append(char_list)
    
    for char_list in layout:
        print(char_list)