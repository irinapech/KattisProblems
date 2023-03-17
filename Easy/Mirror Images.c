#include <stdio.h>

int main()
{
    int number_of_cases;
    scanf("%d", &number_of_cases);

    for (int i = 0; i < number_of_cases; i++)
    {
        int rows, columns;
        scanf("%d %d", &rows, &columns);
        char picture[rows][columns];
        for (int j = 0; j < rows; j++)
        {
            for (int k = 0; k < columns; k++)
            {
                scanf(" %c", &picture[j][k]);
            }
        }
        printf("Test %d\n", i + 1);
        for (int j = rows - 1; j >= 0; j--)
        {
            for (int k = columns - 1; k >= 0; k--)
            {
                printf("%c", picture[j][k]);
            }
            printf("\n");
        }
    }
}