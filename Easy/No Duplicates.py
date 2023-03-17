phrase = [word for word in input().split(' ')]
no_repeats_phrase = set(phrase)
print('yes' if len(phrase) == len(no_repeats_phrase) else 'no')