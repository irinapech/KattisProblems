cards = input()
points = 0
t_cards = len([1 for card in cards if card == 'T'])
# t_cards = len(filter(lambda card: card == 'T', cards))
c_cards = len([1 for card in cards if card == 'C'])
g_cards = len([1 for card in cards if card == 'G'])

if t_cards > 0:
    points += t_cards ** 2
if c_cards > 0:
    points += c_cards ** 2
if g_cards > 0:
    points += g_cards ** 2
points += min(t_cards, c_cards, g_cards) * 7
print(points)
