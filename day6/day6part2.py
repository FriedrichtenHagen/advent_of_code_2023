# y=-xˆ2+lx
# y is distance traveled
# x is time [ms] holding the button
# l is maximal time of race

time_of_race = 47707566
current_distance_record = 282107911471062

# calculate all y values above 0
list_of_distances_traveled = []
for x in range(0, time_of_race):
    distance_traveled = -x**2 + time_of_race * x
    list_of_distances_traveled.append(distance_traveled)

numbers_of_ways_to_beat_current_record = [value for value in list_of_distances_traveled if value > current_distance_record]
print(numbers_of_ways_to_beat_current_record)
print(len(numbers_of_ways_to_beat_current_record))


