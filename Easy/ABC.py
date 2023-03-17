abc = [int(x) for x in input().split()]
abc.sort()

for letter in input():
    print(abc[ord(letter) - ord('A')], end=' ')
print()