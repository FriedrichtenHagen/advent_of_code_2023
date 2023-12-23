
with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day11/input.txt') as f:
    lines = f.read().split('\n')
    for line in lines:
        print(line)
    print('_____________separation_______________')




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
        
def find_galaxies_and_rename():
    galaxy_counter = 0
    renamed_galaxy_list = []
    galaxy_position_list = []
    for line_index, line in enumerate(lines):
        indices = [i for i, char in enumerate(line) if char == '#']
        line_copy = list(line[:])

        for row_index in indices:
            line_copy[row_index] = galaxy_counter
            
            galaxy_position = {
                'name': galaxy_counter,
                'coordinates': [line_index, row_index]
            }
            galaxy_position_list.append(galaxy_position)
            galaxy_counter += 1
        renamed_galaxy_list.append(line_copy)

    for re_line in renamed_galaxy_list:
        print(re_line)
    print('tset')
    return galaxy_position_list
    
def calculate_distance(galaxy_pos_list):
    total_distance = 0
    # since travel is only possible on x and y axis, we can simply calculate the difference 
    # between the coordinates as the min num of steps
    galaxy_stack = galaxy_pos_list[:]
    for i in range(len(galaxy_pos_list)-1):
        # for the last position we do not need to calculate any distances, since all previous galaxies all ready point to it
        gal_y_coord = galaxy_pos_list[i]['coordinates'][0]
        gal_x_coord = galaxy_pos_list[i]['coordinates'][1]
        # remove current galaxy from stack, since we will calculate all paths from (and to) this galaxy
        galaxy_stack = galaxy_stack[1:]
        # calculate the distances to all other galaxies in the stack
        for gal_distance_index in range(len(galaxy_stack)):
            distance_y = galaxy_stack[gal_distance_index]['coordinates'][0] - gal_y_coord
            distance_x = galaxy_stack[gal_distance_index]['coordinates'][1] - gal_x_coord
            # add distance sum to total_distance
            total_distance += abs(distance_x) + abs(distance_y)
            # add distance to current starting galaxy object
            galaxy_pos_list[i][f"{galaxy_pos_list[i]['name']}to{galaxy_stack[gal_distance_index]['name']}"] = [distance_y, distance_x]
        # print(galaxy_stack)
    print(galaxy_pos_list)
    return total_distance


expand_universe()
for line in lines:
    print(line)
galaxy_pos_list = find_galaxies_and_rename()
# print(galaxy_pos_list)
total_distance = calculate_distance(galaxy_pos_list)
print(f'The total distance is {total_distance}')