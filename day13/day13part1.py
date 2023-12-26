import re


def check_for_symmetry(pattern_lists):
    
    for pattern_list in pattern_lists:
        # print(pattern_list)
        for line in pattern_list:
            print(line)
        # start with horizontal symmetry
        # go through the rows starting from the top of the pattern
        for row_index in range(len(pattern_list)-1):
            # compare upper rows (row 0 -> current row) with lower rows (current row + 1 -> last row)
            upper_rows = pattern_list[:row_index + 1]
            lower_rows = pattern_list[row_index + 1:]
            # reverse the upper rows
            reversed_upper_rows = upper_rows[::-1]
            # remember to exclude rows that do not exist in the reflection
            maximum_row_length = min(len(lower_rows), len(reversed_upper_rows))
            cut_reversed_upper_rows = reversed_upper_rows[:maximum_row_length]
            cut_lower_rows = lower_rows[:maximum_row_length]
            # check symmetry
            if(cut_reversed_upper_rows == cut_lower_rows):
                print(f'horizontal symmetry line above row {row_index}')
                number_of_rows_above_each_horizontal_line_of_reflection = row_index + 1
            # also add 100 multiplied by the number of rows above each horizontal line of reflection
            # ...

        # go through columns for vertical symmetry
        pivoted_list = list(map(list, zip(*pattern_list)))
        # for line in pivoted_list:
        #     print(line)

        for column_index in range(len(pivoted_list)-1):
            # compare upper rows (row 0 -> current row) with lower rows (current row + 1 -> last row)
            upper_columns = pivoted_list[:column_index + 1]
            lower_columns = pivoted_list[column_index + 1:]
            # reverse the upper rows
            reversed_upper_columns = upper_columns[::-1]
            # remember to exclude rows that do not exist in the reflection
            maximum_column_length = min(len(lower_columns), len(reversed_upper_columns))
            cut_reversed_upper_rows = reversed_upper_columns[:maximum_column_length]
            cut_lower_columns = lower_columns[:maximum_column_length]
            # check symmetry
            if(cut_reversed_upper_rows == cut_lower_columns):
                print(f'vertical symmetry line to the right of column {column_index}')
                number_of_columns_left_of_vertical_line_of_reflection = column_index + 1
            # add up the number of columns to the left of each vertical line of reflection


with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day13/debug.txt') as f:
    patterns = re.split(r'\n\n', f.read())

    total_pattern_list = []
    for pattern in patterns:
        pattern_list = pattern.split('\n')
        total_pattern_list.append(pattern_list)

    # print(total_pattern_list)
    check_for_symmetry(total_pattern_list)