fbi_found = False
for i in range(5):
    code = input()
    if 'FBI' in code:
        print(i + 1)
        fbi_found = True
if not fbi_found:
    print('HE GOT AWAY!')