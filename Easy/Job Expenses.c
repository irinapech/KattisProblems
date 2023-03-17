#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int expenses = 0;

    for (int i = 0; i < n; i++)
    {
        int amount;
        scanf("%d", &amount);
        if (amount < 0)
        {
            expenses -= amount;
        }
    }
    printf("%d\n", expenses);
}