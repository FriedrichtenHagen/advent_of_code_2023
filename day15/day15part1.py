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



with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day15/input.txt') as csv:
    initialization_sequence = csv.read().split(',')
    total_hash_result = 0
    for step in initialization_sequence:
        step_hash = hash_function(step)
        total_hash_result += step_hash
    print(total_hash_result)