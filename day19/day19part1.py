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
            workflow_strings = parts[0].split('\n')
            for workflow_string in workflow_strings:
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

                
                self.workflows.append(workflow)
                pprint.pprint(self.workflows)

            # read out machine parts
            machine_part_strings = parts[1].split('\n')
            for machine_part_string in machine_part_strings:
                # split each attribute string
                attributes_strings = machine_part_string.split(',')
                # remove { } from string
                # ...

                
                # find x attribute value
                equals_index_x = attributes_strings[0].find('=')
                x = machine_part_string[equals_index_x + 1:]
                # find m attribute value
                equals_index_m = attributes_strings[1].find('=')
                m = machine_part_string[equals_index_m + 1:]
                # find a attribute value
                equals_index_a = attributes_strings[2].find('=')
                a = machine_part_string[equals_index_a + 1:]
                # find s attribute value
                equals_index_s = attributes_strings[3].find('=')
                s = machine_part_string[equals_index_s + 1:]

                machine_part = {
                    'x': x,
                    'm': m,
                    'a': a,
                    's': s
                }
                print(machine_part)


# start at in

if __name__ == "__main__":
    input_path = '/Users/friedrichtenhagen/coding/advent_of_code_2023/day19/debug.txt'
    part1 = MachinePartOrganizer(input_path)
    part1.read_input()