# The newly-improved calibration document consists of lines of text; each line originally contained
# a specific calibration value that the Elves now need to recover. On each line, the calibration value
# can be found by combining the first digit and the last digit (in that order) to form a single
# two-digit number.
# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?


# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen    

with open('code_debugging.txt', 'r') as file:
    # Read the entire content of the file
    content = file.readlines()
    lines = []
    for line in content:
        stripped_line = line.strip()
        lines.append(stripped_line)
    print(lines)
        
    # constants
    array_of_numbers = ['0','1','2','3','4','5','6','7','8','9','0']
    dict_of_numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    }
    list_of_spelled_numbers = list(dict_of_numbers)

    list_of_first_numbers_from_start = []
    list_of_first_numbers_from_end = []


        
    for line in lines:
        # check for spelled out numbers in line
        spelled_word_starting_indexes = [word for index, word in enumerate(list_of_spelled_numbers) if word in line]
        print(spelled_word_starting_indexes)

        word_start_indexes = {}
        for word in spelled_word_starting_indexes:
            word_index = line.find(word)
            word_start_indexes.append(f'{word}': word_index)
        first_letter_first_word = min(word_start_indexes.keys())
        print(first_letter_first_word)

        # iterate over string from the start
        first_number_from_start = ''
        for index, char in enumerate(line):
            # if the first spelled word index is reached: break
            if(index == spelled_word_starting_indexes):
                print('test')
            # check if char is single number
            if(char in array_of_numbers):
                first_number_from_start = char
                list_of_first_numbers_from_start.append(first_number_from_start)
                break
                
        # iterate over string from the end
        first_number_from_end = ''
        for char in reversed(line):
            if(char in array_of_numbers):
                first_number_from_end = char
                list_of_first_numbers_from_end.append(first_number_from_end)
                break        
print('These are the numbers from the start')
print(list_of_first_numbers_from_start)
print('These are the numbers from the end')
print(list_of_first_numbers_from_end)

# add the two numbers together as strings
added_numbers = []
for index, element in enumerate(list_of_first_numbers_from_start):
    new_number_string = list_of_first_numbers_from_start[index] + list_of_first_numbers_from_end[index]
    added_numbers.append(int(new_number_string))
# calculate the sum of all the resulting numbers
print('Added numbers:')
print(f'{added_numbers}')
print(f'Total sum: {sum(added_numbers)}')