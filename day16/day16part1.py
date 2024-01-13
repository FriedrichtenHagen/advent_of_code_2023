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
    direction_symbol = next((key for key, value in directions.items() if value == direction), None)

    # mark current pos on energized table
    energized_layout[current_pos[0]][current_pos[1]] = '#'
    # is it necessary to mark the number of different directions? 


    # next step depending on the character
    if(current_character == '.'):
        # set direction symbol
        layout[current_pos[0]][current_pos[1]] = direction_symbol

        mirror_stepper([current_pos[0] + direction[0], current_pos[1] + direction[1]], direction )
    elif(current_character == '#'):
        mirror_stepper([current_pos[0] + direction[0], current_pos[1] + direction[1]], direction )
    elif(current_character == '\\'):
        
        # change of directions:
        # [0, 1] -> [1, 0]
        # [-1, 0] -> [0, -1]
        # [1, 0] -> [0, 1]
        # [0, -1] -> [-1, 0]
        # the direction coordinates are switched
        new_direction = [direction[1], direction[0]]
        mirror_stepper([current_pos[0] + new_direction[0], current_pos[1] + new_direction[1]], new_direction )
    elif(current_character == '/'):
        
        # change of directions:
        # [0, 1] -> [-1, 0]
        # [-1, 0] -> [0, 1]
        # [1, 0] -> [0, -1]
        # [0, -1] -> [1, 0]
        # the direction coordinates are switched and multiplied by -1
        new_direction = [direction[1] * -1, direction[0] * -1]
        mirror_stepper([current_pos[0] + new_direction[0], current_pos[1] + new_direction[1]], new_direction )
    elif(current_character == '-'):
        if(direction == [1, 0] or direction == [-1, 0]):
            # beam is split
            new_direction1 = [0, -1]
            new_direction2 = [0, 1]
            mirror_stepper([current_pos[0] + new_direction1[0], current_pos[1] + new_direction1[1]], new_direction1 )
            mirror_stepper([current_pos[0] + new_direction2[0], current_pos[1] + new_direction2[1]], new_direction2 )

        elif(direction == [0, 1] or direction == [0, -1]):
            # beam keeps traveling in same direction
            mirror_stepper([current_pos[0] + direction[0], current_pos[1] + direction[1]], direction )
        else:
            print('Something went wrong: -')
    elif(current_character == '|'):
        if(direction == [1, 0] or direction == [-1, 0]):
            # beam keeps traveling in same direction
            mirror_stepper([current_pos[0] + direction[0], current_pos[1] + direction[1]], direction )

        elif(direction == [0, 1] or direction == [0, -1]):
            # beam is split
            new_direction1 = [0, -1]
            new_direction2 = [0, 1]
            mirror_stepper([current_pos[0] + new_direction1[0], current_pos[1] + new_direction1[1]], new_direction1 )
            mirror_stepper([current_pos[0] + new_direction2[0], current_pos[1] + new_direction2[1]], new_direction2 )
        else:
            print('Something went wrong: |')
    else:
        print('mistake. character not found')



with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day16/debug.txt') as input:
    input = input.read().splitlines()
    layout = []
    for line in input:
        char_list = [char for char in line]
        layout.append(char_list)
    
    for char_list in layout:
        print(char_list)
    # only saves the visited, 'energized' fields
    energized_layout = layout
    # start in left upper corner, going right
    mirror_stepper([0, 0], [0, 1])



# handle edges of fields: next step is not legal!