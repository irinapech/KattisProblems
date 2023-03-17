cipher = input()
per = 'PER'
count = 0
for i in range(len(cipher)):
    if cipher[i] != per[i % 3]:
        count += 1
print(count)