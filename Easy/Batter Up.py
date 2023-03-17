_ = input()
scores = [int(x) for x in input().split() if int(x) >= 0]
print(sum(scores)/len(scores))