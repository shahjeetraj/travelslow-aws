#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start_population;
        do
        {
            start_population = get_int("Start size: ");
        }
        while (start_population < 9);

    // TODO: Prompt for end size
    int target_population;
        do
        {
            target_population = get_int("End size: ");
        }
        while (target_population < start_population);

    // TODO: Calculate number of years until we reach threshold
    int new_population = 0;
    new_population = start_population;
    int years = 0;
        do
        {
            if (target_population > start_population)
            {
                int born = new_population / 3;
                int died = new_population / 4;
                new_population = new_population + born - died;
                years = years + 1;
            }
            else
            {
                break;
            }
        }
        while (new_population < target_population);

    // TODO: Print number of years
    printf("Years: %i\n", years);
}
