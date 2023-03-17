blocks = int(input())
i = 1
height = 0
while blocks - i * i >= 0:
    blocks = blocks - i * i
    height += 1
    i += 2
print(height)