number_of_boxes = int(input())
count_sessions = 0
for _ in range(number_of_boxes):
    box_name = input().lower()
    if 'rose' in box_name or 'pink' in box_name:
        count_sessions += 1
print(count_sessions if count_sessions > 0 else 'I must watch Star Wars with my daughter')