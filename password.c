// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <ctype.h>
#include <cs50.h>
#include <stdio.h>

bool checkuppercase(string password);
bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    // check if password meets criteria
    int upper = 0;
    int lower = 0;
    int number = 0;
    int symbol = 0;
    for (int i = 0; i < 999; i++)
    {
        if (isupper(password[i]))
        {
            upper++;
        }
        if (islower(password[i]))
        {
            lower++;
        }
        if (isdigit(password[i]))
        {
            number++;
        }
        if (ispunct(password[i]))
        {
            symbol++;
        }
        if (upper >= 1 && lower >= 1 && number >= 1 && symbol >= 1)
        {
            break;
        }
        int isspace = password[i];
        if ( isspace == 0)
        {
            break;
        }
        else
        {
            i++;
        }
    }
    if (upper >= 1 && lower >= 1 && number >= 1 && symbol >= 1)
    {
        return true;
    }
    else
    {
        return false;
    }
}
