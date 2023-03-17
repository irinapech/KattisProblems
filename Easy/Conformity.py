number_of_frosh = int(input())
frosh_combinations = dict()
for i in range(number_of_frosh):
    combination = str(sorted([int(x) for x in input().split(' ')]))
    if combination in frosh_combinations:
        frosh_combinations[combination] += 1
    else:
        frosh_combinations[combination] = 1

most_popular_combination = max(frosh_combinations.values())
count = 0
for combination in frosh_combinations:
    if frosh_combinations[combination] == most_popular_combination:
        count += frosh_combinations[combination]
print(count)

# max_combination = max(frosh_combinations.values())
# popularity_sum = sum(filter(lambda x: x == max_combination, frosh_combinations.values()))
# print(popularity_sum)