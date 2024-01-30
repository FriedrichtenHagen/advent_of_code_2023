import pprint




class MachinePartOrganizer():
    """A class sorting machine parts."""
    
    def __init__(self, input_path):
        self.INPUT_PATH = input_path
        self.workflows = []
        self.machine_parts = []

    def read_input(self):
        with open(self.INPUT_PATH) as i:
            parts = i.read().split('\n\n')
            # read out workflows
            self.workflows = parts[0].split('\n')
            for workflow_string in self.workflows:
                name = workflow_string.split('{')[0]
                conditions = workflow_string.split('{')[1][0:-1].split(',')
                
                conditions_dicts = []
                fallback_target = None
                for condition_index, condition_string in enumerate(conditions):
                    colon_index = condition_string.find(':')
                    if condition_index != len(conditions) - 1:
                        # regular condition
                        category = condition_string[0]
                        comparison_operator = condition_string[1]
                        value = condition_string[2:colon_index]
                        target = condition_string[colon_index+1:]

                        condition = {
                            'category': category,
                            'comparison_operator': comparison_operator,
                            'value': value,
                            'target': target
                        }
                        conditions_dicts.append(condition)
                    else:
                        # fallback target
                        fallback_target = condition_string

                workflow = {
                    'name': name,
                    'conditions': conditions_dicts,
                    'fallback_target': fallback_target
                }

                pprint.pprint(workflow)


            # read out machine parts
            self.machine_parts = parts[1].split('\n')


# start at in

if __name__ == "__main__":
    input_path = '/Users/friedrichtenhagen/coding/advent_of_code_2023/day19/debug.txt'
    part1 = MachinePartOrganizer(input_path)
    part1.read_input()