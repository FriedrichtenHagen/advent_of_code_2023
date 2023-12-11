# y=-xˆ2+lx
# y is distance traveled
# x is time [ms] holding the button
# l is maximal time of race

# Time:        47     70     75     66
# Distance:   282   1079   1147   1062

time_of_race = [47, 70, 75, 66]
current_distance_record = [282, 1079, 1147, 1062]

# To see how much margin of error you have, determine the number of ways you can beat the record in each race
all_numbers_to_beat_races = []
for i in range(len(time_of_race)):

    # calculate all y values above 0
    list_of_distances_traveled = []
    for x in range(0, time_of_race[i]):
        distance_traveled = -x**2 + time_of_race[i] * x
        list_of_distances_traveled.append(distance_traveled)

    numbers_of_ways_to_beat_current_record = [value for value in list_of_distances_traveled if value > current_distance_record[i]]
    print(numbers_of_ways_to_beat_current_record)
    print(len(numbers_of_ways_to_beat_current_record))
    all_numbers_to_beat_races.append(len(numbers_of_ways_to_beat_current_record))

# multiply the numbers of ways to beat the race
end_result = 1
for number in all_numbers_to_beat_races:
    end_result *= number

print(f'The end result is: {end_result}')

