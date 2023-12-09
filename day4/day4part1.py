with open("/Users/friedrichtenhagen/coding/advent_of_code_2023/day4/input.txt") as f:
    data = f.read().strip()
    lines = data.split("\n")
    total_points = 0
    for line in lines:
        winning_answers = list(set(list(filter(str.strip, line.split(':')[1].split('|')[0].strip().split(' ')))))
        print(winning_answers)

        choices = list(set(list(filter(str.strip, line.split(':')[1].split('|')[1].strip().split(' ')))))
        print(choices)

        number_of_matches = 0
        for num in choices: 
            if(num in winning_answers):
                number_of_matches += 1

        if(number_of_matches):
            points = 2 ** (number_of_matches - 1)
        else:
            points = 0
        print(f'number of matches: {number_of_matches}')
        print(f'points: {points}')
        total_points += points
print(f'total points: {total_points}')