import copy

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
    print([current_character, direction_symbol])
    # mark current pos on energized table
    energized_layout[current_pos[0]][current_pos[1]] = '#'
    for line in energized_layout:
        print(line)
    # is it necessary to mark the number of different directions? 


    # next step depending on the character
    if(current_character == '.'):
        # set direction symbol
        layout[current_pos[0]][current_pos[1]] = direction_symbol

        # boundary check
        y = current_pos[0] + direction[0]
        x = current_pos[1] + direction[1]
        if 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
            mirror_stepper([current_pos[0] + direction[0], current_pos[1] + direction[1]], direction ) 
        else:
            return
    elif(current_character == direction_symbol):
        # we have been here before! This is a cycle
        return
    elif(current_character in ['v', '<', '>', '^']):
        # set direction symbol
        layout[current_pos[0]][current_pos[1]] = direction_symbol

        # boundary check
        y = current_pos[0] + direction[0]
        x = current_pos[1] + direction[1]
        if 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
            mirror_stepper([current_pos[0] + direction[0], current_pos[1] + direction[1]], direction ) 
        else:
            return
    elif(current_character == '\\'):
        
        # change of directions:
        # [0, 1] -> [1, 0]
        # [-1, 0] -> [0, -1]
        # [1, 0] -> [0, 1]
        # [0, -1] -> [-1, 0]
        # the direction coordinates are switched
        new_direction = [direction[1], direction[0]]
        
        # boundary check
        y = current_pos[0] + new_direction[0]
        x = current_pos[1] + new_direction[1]
        if 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
            mirror_stepper([current_pos[0] + new_direction[0], current_pos[1] + new_direction[1]], new_direction ) 
        else:
            return
    elif(current_character == '/'):
        
        # change of directions:
        # [0, 1] -> [-1, 0]
        # [-1, 0] -> [0, 1]
        # [1, 0] -> [0, -1]
        # [0, -1] -> [1, 0]
        # the direction coordinates are switched and multiplied by -1
        new_direction = [direction[1] * -1, direction[0] * -1]

        # boundary check
        y = current_pos[0] + new_direction[0]
        x = current_pos[1] + new_direction[1]
        if 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
            mirror_stepper([current_pos[0] + new_direction[0], current_pos[1] + new_direction[1]], new_direction ) 
        else:
            return
    elif(current_character == '-'):
        if(direction == [1, 0] or direction == [-1, 0]):
            # beam goes left
            new_direction1 = [0, -1]
            # boundary check
            y = current_pos[0] + new_direction1[0]
            x = current_pos[1] + new_direction1[1]
            if 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
                mirror_stepper([current_pos[0] + new_direction1[0], current_pos[1] + new_direction1[1]], new_direction1 ) 
            
            # beam goes right
            new_direction2 = [0, 1]
            # boundary check
            y = current_pos[0] + new_direction2[0]
            x = current_pos[1] + new_direction2[1]
            if 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
                mirror_stepper([current_pos[0] + new_direction2[0], current_pos[1] + new_direction2[1]], new_direction2) 
            else:
                return

        elif(direction == [0, 1] or direction == [0, -1]):
            # beam keeps traveling in same direction
            # boundary check
            y = current_pos[0] + direction[0]
            x = current_pos[1] + direction[1]
            if 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
                mirror_stepper([current_pos[0] + direction[0], current_pos[1] + direction[1]], direction ) 
            else:
                return
        else:
            print('Something went wrong: -')
    elif(current_character == '|'):
        if(direction == [1, 0] or direction == [-1, 0]):
            # beam keeps traveling in same direction
            # boundary check
            y = current_pos[0] + direction[0]
            x = current_pos[1] + direction[1]
            if 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
                mirror_stepper([current_pos[0] + direction[0], current_pos[1] + direction[1]], direction ) 
            else:
                return
        elif(direction == [0, 1] or direction == [0, -1]):
            # beam goes up
            new_direction1 = [-1, 0]
            # boundary check
            y = current_pos[0] + new_direction1[0]
            x = current_pos[1] + new_direction1[1]
            if 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
                mirror_stepper([current_pos[0] + new_direction1[0], current_pos[1] + new_direction1[1]], new_direction1 ) 
            
            # beam goes down
            new_direction2 = [1, 0]
            # boundary check
            y = current_pos[0] + new_direction2[0]
            x = current_pos[1] + new_direction2[1]
            if 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
                mirror_stepper([current_pos[0] + new_direction2[0], current_pos[1] + new_direction2[1]], new_direction2) 
            else:
                return
        else:
            print('Something went wrong: |')
    else:
        print('mistake. character not found')

with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day16/input.txt') as input:
    input = input.read().splitlines()
    layout = []
    for line in input:
        char_list = [char for char in line]
        layout.append(char_list)
    
    # only saves the visited, 'energized' fields
    energized_layout = copy.deepcopy(layout)
    # start in left upper corner, going right
    mirror_stepper([0, 0], [0, 1])
    print('direction arrow copy:')
    for line in layout:
        print(line)
    print('energized copy:')
    for line in energized_layout:
        print(''.join(line))


    count_hash = sum(row.count("#") for row in energized_layout)
    print(count_hash)


# handle fields with multiple arrows