dominant = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
not_dominant = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}

number_of_hands, trump_suit = [x for x in input().split(' ')]
number_of_hands = int(number_of_hands) * 4

number_of_points = 0
for card in range(number_of_hands):
    hands = input()
    card = hands[0]
    suit = hands[1]
    if suit == trump_suit:
        number_of_points += dominant[card]
    else:
        number_of_points += not_dominant[card]

print(number_of_points)
