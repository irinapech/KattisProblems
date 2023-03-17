number_of_cases = int(input())
for _ in range(number_of_cases):
    beats, seconds = [int(x) for x in input().split(' ')]
    bpm = (60 * beats) / seconds
    print(f"{bpm - 60/ seconds:.4f} {bpm:.4f} {bpm + 60/ seconds:.4f}")