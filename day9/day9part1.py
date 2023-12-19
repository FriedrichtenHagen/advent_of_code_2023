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
    two_dimensional_difference_list = [history]
    recursive_difference_calculator(history, two_dimensional_difference_list)
    # print(two_dimensional_difference_list)
    # add initial zero
    two_dimensional_difference_list[-1].append(0)
    reversed_difference_list = two_dimensional_difference_list[::-1]
    # print(reversed_difference_list)

    for row_index, row in enumerate(reversed_difference_list):
        if row_index == len(reversed_difference_list)-1:
            continue  # Skip the last row since there is no next row

        # a + difference = c
        # d
        # ac
        # dfg
        # ....
        difference = reversed_difference_list[row_index][-1]
        a = reversed_difference_list[row_index + 1][-1]
        c = a + difference
        reversed_difference_list[row_index + 1].append(c)
    forecasted_difference_list = reversed_difference_list[::-1]
    print('Updated reversed list:')
    for list in forecasted_difference_list:
        print(list)


    # save final next value (top row, predicted number)


def recursive_difference_calculator(list_of_numbers, two_dimensional_difference_list):
            difference_list = []
            for number_index in range(len(list_of_numbers)-1):
                # compare number to following number
                difference = list_of_numbers[number_index+1] - list_of_numbers[number_index]
                difference_list.append(difference)
            two_dimensional_difference_list.append(difference_list)
            if(sum(difference_list) == 0):
                for list in two_dimensional_difference_list:
                    print(list)
                return 
            else:
                # print(two_dimensional_difference_list)
                recursive_difference_calculator(difference_list, two_dimensional_difference_list)
            
example_history1 = [24, 38, 52, 66, 80, 94, 108, 122, 136, 150, 164, 178, 192, 206, 220, 234, 248, 262, 276, 290, 304]
example_history2 = [5, 4, 13, 36, 73, 128, 229, 462, 1032, 2399, 5601, 12970, 29584, 66034, 143565, 303669, 626287, 1264754, 2512757, 4930676, 9578227]
example_history3 = [10, 13, 16, 21, 30, 45]

list_of_histories = extract_from_input()
extrapolate_history(example_history3)
