


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
        
        
    def dig_border_trench():
        pass
    def fill_trench():
        pass


if __name__ == "__main__":
    content_list = PoolDigger.read_input()
    print(content_list)