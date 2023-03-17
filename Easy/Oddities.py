n = int(input())
for _ in range(n):
    x = int(input())
    print(f"{x} is {'odd' if x % 2 != 0 else 'even'}")