#include <stdio.h>

#define HOURS_IN_DAY 24
#define MINUTES_OR_SECONDS 60

int calculate_seconds_or_minutes(int explosion, int current, int* next_explosion_time_period)
{
    int time;
    if (explosion < current)
    {
        time = MINUTES_OR_SECONDS + explosion - current;
        (*next_explosion_time_period)--;
    }
    else
    {
        time = explosion - current;
    }
    return time;
}

int main()
{
    int current_hour, current_minute, current_second;
    scanf("%d:%d:%d", &current_hour, &current_minute, &current_second);

    int explosion_hour, explosion_minute, explosion_second;
    scanf("%d:%d:%d", &explosion_hour, &explosion_minute, &explosion_second);

    int seconds, minutes, hours;
    seconds = calculate_seconds_or_minutes(explosion_second, current_second, &explosion_minute);
    minutes = calculate_seconds_or_minutes(explosion_minute, current_minute, &explosion_hour);

    if (explosion_hour <= current_hour)
    {
        hours = HOURS_IN_DAY + explosion_hour - current_hour;
    }
    else
    {
        hours = explosion_hour - current_hour;
    }

    printf("%2.2d:%2.2d:%2.2d", hours, minutes, seconds);
}