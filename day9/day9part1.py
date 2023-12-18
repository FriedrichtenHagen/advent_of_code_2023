# 24 38 52 66 80 94 108 122 136 150 164 178 192 206 220 234 248 262 276 290 304


def extract_from_input():
    with open("/Users/friedrichtenhagen/coding/advent_of_code_2023/day9/input.txt") as f:
        data = f.read().strip()
        lines = data.split("\n")
        list_of_histories = []
        for line in lines:
            list_of_values = line.split(' ')
            list_of_histories.append(list_of_values)
    return list_of_histories

def extrapolate_history(history):
    two_dimensional_difference_list = []
    recursive_difference_calculator(history, two_dimensional_difference_list)
        

def recursive_difference_calculator(list_of_numbers, two_dimensional_difference_list):
            difference_list = []
            for number_index in range(len(list_of_numbers)-1):
                # compare number to following number
                difference = abs(list_of_numbers[number_index] - list_of_numbers[number_index+1])
                difference_list.append(difference)
            two_dimensional_difference_list.append(difference_list)
            if(sum(difference_list) == 0):
                print(two_dimensional_difference_list)
                return 
            else:
                # print(two_dimensional_difference_list)
                recursive_difference_calculator(difference_list, two_dimensional_difference_list)
            
example_history = [24, 38, 52, 66, 80, 94, 108, 122, 136, 150, 164, 178, 192, 206, 220, 234, 248, 262, 276, 290, 304]

list_of_histories = extract_from_input()
extrapolate_history(example_history)
