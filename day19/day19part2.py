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
                            'value': int(value),
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

    def evaluate_parts(self):
        # go through all machine parts
        for machine_part in self.machine_parts:
            # e.g. {'a': '1222', 'm': '2655', 's': '2876}', 'x': '787'}

            # start at workflow 'in'
            # find work flow 'in' in workflows list
            in_workflow = self.find_workflow_by_name('in')
            if in_workflow == None:
                raise ValueError('Workflow with name 'in' not found.')
            # start the chain of workflows that will decide if this machine part is rejected or accepted
            self.evaluate_workflow(in_workflow, machine_part)

    def find_workflow_by_name(self, workflow_name):
        matching_workflow = next((workflow for workflow in self.workflows if workflow[f'name'] == f'{workflow_name}'), None)
        return matching_workflow

    def evaluate_workflow(self, workflow, current_machine_part):
        # go through all conditions of this workflow
        for condition in workflow['conditions']:
            # prevent the condition loop from continuing if a condition is met
            if self.evaluate_condition(condition, current_machine_part):
                break

        # if current_machine_part has not been accepted or rejected: go to fallback value
        if 'accepted_status' not in current_machine_part:
            # check if fallback target is A or R
            fallback_target = workflow['fallback_target']
            if fallback_target == 'A':
                current_machine_part['accepted_status'] = True
            elif fallback_target == 'R':
                current_machine_part['accepted_status'] = False
            else:
                # go to the fallback workflow
                fallback_workflow = self.find_workflow_by_name(fallback_target)
                self.evaluate_workflow(fallback_workflow, current_machine_part)

    def evaluate_condition(self, condition, current_machine_part):
        category = condition['category']
        comparison_operator = condition['comparison_operator']
        value = condition['value']
        target = condition['target']

        if comparison_operator == '<':
            if current_machine_part[f'{category}'] < value:
                # start evaluating target workflow
                # if R or A then reject or accept
                if target == 'A':
                    current_machine_part['accepted_status'] = True
                elif target == 'R':
                    current_machine_part['accepted_status'] = False
                else:
                    # move to target workflow
                    target_workflow = self.find_workflow_by_name(target)
                    self.evaluate_workflow(target_workflow, current_machine_part)
                return True
            else:
                # condition is not met!
                return False

        elif comparison_operator == '>':
            if current_machine_part[f'{category}'] > value:
                # start evaluating target workflow
                # if R or A then reject or accept
                if target == 'A':
                    current_machine_part['accepted_status'] = True
                elif target == 'R':
                    current_machine_part['accepted_status'] = False
                else:
                    # move to target workflow
                    target_workflow = self.find_workflow_by_name(target)
                    self.evaluate_workflow(target_workflow, current_machine_part)  
                return True
            else:
                # condition is not met!
                return False
        else:
            raise ValueError(f'invalid comparison_operator found: {comparison_operator}')
        
    def calcute_sum_of_rating_numbers(self):
        # calculate sum of ratings for accepted machine parts
        total_sum = 0

        accepted_machine_parts = (machine_part for machine_part in self.machine_parts if machine_part['accepted_status'] == True)
        for machine_part in accepted_machine_parts:
            machine_part_sum = int(machine_part['a']) + int(machine_part['m']) + int(machine_part['s']) + int(machine_part['x'])
            total_sum += machine_part_sum
        return total_sum
    
    def calculate_number_of_machine_part_combinations(self, rating_range):
        machine_part_list = []
        for x in range(rating_range):
            for m in range(rating_range):
                for a in range(rating_range):
                    for s in range(rating_range):
                        machine_part = {
                            'x': x,
                            'm': m,
                            'a': a,
                            's': s
                        }
                        machine_part_list.append(machine_part)
        return machine_part_list
    
if __name__ == "__main__":
    input_path = '/Users/friedrichtenhagen/coding/advent_of_code_2023/day19/input.txt'
    
    part1 = MachinePartOrganizer(input_path)
    # parse the input and store in machine_parts and workflows
    part1.read_input()
    part1.machine_parts = part1.calculate_number_of_machine_part_combinations(4000)

    pprint.pprint(part1.workflows)
    pprint.pprint(part1.machine_parts)
    # # run the parts through the workflow
    # # each part will either be rejected (R) or accepted (A)
    # part1.evaluate_parts()
    # print('Evaluated machine parts:')
    # pprint.pprint(part1.machine_parts)

    # # what do you get if you add together all of the rating numbers for all of the parts that ultimately get accepted?
    # # Adding all of the ratings for all of the accepted parts gives the sum total of 19114.
    # result = part1.calcute_sum_of_rating_numbers()
    # print(f'The total sum is {result}')


