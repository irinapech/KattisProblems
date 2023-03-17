#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

int sum_after_doubling_digits_number(char number[])
{
    int sum = 0;
    int len = strlen(number);
    for (int i = len - 1; i >= 0; i--)
    {
        int place_value = len - i;
        int digit = number[i] - '0'; 
        if (place_value % 2 == 0)
        {
            digit *= 2;
            if (digit >= 10)
            {
                digit = digit % 10 + digit / 10;
            }
        }
        sum += digit;
    }
    return sum;
}

int main()
{
    int number_of_test_cases;
    scanf("%d", &number_of_test_cases);
    for (int i = 0; i < number_of_test_cases; i++)
    {
        char check_number[MAX];
        scanf("%s", &check_number);
        int sum = sum_after_doubling_digits_number(check_number);
        if (sum % 10 == 0)
        {
            printf("%s\n", "PASS");
        }
        else
        {
            printf("%s\n", "FAIL");
        }
    }
}