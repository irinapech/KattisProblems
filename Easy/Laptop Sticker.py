wc, hc, ws, hs = [int(x) for x in input().split(' ')]
if ws - 2 < wc and hs - 2 < hc:
    print(1)
else:
    print(0)