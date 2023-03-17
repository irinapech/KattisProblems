cards_in_hand = [x for x in input().split(' ')]
ranks = dict()
for card in cards_in_hand:
    if card[0] in ranks:
        ranks[card[0]] += 1
    else:
        ranks[card[0]] = 1
print(max(ranks.values()))