n, t = [int(x) for x in input().split(' ')]
cocktail = sorted([int(input()) for _ in range(n)])
cocktail.reverse()

flag = True
longest_effect = cocktail[0]

for x in cocktail[1:]:
    longest_effect -= t
    if longest_effect < 1:
        flag = False
        break
    
print("YES" if flag else "NO")
