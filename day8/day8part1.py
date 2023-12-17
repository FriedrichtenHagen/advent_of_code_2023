directions = 'LRRRLRRLRLRRRLRLLLLRRRLRLRRLRLRLRRLRRRLRRLRRRLRLLLRRLRRLRRLRRLRRLLLLLRLRLRRRLRLLRRLRLRRRLRRLRRRLLLRRLRRLRRLRRRLRLRLRRLLRRRLRRLRRRLRRRLRRRLRLRRLRRLRRLRRRLRLRRLRRLLRRRLRRLRRLRRRLRLRLRRLLRRRLLRRLRRRLRRRLRLRRLLRRRLRLRRLLRRLRLRRRLRLRRRLRRLRRLRRLRRRLRRRLRLLRRLRRLLRRLRRRLRRLRLRLRRRLLLRRLRLRRLRRLRLRLLRLRRLRLRLRRRR'

multiple_directions = ''
for i in range(100):
    multiple_directions += directions


def find_node_by_name(name):
    return next((d for d in list_of_nodes if 'name' in d and d['name'] == name), None)

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

def traverse_node_list(start_node):
    current_node = start_node
    for index, direction in enumerate(multiple_directions):
        #check if goal has been reached
        if(current_node['name'] == 'ZZZ'):
            print(f'ZZZ was reached after {index} nodes.')
            break
        else:
        # make the next move according to the direction
            if(direction == 'L'):
                current_node = find_node_by_name(current_node['left'])
            elif(direction == 'R'):
                current_node = find_node_by_name(current_node['right'])
            print(current_node)

            



list_of_nodes = extract_nodes_from_input()
print(list_of_nodes)
# find starting point
AAA = find_node_by_name('AAA')
print(AAA)
traverse_node_list(AAA)