number_of_cards, predicted_card, number_of_steps = [int(x) for x in input().split(' ')]
for _ in range(number_of_steps):
    chosen_cards = [int(x) for x in input().split(' ')]
    chosen_cards.pop(0)
    if predicted_card in chosen_cards:
        print('KEEP')
    else:
        print('REMOVE')
