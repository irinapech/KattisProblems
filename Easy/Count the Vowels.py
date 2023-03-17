sentence = input().upper()
vowels = 'AEIOU'
sum = 0
for character in sentence:
    if character in vowels:
        sum += 1
print(sum)