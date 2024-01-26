


class PoolDigger:
    """A class for managing pool digging operations."""
    
    def __init__(self, input_path):
        self.name = 'day 18'
        self.INPUT_PATH = input_path
        self.dig_plan = [['S']]

    def read_input(self):
        instructions = []
        with open(self.INPUT_PATH) as i:
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

    def dig_border_trench(self, instructions_list):

        current_position = [0, 0]
        for instruction in instructions_list:

            current_direction = instruction['direction']
            length = instruction['length']

            current_row = current_position[0]
            current_column = current_position[1]

            # right
            if current_direction == 'R':
                # add range check
                if 0 <= current_column + length < len(self.dig_plan[current_row]):
                # field exist:
                    for l in range(length):
                        self.dig_plan[current_row][current_column + l + 1] = '#'
                else:
                    # field does not exist:
                    # add length times # to current row
                    for l in range(length):
                        if 0 <= current_column + l + 1 < len(self.dig_plan[current_row]):
                            # the row exists
                            self.dig_plan[current_row][current_column + l + 1] = '#'
                        else:
                            # insert # add start of row (since we are going left)
                            self.dig_plan[current_row].append('#')
                            # add length times . to all other rows
                            all_other_row_indexes = [row_index for row_index, row in enumerate(self.dig_plan) if row_index != current_row]
                            for index in all_other_row_indexes:
                                self.dig_plan[index].append('#')
                # update current pos
                current_position = [current_row, current_column + length]
            # left
            elif current_direction == 'L':
                # add range check
                if 0 <= current_column - length < len(self.dig_plan[current_row]):
                # field exist:
                    for l in range(length):
                        self.dig_plan[current_row][current_column - l - 1] = '#'
                else:
                    # field does not exist:
                    # add length times # to current row
                    for l in range(length):
                        if 0 <= current_column - l + 1 < len(self.dig_plan[current_row]):
                            # the row exists
                            self.dig_plan[current_row][current_column - l - 1] = '#'
                        else:
                            # insert # add start of row (since we are going left)
                            self.dig_plan[current_row].insert(0, '#')
                            # add length times . to all other rows
                            all_other_row_indexes = [row_index for row_index, row in enumerate(self.dig_plan) if row_index != current_row]
                            for index in all_other_row_indexes:
                                self.dig_plan[index].insert(0, '.')

                # update current pos
                current_position = [current_row, current_column - length]
            # down
            elif current_direction == 'D':
                # check if new row needs to be added
                if 0 <= current_row + length < len(self.dig_plan):
                    # the used rows already exist
                    for l in range(length):
                        self.dig_plan[current_row + l][current_column] = '#'
                else:
                    # the used rows need to be created
                    # maybe only some rows already exist
                    for l in range(length):
                        if 0 <= current_row + l + 1 < len(self.dig_plan):
                            # the row already exists
                            self.dig_plan[current_row + l][current_column] = '#'
                        else:
                            # the row needs to be created
                            # create row that has the width of current row
                            width_of_current_row = len(self.dig_plan[current_row])
                            new_row = ['.'] * width_of_current_row
                            new_row[current_column] = '#'
                            self.dig_plan.append(new_row)

                # update current pos
                current_position = [current_row + length, current_column]            
            # up
            elif current_direction == 'U':
                # check if new row needs to be added
                if 0 <= current_row - length < len(self.dig_plan):
                    # the used rows already exist
                    for l in range(length):
                        self.dig_plan[current_row - l - 1][current_column] = '#'
                else:
                    # the used rows need to be created
                    # maybe only some rows already exist
                    for l in range(length):
                        if 0 <= current_row - l - 1 < len(self.dig_plan):
                            # the row already exists
                            self.dig_plan[current_row - l - 1][current_column] = '#'
                        else:
                            # the row needs to be created
                            # create row that has the width of current row
                            width_of_current_row = len(self.dig_plan[current_row])
                            new_row = ['.'] * width_of_current_row
                            new_row[current_column] = '#'
                            self.dig_plan.insert(0, new_row)
                # update current pos
                current_position = [current_row - length, current_column]  

    def fill_trench(self):
        for row_index, row in enumerate(self.dig_plan):
            for column_index, column in enumerate(self.dig_plan[row_index]):
                if self.dig_plan[row_index][column_index] == '.':
                    inside_pool_right = False
                    inside_pool_left = False
                    inside_pool_up = False
                    inside_pool_down = False
                    # check in four directions
                    # if we cross a '#' in all four directions we know that we are inside the pool

                    # right
                    fields_to_the_right = len(row) - (column_index + 1)
                    for f in range(fields_to_the_right):
                        if self.dig_plan[row_index][column_index + f + 1] == '#':
                            inside_pool_right = True
                            break
                        else: 
                            continue
                    # left
                    fields_to_the_left = column_index
                    for f in range(fields_to_the_left):
                        if self.dig_plan[row_index][column_index - f - 1] == '#':
                            inside_pool_left = True
                            break
                        else: 
                            continue
                    # up
                    fields_to_the_top = row_index
                    for f in range(fields_to_the_top):
                        if self.dig_plan[row_index - f - 1][column_index] == '#':
                            inside_pool_up = True
                            break
                        else: 
                            continue
                    # down
                    fields_to_the_bottom = len(self.dig_plan) - (row_index + 1)
                    for f in range(fields_to_the_bottom):
                        if self.dig_plan[row_index + f + 1][column_index] == '#':
                            inside_pool_down = True
                            break
                        else: 
                            continue

                    if inside_pool_right and inside_pool_left and inside_pool_down and inside_pool_up:
                        self.dig_plan[row_index][column_index] = '#'

    def print_trench_plan(self):
        for dir in self.dig_plan:
            print(dir)
        print('>>>>>>>>>>>>>>>>>>>')

    def count_trench_volume(self):
        ''' counts the # fields in the filed trench '''
        trench_square_meters = 0
        for row in self.dig_plan:
            for character in row:
                if character == '#':
                    trench_square_meters += 1
        return trench_square_meters




if __name__ == "__main__":
    input_path = '/Users/friedrichtenhagen/coding/advent_of_code_2023/day18/input.txt'
    # instance of PoolDigger class with the specified input_path
    pool_digger = PoolDigger(input_path)
    
    instructions_list = pool_digger.read_input()
    pool_digger.dig_border_trench(instructions_list)
    print('trench border')
    pool_digger.print_trench_plan()
    
    pool_digger.fill_trench()
    print('filled trench:')
    pool_digger.print_trench_plan()

    trench_volume = pool_digger.count_trench_volume()
    print(f'The trench has a volume of: {trench_volume}')