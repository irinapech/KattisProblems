def doubling_digits(number):
    number = list(reversed(number))
    for i in range(len(number)):
        number[i] = int(number[i])
        if i % 2 != 0:
            number[i] *= 2
            if number[i] >= 10:
                number[i] = number[i] // 10 + number[i] % 10
    return number
        
n = int(input())
for _ in range(n):
    checksum = sum(doubling_digits(input()))
    print('PASS' if checksum % 10 == 0 else 'FAIL')