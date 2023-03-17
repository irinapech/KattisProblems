#include <stdio.h>

int main()
{
    int dice1, dice2;
    scanf("%d %d", &dice1, &dice2);

    int number_of_possible_sums = dice1 * dice2;
    int sums[number_of_possible_sums];
    int k = 0;
    for (int i = 1; i <= dice1; i++)
    {
        for (int j = 1; j <= dice2; j++)
        {
            sums[k] = i + j;
            k++;
        }
    }

    int number_of_unique_sums = dice1 + dice2;
    int sums_frequency[number_of_unique_sums];

    for (int i = 0; i < number_of_unique_sums; i++)
    {
        sums_frequency[i] = 0;
    }

    for (int i = 0; i < k; i++)
    {
        sums_frequency[sums[i]]++;
    }

    int max = sums_frequency[0];
    for (int i = 0; i < number_of_unique_sums; i++)
    {
        if (sums_frequency[i] > max)
        {
            max = sums_frequency[i];
        }
    }
    for (int i = 0; i < number_of_unique_sums; i++)
    {
        if (sums_frequency[i] == max)
        {
            printf("%d\n", i);
        }
    }
}