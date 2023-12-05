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

        # only if there are any spelled numbers in the line
        if(spelled_word_starting_indexes):
            word_start_indexes = {}
            for index, word in enumerate(spelled_word_starting_indexes):
                word_index = line.find(word)

                # check if this number has already been found
                if(word in word_start_indexes):
                    if(word_start_indexes[f"{word}"] < word_index):
                        # the existing index for that number is smaller
                        break
                    else:
                        # existing index of that number is >= the existing index
                        # overwrite the existing number
                        word_start_indexes[f"{word}"] = word_index
                else:
                    word_start_indexes[f"{word}"] = word_index
            print(word_start_indexes)

            first_letter_first_word = min(word_start_indexes.values())
            first_letter_last_word = max(word_start_indexes.values())
            print(first_letter_first_word, first_letter_last_word)

            def find_key_by_value(dictionary, target_value):
                return next((key for key, value in dictionary.items() if value == target_value), None)

            first_number = find_key_by_value(word_start_indexes, first_letter_first_word)
            # look up first_number string as an int
            first_number_int = dict_of_numbers[f'{first_number}']
            last_number = find_key_by_value(word_start_indexes, first_letter_last_word)
            last_number_int = dict_of_numbers[f'{last_number}']
        # iterate over string from the start
        first_number_from_start = ''
        for index, char in enumerate(line):
            # if the first spelled word index is reached: break
            if(index == first_letter_first_word):
                print(first_letter_first_word)
                list_of_first_numbers_from_start.append(first_number_int)
                break
            # check if char is single number
            if(char in array_of_numbers):
                first_number_from_start = char
                list_of_first_numbers_from_start.append(first_number_from_start)
                break
                


        # iterate over string from the end
        first_number_from_end = ''
        for index, char in enumerate(reversed(line)):
            # if the first spelled word index is reached: break

            # it needs to be the last letter of the last word!!!
            if(index == first_letter_first_word):
                print(first_letter_first_word)
                list_of_first_numbers_from_start.append(first_number_int)
                break
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
    new_number_string = int(list_of_first_numbers_from_start[index]) + int(list_of_first_numbers_from_end[index])
    added_numbers.append(int(new_number_string))
# calculate the sum of all the resulting numbers
print('Added numbers:')
print(f'{added_numbers}')
print(f'Total sum: {sum(added_numbers)}')