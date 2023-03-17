number_of_cases = int(input())

import math

def decrypt_message(encrypted_message, divide_by, remainder, decrypted_message):
    for i in range(len(encrypted_message)):
        if i % divide_by == remainder:
            decrypted_message.append(encrypted_message[i])

for _ in range(number_of_cases):
    encrypted_message = input()
    decrypted_message = []
    divide_by = int(math.sqrt(len(encrypted_message)))
    for remainder in range(int(math.sqrt(len(encrypted_message))), -1, -1):
        decrypt_message(encrypted_message, divide_by, remainder, decrypted_message)
    print(''.join(decrypted_message))