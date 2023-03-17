x, y, n = [int(x) for x in input().split(' ')]

for i in range(1, n + 1):
    print('FizzBuzz' if i % x == 0 and i % y == 0 
          else 'Fizz' if i % x == 0 
          else 'Buzz' if i % y == 0 
          else i)