n = int(input())
sum = 0
for _ in range(n):
    first, second = [float(x) for x in input().split()]
    sum += first * second
        
print(f"{sum:.3f}")