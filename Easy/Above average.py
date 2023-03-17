c = int(input())

for x in range(c):
    scores = [int(x) for x in input().split(' ')]
    n = scores[0]
    scores.pop(0)
    count = 0
    average = sum(scores) / n
    # count = sum([1 if x > average else 0 for x in scores])
    count = len([x for x in scores if x > average])
    print(f"{round(count / n * 100, 3):.3f}%")