#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for credit card number
    long long card_number;
    do
    {
        card_number = get_long("Number: ");
    }
    while (card_number <= 0);

    // Store the original card number
    long long temp_card_number = card_number;

    // Calculate sum of digits
    int sum = 0;
    int digit_count = 0;

    while (temp_card_number > 0)
    {
        // Get last digit
        int digit = temp_card_number % 10;

        // Every other digit from right
        if (digit_count % 2 == 1)
        {
            digit *= 2;

            // If doubling results in two-digit, add its digits
            sum += (digit % 10) + (digit / 10);
        }
        else
        {
            sum += digit;
        }

        // Move to next digit
        temp_card_number /= 10;
        digit_count++;
    }

    // Check card valid and determine card type
    if (sum % 10 == 0)
    {
        // Count number of digits
        int num_digits = digit_count;

        // Determine first two digits
        temp_card_number = card_number; // Use the original card number
        while (temp_card_number >= 100)
        {
            temp_card_number /= 10;
        }
        int first_two_digits = temp_card_number;

        // Check card type
        if ((num_digits == 15) && (first_two_digits == 34 || first_two_digits == 37))
        {
            printf("AMEX\n");
        }
        else if ((num_digits == 16) && (first_two_digits >= 51 && first_two_digits <= 55))
        {
            printf("MASTERCARD\n");
        }
        else if ((num_digits == 13 || num_digits == 16) && (first_two_digits / 10 == 4))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}
