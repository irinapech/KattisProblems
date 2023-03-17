left, right = [int(x) for x in input().split(' ')]
if left == 0 and right == 0:
    print('Not a moose')
elif left == right:
    print(f'Even {right * 2}')
else:
    print(f'Odd {max(left, right) * 2}')