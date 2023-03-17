doodle = input()

number_of_chars_before_opening_paren = len(doodle[:doodle.index('(') + 1])
number_of_chars_after_closing_paren = len(doodle[doodle.index(')'):])

print('correct' if number_of_chars_before_opening_paren == number_of_chars_after_closing_paren else 'fix')