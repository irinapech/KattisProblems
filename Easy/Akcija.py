number_of_books = int(input())
books_prices = sorted([int(input()) for _ in range(number_of_books)], reverse=True)
sum = sum([books_prices[i] for i in range(number_of_books) if i % 3 != 2])
print(sum)
