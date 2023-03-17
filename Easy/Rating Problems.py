n, k = [int(x) for x in input().split(' ')]
sum_ratings = sum([int(input()) for _ in range(k)])
print(f"{(sum_ratings + (n - k) * (-3)) / n} {(sum_ratings + (n - k) * 3) / n}")