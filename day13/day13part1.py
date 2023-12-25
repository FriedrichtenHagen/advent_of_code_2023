import re


def check_for_symmetry(pattern_lists):
    horizontal_reflection_line = []
    # start with horizontal symmetry
    for pattern_list in pattern_lists:
        # go through the rows starting from the top of the pattern
        for row_index in range(len(pattern_list)-1):
            # compare upper rows (row 0 -> current row) with lower rows (current row + 1 -> last row)
            upper_rows = pattern_list[:row_index + 1]
            lower_rows = pattern_list[row_index + 1:]
            print(upper_rows)
            print(lower_rows)
            # reverse the upper rows
            reversed_upper_rows = upper_rows[::-1]
            print(reversed_upper_rows)
            # remember to exclude rows that do not exist in the reflection
            length_upper_rows = len(reversed_upper_rows)
            length_lower_rows = len(lower_rows)
            maximum_row_length = min(length_lower_rows, length_upper_rows)
            cut_reversed_upper_rows = reversed_upper_rows[:maximum_row_length]
            cut_lower_rows = lower_rows[:maximum_row_length]
            # check symmetry
            if(cut_reversed_upper_rows == cut_lower_rows):
                print(f'symmerty line above line {row_index}')
            # also add 100 multiplied by the number of rows above each horizontal line of reflection

    # go through columns for vertical symmetry

    # add up the number of columns to the left of each vertical line of reflection

with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day13/debug.txt') as f:
    patterns = re.split(r'\n\n', f.read())

    total_pattern_list = []
    for pattern in patterns:
        pattern_list = pattern.split('\n')
        total_pattern_list.append(pattern_list)

    print(total_pattern_list)
    check_for_symmetry(total_pattern_list)