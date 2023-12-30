#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check for correct command-line usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open forensic image for reading
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open forensic image.\n");
        return 1;
    }

    // Recover JPEGs
    // Define a buffer to read data from the file
    BYTE buffer[BLOCK_SIZE];

    // Counter for JPEG file names
    int jpegCounter = 0;

    // File pointer for the current JPEG file
    FILE *jpegFile = NULL;

    // Loop through the forensic image
    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        // Check for the start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If a JPEG file is already open, close it
            if (jpegFile != NULL)
            {
                fclose(jpegFile);
            }

            // Create a new JPEG file
            char filename[8];
            sprintf(filename, "%03i.jpg", jpegCounter++);
            jpegFile = fopen(filename, "w");

            // Check if the file is successfully created
            if (jpegFile == NULL)
            {
                fprintf(stderr, "Could not create JPEG file.\n");
                fclose(file);
                return 1;
            }
        }

        // Write data to the JPEG file
        if (jpegFile != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, jpegFile);
        }
    }

    // Close any remaining files
    if (jpegFile != NULL)
    {
        fclose(jpegFile);
    }

    // Close the forensic image file
    fclose(file);

    return 0;
}
