#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct person
{
    struct person *parents[2];
    char alleles[2];
} person;

// Function prototypes
char random_allele(void);
person *create_family(int generations);
void print_family(person *p);
void free_family(person *p);

int main(void)
{
    // Seed the random number generator
    srand(time(NULL));

    // Create a family with 3 generations
    person *p = create_family(3);

    // Print the family
    print_family(p);

    // Free the allocated memory
    free_family(p);

    return 0;
}

char random_allele(void)
{
    return (rand() % 2) ? 'A' : 'B';
}

person *create_family(int generations)
{
    // TODO: Allocate memory for a new person
    person *new_person = malloc(sizeof(person));

    // TODO: Check if there are more generations to allocate
    if (generations > 1)
    {
        // TODO: Create two new parents recursively
        person *parent0 = create_family(generations - 1);
        person *parent1 = create_family(generations - 1);

        // TODO: Set parent pointers for the new person
        new_person->parents[0] = parent0;
        new_person->parents[1] = parent1;

        // TODO: Assign alleles randomly from parents
        new_person->alleles[0] = parent0->alleles[rand() % 2];
        new_person->alleles[1] = parent1->alleles[rand() % 2];
    }
    else
    {
        // TODO: Set both parents to NULL for the oldest generation
        new_person->parents[0] = NULL;
        new_person->parents[1] = NULL;

        // TODO: Assign alleles randomly for the oldest generation
        new_person->alleles[0] = random_allele();
        new_person->alleles[1] = random_allele();
    }

    // TODO: Return a pointer to the allocated person
    return new_person;
}

void print_family(person *p)
{
    if (p == NULL)
    {
        return;
    }

    printf("Person with alleles %c%c\n", p->alleles[0], p->alleles[1]);

    // Recursively print parents
    print_family(p->parents[0]);
    print_family(p->parents[1]);
}

void free_family(person *p)
{
    if (p == NULL)
    {
        return;
    }

    // Recursively free parents before freeing the child
    free_family(p->parents[0]);
    free_family(p->parents[1]);

    // Free the current person
    free(p);
}
