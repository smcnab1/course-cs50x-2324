#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for pyramid height between 1 and 8
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Build pyramid
    for (int i = 0; i < height; i++)
    {
        // Print spaces on left of pyramid
        for (int j = 0; j < height - i - 1; j++)
        {
            printf(" ");
        }

        // Print hash for left pyramid
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }

        // Print gap between pyramids
        printf("  ");

        // Print hash for right pyramid
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }

        // Move to next line after row complete
        printf("\n");
    }
    return 0;
}
