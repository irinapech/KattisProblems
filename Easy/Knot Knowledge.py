input()
to_learn = [int(x) for x in input().split(' ')]
learnt = [int(x) for x in input().split(' ')]
for knot in learnt:
    to_learn.remove(knot)
for x in to_learn:
    print(f"{x} ")