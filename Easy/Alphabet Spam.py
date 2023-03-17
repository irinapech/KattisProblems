message = input()

whitespace = [character for character in message if character == '_']
lowercase = [character for character in message if character >= 'a' and character <= 'z']
uppercase = [character for character in message if character >= 'A' and character <= 'Z']
symbols = [character for character in message if character < 'A' or (character > 'Z' and character < 'a') or character > 'z']
while '_' in symbols:
    symbols.remove('_')

print(len(whitespace) / len(message))
print(len(lowercase) / len(message))
print(len(uppercase) / len(message))
print(len(symbols) / len(message))