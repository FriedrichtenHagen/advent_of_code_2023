max_red = 12
max_green = 13
max_blue = 14

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes,
# 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

with open("input.txt") as f:
    data = f.read().strip()
    lines = data.split("\n")

    total_sum_power_of_cubes = 0

    for index, game in enumerate(lines):
        # remove 'Game 89:' from each game and then divide into the draws
        draws = game.split(':')[1].strip().split(';')
        # define game maximums of each color
        max_necessary_red = 0
        max_necessary_green = 0
        max_necessary_blue = 0
        # go through each draw of the game
        for draw in draws:

            colors = draw.split(',')
            for color in colors:
                number_of_cubes = int(color.strip().split(' ')[0])
                color_of_cubes = color.strip().split(' ')[1]
                if(color_of_cubes == 'red'):
                    if(number_of_cubes > max_necessary_red):
                        max_necessary_red = number_of_cubes
                elif(color_of_cubes == 'green'):
                    if(number_of_cubes > max_necessary_green):
                        max_necessary_green = number_of_cubes
                elif(color_of_cubes == 'blue'):
                    if(number_of_cubes > max_necessary_blue):
                        max_necessary_blue = number_of_cubes
            power_of_cubes = max_necessary_blue * max_necessary_green * max_necessary_red


        print(f'{index+1}: {draws}')
        print(f'Power of cubes: {power_of_cubes}')
        total_sum_power_of_cubes += power_of_cubes

    print(total_sum_power_of_cubes)