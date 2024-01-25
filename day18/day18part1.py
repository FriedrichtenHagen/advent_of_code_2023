


class PoolDigger:
    name = 'day 18'
    INPUT_PATH = '/Users/friedrichtenhagen/coding/advent_of_code_2023/day18/debug.txt'

    # dig_plan starts with one dug hole '#'
    dig_plan = [
        ['S']
    ]

    @staticmethod
    def read_input():
        instructions = []
        with open(PoolDigger.INPUT_PATH) as i:
            lines = i.read().split('\n')
            for line in lines:
                sub_commands = line.split()
                instruction_object = {
                    'direction': sub_commands[0],
                    'length': int(sub_commands[1]),  # Assuming length is an integer
                    'color': sub_commands[2]
                }
                instructions.append(instruction_object)
            return instructions
        

    def dig_border_trench(instructions_list):

        current_position = [0, 0]
        for instruction in instructions_list:

            current_direction = instruction['direction']
            length = instruction['length']

            current_row = current_position[0]
            current_column = current_position[1]

            # right
            if current_direction == 'R':
                # add range check
                if 0 <= current_column + length < len(PoolDigger.dig_plan[current_row]):
                # field exist:
                    for l in range(length):
                        PoolDigger.dig_plan[current_row][current_column + l + 1] = '#'
                else:
                    # field does not exist:
                    # add length times # to current row
                    for l in range(length):
                        if 0 <= current_column + l + 1 < len(PoolDigger.dig_plan[current_row]):
                            # the row exists
                            PoolDigger.dig_plan[current_row][current_column + l + 1] = '#'
                        else:
                            # insert # add start of row (since we are going left)
                            PoolDigger.dig_plan[current_row].append('#')
                            # add length times . to all other rows
                            all_other_row_indexes = [row_index for row_index, row in enumerate(PoolDigger.dig_plan) if row_index != current_row]
                            for index in all_other_row_indexes:
                                PoolDigger.dig_plan[index].append('#')
                # update current pos
                current_position = [current_row, current_column + length]
            # left
            elif current_direction == 'L':
                # add range check
                if 0 <= current_column - length < len(PoolDigger.dig_plan[current_row]):
                # field exist:
                    for l in range(length):
                        PoolDigger.dig_plan[current_row][current_column - l - 1] = '#'
                else:
                    # field does not exist:
                    # add length times # to current row
                    for l in range(length):
                        if 0 <= current_column - l + 1 < len(PoolDigger.dig_plan[current_row]):
                            # the row exists
                            PoolDigger.dig_plan[current_row][current_column - l - 1] = '#'
                        else:
                            # insert # add start of row (since we are going left)
                            PoolDigger.dig_plan[current_row].insert(0, '#')
                            # add length times . to all other rows
                            all_other_row_indexes = [row_index for row_index, row in enumerate(PoolDigger.dig_plan) if row_index != current_row]
                            for index in all_other_row_indexes:
                                PoolDigger.dig_plan[index].insert(0, '.')

                # update current pos
                current_position = [current_row, current_column - length]
            # down
            elif current_direction == 'D':
                # check if new row needs to be added
                if 0 <= current_row + length < len(PoolDigger.dig_plan):
                    # the used rows already exist
                    for l in range(length):
                        PoolDigger.dig_plan[current_row + l][current_column] = '#'
                else:
                    # the used rows need to be created
                    # maybe only some rows already exist
                    for l in range(length):
                        if 0 <= current_row + l + 1 < len(PoolDigger.dig_plan):
                            # the row already exists
                            PoolDigger.dig_plan[current_row + l][current_column] = '#'
                        else:
                            # the row needs to be created
                            # create row that has the width of current row
                            width_of_current_row = len(PoolDigger.dig_plan[current_row])
                            new_row = ['.'] * width_of_current_row
                            new_row[current_column] = '#'
                            PoolDigger.dig_plan.append(new_row)

                # update current pos
                current_position = [current_row + length, current_column]            
            # up
            elif current_direction == 'U':
                # check if new row needs to be added
                if 0 <= current_row - length < len(PoolDigger.dig_plan):
                    # the used rows already exist
                    for l in range(length):
                        PoolDigger.dig_plan[current_row - l - 1][current_column] = '#'
                else:
                    # the used rows need to be created
                    # maybe only some rows already exist
                    for l in range(length):
                        if 0 <= current_row - l - 1 < len(PoolDigger.dig_plan):
                            # the row already exists
                            PoolDigger.dig_plan[current_row - l - 1][current_column] = '#'
                        else:
                            # the row needs to be created
                            # create row that has the width of current row
                            width_of_current_row = len(PoolDigger.dig_plan[current_row])
                            new_row = ['.'] * width_of_current_row
                            new_row[current_column] = '#'
                            PoolDigger.dig_plan.insert(0, new_row)
                # update current pos
                current_position = [current_row - length, current_column]  

    def fill_trench():
        for row_index, row in enumerate(PoolDigger.dig_plan):
            for column_index, column in enumerate(PoolDigger.dig_plan[row_index]):
                inside_pool = False
                # check in four directions
                # if we cross a '#' in all four directions we know that we are inside the pool

                # add border checking to each direction

                # right
                fields_to_the_right = len(row) - column_index
                for f in range(fields_to_the_right):
                    if PoolDigger.dig_plan[row_index][column_index + f + 1] == '#':
                        inside_pool = True
                    else: 
                        continue
                # left
                fields_to_the_left = column_index
                for f in range(fields_to_the_left):
                    if PoolDigger.dig_plan[row_index][column_index - f - 1] == '#':
                        inside_pool = True
                    else: 
                        continue
                if inside_pool:
                    PoolDigger.dig_plan[row_index][column_index] = '#'


    def print_trench_plan():
        for dir in PoolDigger.dig_plan:
            print(dir)
        print('>>>>>>>>>>>>>>>>>>>')




if __name__ == "__main__":
    instructions_list = PoolDigger.read_input()
    for dir in instructions_list:
        print(dir)

    PoolDigger.dig_border_trench(instructions_list)
    PoolDigger.print_trench_plan()
    PoolDigger.fill_trench()
    PoolDigger.print_trench_plan()