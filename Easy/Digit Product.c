#include <stdio.h>

int repeated_digits_product(int number)
{
    if (number < 10)
    {
        return number;
    }
    else
    {
        int product = 1;
        while (number != 0)
        {
            if (number % 10 != 0)
            {
                product *= number % 10;
            }
            number /= 10;
        }
        return repeated_digits_product(product);
    }
}

int main()
{
    int input;
    scanf("%d", &input);
    input = repeated_digits_product(input);
    printf("%d\n", input);
}