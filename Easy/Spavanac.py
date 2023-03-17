hours, minutes = [int(x) for x in input().split(' ')]
if minutes < 45 and hours > 0:
    print(f"{hours - 1} {60 + minutes - 45}")
elif minutes < 45 and hours == 0:
    print(f"{23} {60 + minutes - 45}")
else:
    print(f"{hours} {minutes - 45}")