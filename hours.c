#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

float calc_hours(int hours[], int weeks, char output);

int main(void)
{
    const int maxWeeks = 10; // Choose a suitable maximum value for weeks
    int weeks = get_int("Number of weeks taking CS50: ");

    if (weeks > maxWeeks)
    {
        printf("Please enter a value less than or equal to %d for weeks.\n", maxWeeks);
        return 1; // Exit with an error code
    }

    int hours[maxWeeks];

    for (int i = 0; i < weeks; i++)
    {
        hours[i] = get_int("Week %i HW Hours: ", i);
    }

    char output;
    do
    {
        output = toupper(get_char("Enter T for total hours, A for average hours per week: "));
    }
    while (output != 'T' && output != 'A');

    printf("%.1f hours\n", calc_hours(hours, weeks, output));
}

// Complete the calc_hours function
float calc_hours(int hours[], int weeks, char output)
{
    float result = 0.0;

    if (output == 'T')
    {
        for (int i = 0; i < weeks; i++)
        {
            result += hours[i];
        }
    }
    else if (output == 'A')
    {
        for (int i = 0; i < weeks; i++)
        {
            result += hours[i];
        }
        result /= weeks;
    }

    return result;
}
