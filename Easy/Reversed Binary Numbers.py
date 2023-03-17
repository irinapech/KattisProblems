number = int(input())
binary_number = bin(number)
reversed_binary_number = str(binary_number)[::-1][:-len('b0')]
print(int(reversed_binary_number, 2))

# print(int(str(bin(int(input())))[::-1][:-2], 2))