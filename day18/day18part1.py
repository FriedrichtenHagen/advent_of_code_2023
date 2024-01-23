


class PoolDigger:
    name = 'day 18'
    INPUT_PATH = '/Users/friedrichtenhagen/coding/advent_of_code_2023/day18/debug.txt'

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
        # dig_plan starts with one dug hole '#'
        dig_plan = [
            ['S']
        ]
        current_position = [0, 0]
        for instruction in instructions_list:

            current_direction = instruction['direction']
            length = instruction['length']

            current_row = current_position[0]
            current_column = current_position[1]

            # right
            if current_direction == 'R':
                # add length times # to current row
                for l in range(length):
                    dig_plan[current_row].insert(current_column + 1, '#')
                # add length times . to all other rows
                all_other_row_indexes = [row_index for row_index, row in enumerate(dig_plan) if row_index != current_row]
                for index in all_other_row_indexes:
                    dig_plan[index].insert(current_column, '.')
                # update current pos
                current_position = [current_row, current_column + length]
            # left
            elif current_direction == 'L':
                # add length times # to current row
                for l in range(length):
                    dig_plan[current_row].insert(current_column, '#')
                # add length times . to all other rows
                all_other_row_indexes = [row_index for row_index, row in enumerate(dig_plan) if row_index != current_row]
                for index in all_other_row_indexes:
                    dig_plan[index].insert(current_column, '.')
                # update current pos
                current_position = [current_row, current_column - length]
            # down
            elif current_direction == 'D':
                # check if new row needs to be added
                if 0 <= current_row + length < len(dig_plan):
                    # the used rows already exist
                    for l in range(length):
                        dig_plan[current_row + l][current_column] = '#'
                else:
                    # the used rows need to be created
                    # maybe only some rows already exist
                    for l in range(length):
                        if 0 <= current_row + l < len(dig_plan):
                            # the row already exists
                            dig_plan[current_row + l][current_column] = '#'
                        else:
                            # the row needs to be created
                            # create row that has the width of current row
                            width_of_current_row = len(dig_plan[current_row])
                            new_row = ['.'] * width_of_current_row
                            dig_plan.append([new_row])

                # update current pos
                current_position = [current_row + length, current_column]            
            # up
            elif current_direction == 'U':
                # check if new row needs to be added
                if 0 <= current_row - length < len(dig_plan):
                    # the used rows already exist
                    for l in range(length):
                        dig_plan[current_row - l][current_column] = '#'
                else:
                    # the used rows need to be created
                    # maybe only some rows already exist
                    for l in range(length):
                        if 0 <= current_row - l < len(dig_plan):
                            # the row already exists
                            dig_plan[current_row - l][current_column] = '#'
                        else:
                            # the row needs to be created
                            # create row that has the width of current row
                            width_of_current_row = len(dig_plan[current_row])
                            new_row = ['.'] * width_of_current_row
                            dig_plan.insert(0, new_row)
                # update current pos
                current_position = [current_row - length, current_column]  
            for dir in dig_plan:
                print(dir)
    def fill_trench():
        pass


if __name__ == "__main__":
    instructions_list = PoolDigger.read_input()
    for dir in instructions_list:
        print(dir)
    PoolDigger.dig_border_trench(instructions_list)
    