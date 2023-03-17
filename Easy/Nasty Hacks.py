number_of_tests = int(input())
for _ in range(number_of_tests):
    r, e, c = [int(x) for x in input().split(' ')]
    if r == e - c:
        print('does not matter')
    elif r < e - c:
        print('advertise')
    else:
        print('do not advertise')
