#include <stdio.h>

#define MAX 1000

int main()
{
    int number_of_presses;
    scanf("%d", &number_of_presses);

    int time_of_presses[MAX];
    for (int i = 0; i < number_of_presses; i++)
    {
        scanf("%d", &time_of_presses[i]);
    }

    if (number_of_presses % 2 != 0)
    {
        printf("%s", "still running");
    }
    else
    {
        int sum_of_seconds = 0;
        for (int i = number_of_presses - 1; i >= 1; i -= 2)
        {
            sum_of_seconds += time_of_presses[i] - time_of_presses[i - 1];
        }
        printf("%d", sum_of_seconds);
    }
}