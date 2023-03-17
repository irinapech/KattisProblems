name = input()
name_without_adjacent_repeats = []
[name_without_adjacent_repeats.append(name[i]) for i in range(len(name)) if name[i] != name[i - 1] or i == 0]
print(''.join(name_without_adjacent_repeats))