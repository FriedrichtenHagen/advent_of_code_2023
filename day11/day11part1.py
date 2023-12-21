with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day11/input_debugging.txt') as f:
    lines = f.read().split('\n')
    for line in lines:
        print(line)
    print('llllllll')




def expand_universe():
    # expand rows
    copy_lines = lines[:]
    lines_added = 0
    for row_index, row in enumerate(copy_lines):
        if(not '#' in row):
           empty_row = row[:]
           # add another empty line
           lines.insert(row_index + lines_added, empty_row)
           lines_added += 1

    # expand lines
    copy_columns = lines[:]
    columns_added = 0
    for column_index in range(len(copy_columns[0])):
        column_is_empty = True
        for row_index, row in enumerate(copy_columns):
            if(row[column_index] == '#'):
                column_is_empty = False
        if(column_is_empty):
            columns_added += 1
            for row_index2, row2 in enumerate(copy_columns):
                # add '.' to each row on that column_index
                index_to_insert = column_index+columns_added
                row_add = lines[row_index2][:index_to_insert] + '.' + lines[row_index2][index_to_insert:]
                # replace row with row with added '.'
                lines[row_index2] = row_add
        
        


expand_universe()
for line in lines:
    print(line)