n = int(input())

multiples = [int(input()) for _ in range(n)]
# print("\n")

# i = 0
# while i < n:
#     for j in range(i + 1, n):
#         # print(f"multiples[i] = {multiples[i]}, multiples[j] = {multiples[j]}")
#         if multiples[j] % multiples[i] == 0:
#             print(multiples[j])
#             i = j
#             break
#     if j == n - 1:
#         break
#     else:    
#         i += 1

point = -1
for i in range(n):
    if point == -1:
        point = i
    elif multiples[i] % multiples[point] == 0:
        print(multiples[i])
        point = -1