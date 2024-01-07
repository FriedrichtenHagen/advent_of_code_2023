
def hash_function(input_string):
    current_value = 0
    for character in input_string:    
        # Determine the ASCII code for the current character of the string.
        ascii_code = ord(character)
        # Increase the current value by the ASCII code you just determined.
        current_value += ascii_code
        # Set the current value to itself multiplied by 17.
        current_value = current_value * 17
        # Set the current value to the remainder of dividing itself by 256.
        current_value = current_value % 256
    return current_value

def fill_boxes(initialization_sequence):
    # contains 255 boxes
    list_of_boxes = []
    for i in range(256):
        list_of_boxes.append([])

    for step in initialization_sequence:
        # divide into label, operation and focal_length
        if '-' in step:
            label = step.split('-')[0]
            box_number = hash_function(label)
            focal_length = None
            # find lense with matching label in box
            # first_found_index = next((index for index, lense in enumerate(box) if lense.get('label') == label), None)
            # found_indexes = [index for index, lense in enumerate(list_of_boxes[box_number]) if lense.get('label') == label]
            
            # remove lense(s) from box
            list_of_boxes[box_number] = [lense for lense in list_of_boxes[box_number] if lense.get('label') != label]
            
        elif '=' in step:
            label = step.split('=')[0]
            box_number = hash_function(label)
            focal_length = step.split('=')[1]

            first_found_index = next((index for index, lense in enumerate(list_of_boxes[box_number]) if lense.get('label') == label), None)
            new_lense = {
                'label' : label,
                'focal_length' : int(focal_length)
            }
            # If there is already a lens in the box with the same label, replace the old lens with the new lens: 
            # remove the old lens and put the new lens in its place, not moving any other lenses in the box.
            if first_found_index is not None:
                list_of_boxes[box_number][first_found_index] = new_lense
            # If there is not already a lens in the box with the same label, add the lens to the box immediately 
            # behind any lenses already in the box. Don't move any of the other lenses when you do this. 
            else:
                list_of_boxes[box_number].append(new_lense)

        else:
            print('something went wrong')
        print(list_of_boxes)
    return list_of_boxes

def calculate_focusing_power(list_of_boxes):
    total_focusing_power = 0
    for box_index, box in enumerate(list_of_boxes):
        for lense_index, lense in enumerate(box):
            lense_focusing_power = (1 + box_index) * (1 + lense_index) * lense['focal_length']
            total_focusing_power += lense_focusing_power
    return total_focusing_power




with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day15/input.txt') as csv:
    initialization_sequence = csv.read().split(',')
    list_of_boxes = fill_boxes(initialization_sequence)
    print(calculate_focusing_power(list_of_boxes))
    
        