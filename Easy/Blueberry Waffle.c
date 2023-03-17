#include <stdio.h>

int main()
{
    int r, f;
    scanf("%d %d", &r, &f);
    if ((f / r) % 2 != 0)
    {
        if ((f % r) < (r / 2))
        {
            printf("%s", "down");
        }
        else
        {
            printf("%s", "up");
        }
    }
    else
    {
        if ((f % r) < (r / 2))
        {
            printf("%s", "up");
        }
        else
        {
            printf("%s", "down");
        }
    }
}