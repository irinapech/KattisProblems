current_hour, current_minute, current_second = [int(x) for x in input().split(':')]
explosion_hour, explosion_minute, explosion_second = [int(x) for x in input().split(':')]

hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

def calculate_seconds_or_minutes(current, explosion, next_time_period):
    if explosion < current:
        time = seconds_in_minute + explosion - current
        next_time_period -= 1
    else:
        time = explosion - current
    return time, next_time_period

seconds, explosion_minute = calculate_seconds_or_minutes(current_second, explosion_second, explosion_minute)
minutes, explosion_hour = calculate_seconds_or_minutes(current_minute, explosion_minute, explosion_hour)

if explosion_hour <= current_hour:
    hours = hours_in_day + explosion_hour - current_hour
else:
    hours = explosion_hour - current_hour

print(f"{hours:02}:{minutes:02}:{seconds:02}")