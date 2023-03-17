n = int(input())

while n != -1:
    old_time = 0
    distance = 0
    for _ in range(n):
        speed, time_elapsed = [int(x) for x in input().split(' ')]
        distance += speed * (time_elapsed - old_time)
        old_time = time_elapsed
    print(f"{distance} miles")
    n = int(input())
