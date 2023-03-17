def count(substance, calories_per_gram, calories, percentage):
    substance_number = int(substance[:-1])

    if 'g' in substance:
        substance_number *= calories_per_gram
        calories += substance_number
    elif 'C' in substance:
        calories += substance_number

    if calories_per_gram == 9:
        if '%' in substance:
            percentage -= substance_number
            calories = calories / (percentage / 100)
            substance_number = calories * substance_number / 100
        else:
            calories = calories / (percentage / 100)

    elif '%' in substance:
        percentage -= substance_number

    return substance_number, percentage, calories


line_input = input()
while True:

    calories = 0
    fat_number = 0
    while line_input != '-':

        fat, protein, sugar, starch, alcohol = line_input.split(' ')

        temp_calories = 0
        percentage = 100

        protein_number, percentage, temp_calories = count(protein, 4, temp_calories, percentage)
        sugar_number, percentage, temp_calories = count(sugar, 4, temp_calories, percentage)
        starch_number, percentage, temp_calories = count(starch, 4, temp_calories, percentage)
        alcohol_number, percentage, temp_calories = count(alcohol, 7, temp_calories, percentage)
        temp_fat_number, percentage, temp_calories = count(fat, 9, temp_calories, percentage)

        fat_number += temp_fat_number
        calories += temp_calories
        line_input = input()

    fat_percentage = fat_number / calories
    print(f"{round(fat_percentage * 100)}%")

    line_input = input()
    if line_input == '-':
        break
