max_red = 12
max_green = 13
max_blue = 14

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes,
# 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

with open("input.txt") as f:
    data = f.read().strip()
    lines = data.split("\n")
    sum_of_valid_indexes = 0
    for index, game in enumerate(lines):
        # remove 'Game 89:' from each game and then divide into the draws
        draws = game.split(':')[1].strip().split(';')
        # each game is valid until proven otherwise
        game_isvalid = True 
        # go through each draw of the game
        for draw in draws:
            num_red = 0
            num_green = 0
            num_blue = 0
            colors = draw.split(',')
            for color in colors:
                number_of_cubes = color.strip().split(' ')[0]
                color_of_cubes = color.strip().split(' ')[1]
                if(color_of_cubes == 'red'):
                    num_red += int(number_of_cubes)
                elif(color_of_cubes == 'green'):
                    num_green += int(number_of_cubes)
                elif(color_of_cubes == 'blue'):
                    num_blue += int(number_of_cubes)
            # check for validity of this game
            # as soon as one draw exceeds the maximum the whole game is invalid
            if(num_red > max_red or num_blue > max_blue or num_green > max_green):
                # this game is not valid
                game_isvalid = False

        print(f'{index+1}: {draws}')
        print(game_isvalid)
        if(game_isvalid):
            sum_of_valid_indexes += (index+1)
print(sum_of_valid_indexes)