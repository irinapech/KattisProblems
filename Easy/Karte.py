cards = input()
repeats = False
suits = {'P': [], 'K': [], 'H': [], 'T': []}
for i in range(len(cards) - 2):
    if cards[i].isalpha():
        number = int(cards[i + 1]) * 10 + int(cards[i + 2])
        if number in suits[cards[i]]:
            repeats = True
        else:
            suits[cards[i]].append(number)

print(suits)
if not repeats:
    for suit in suits:
        print(13 - len(suits[suit]), end=' ')
else:
    print('GRESKA')

# card_string = input()
# split_cards = [card_string[i:i+3] for i in range(0, len(card_string), 3)]
# suits = {'P': [], 'K': [], 'H': [], 'T': []}

# for card in split_cards:
#     suit = card[0]
#     number = int(card[1:3])
#     if number in suits[suit]:
#         print('GRESKA')
#         exit()
#     else:
#         suits[suit].append(number)

# print(' '.join([str(13 - len(suit)) for suit in suits.values()]))