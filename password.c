// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <ctype.h>
#include <cs50.h>
#include <stdio.h>

int len(string word);
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
    int plen = len(password);
    for (int i = 0; i < plen; i++)
    {
        if (isupper(password[i]))
        {
            upper++;
            //printf("%c\n",password[i]);
            //printf("%i\n",isupper(password[i]));
        }
        else if (islower(password[i]))
        {
            lower++;
            //printf("%c\n",password[i]);
            //printf("%i\n",islower(password[i]));
        }
        else if (isdigit(password[i]))
        {
            number++;
            //printf("%c\n",password[i]);
            //printf("%i\n",isdigit(password[i]));
        }
        else if (ispunct(password[i]))
        {
            symbol++;
            //printf("%c\n",password[i]);
            //printf("%i\n",isdigit(password[i]));
        }
        else if (upper >= 1 && lower >= 1 && number >= 1 && symbol >= 1)
        {
            break;
        }
        else if (isspace(password[i]))
        {
            //printf("%c\n",password[i]);
            break;
        }
        else
        {
            i++;
        }
    }
    if (upper >= 1 && lower >= 1 && number >= 1 && symbol >= 1)
    {
        //printf("lower %i upper %i number%i symbol%i\n", lower, upper, number, symbol);
        return true;
    }
    else
    {
        //printf("lower %i upper %i number%i symbol%i\n", lower, upper, number, symbol);
        return false;
    }
}

int len(string word)
{
    int a = 0;
    do
    {
        a++;
    }
    while(word[a]!=0);
    return a;
}
