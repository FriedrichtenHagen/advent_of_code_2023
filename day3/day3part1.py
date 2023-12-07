# testing
import re

with open("/Users/friedrichtenhagen/coding/advent_of_code_2023/day3/day3input_debugging.txt") as f:
    data = f.read().strip()
    lines = data.split("\n")
    print(lines)
    symbols = ['!', '@', '#', '$', '%', 'ˆ', '&', '*', '(', ')', '_']
    part_number_sum = 0
    for line_index, line in enumerate(lines):
        # Convert the list of strings to a list of integers
        numbers_with_indices = [(int(num), match.start()) for match, num in zip(re.finditer(r'\d+', line), re.findall(r'\d+', line))]
        print(numbers_with_indices)
        # check if each number is a 'part number'
        for tuple in numbers_with_indices:
            tuple_ispart = False
            number = tuple[0]
            number_length = len(str(number))
            index_in_line = tuple[1]
            for i in range(index_in_line, index_in_line+number_length):
                if(
                    lines[line_index-1][index_in_line-1] in symbols or
                    lines[line_index-1][index_in_line] in symbols or
                    lines[line_index-1][index_in_line+1] in symbols or
                    lines[line_index][index_in_line+1] in symbols or
                    lines[line_index+1][index_in_line+1] in symbols or
                    lines[line_index+1][index_in_line] in symbols or
                    lines[line_index+1][index_in_line-1] in symbols or
                    lines[line_index][index_in_line-1] in symbols
                   ):
                    # this is a part number!
                    print(f'part number: {tuple}')