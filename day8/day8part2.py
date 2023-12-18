import re

directions = 'LRRRLRRLRLRRRLRLLLLRRRLRLRRLRLRLRRLRRRLRRLRRRLRLLLRRLRRLRRLRRLRRLLLLLRLRLRRRLRLLRRLRLRRRLRRLRRRLLLRRLRRLRRLRRRLRLRLRRLLRRRLRRLRRRLRRRLRRRLRLRRLRRLRRLRRRLRLRRLRRLLRRRLRRLRRLRRRLRLRLRRLLRRRLLRRLRRRLRRRLRLRRLLRRRLRLRRLLRRLRLRRRLRLRRRLRRLRRLRRLRRRLRRRLRLLRRLRRLLRRLRRRLRRLRLRLRRRLLLRRLRLRRLRRLRLRLLRLRRLRLRLRRRR'

multiple_directions = ''
for i in range(10000):
    multiple_directions += directions


def find_node_by_name(name):
    return next((d for d in list_of_nodes if 'name' in d and d['name'] == name), None)

def find_nodes_that_end_with_A():
    pattern = r'.*A$'
    return [d for d in list_of_nodes if re.match(pattern, d['name'])]


def extract_nodes_from_input():
    with open("/Users/friedrichtenhagen/coding/advent_of_code_2023/day8/input.txt") as f:
        data = f.read().strip()
        lines = data.split("\n")
        list_of_nodes = []
        for line in lines:
            name = line.split('=')[0].strip()
            leftright = line.split('=')[1].strip()
            left = leftright.split(',')[0].replace('(', '').strip()
            right = leftright.split(',')[1].replace(')', '').strip()

            node = {
                'name' : name,
                'left' : left,
                'right' : right
            }
            list_of_nodes.append(node)
    return list_of_nodes

def traverse_node_list(start_nodes):
    current_nodes = start_nodes
    for direction_index, direction in enumerate(multiple_directions):
        # go through each thread with the current direction
        # each starting node creates a thread
        for thread_index, current_node in enumerate(current_nodes):

            # make the next move according to the direction
            if(direction == 'L'):
                current_node = find_node_by_name(current_node['left'])
            elif(direction == 'R'):
                current_node = find_node_by_name(current_node['right'])
            print(f'{thread_index}:{current_node}')


        #after going through all threads: check if goal has been reached on this direction
        zzz_reached_for_nodes = 0
        for node in current_nodes:
            # check if last character is Z
            if(node['name'][2] == 'Z'):
                zzz_reached_for_nodes += 1
                # check if all nodes end on Z
                if(zzz_reached_for_nodes == len(current_nodes)):
                    print(f'ZZZ was reached after {direction_index} nodes.')
                    break



            



list_of_nodes = extract_nodes_from_input()
print(list_of_nodes)
# find starting point
nodes_that_start_with_A = find_nodes_that_end_with_A()
print(nodes_that_start_with_A)
traverse_node_list(nodes_that_start_with_A)