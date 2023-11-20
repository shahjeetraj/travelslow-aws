// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>

// Write a function to replace vowels with numbers
int arglen(string word);

int main(int argc, string argv[])
{
    for (int i = 1; i < argc; i++)
    {
        int len = arglen(argv[i]);
    }
    printf("\n");
}

// Write a function to replace vowels with numbers
int arglen(string word)
{
    int a = 0;
    do
    {
        a++;
        if (word[a] == 'a')
        {
            word[a] = '6';
        }
        else if (word[a] == 'e')
        {
            word[a] = '3';
        }
        else if (word[a] == 'i')
        {
            word[a] = '1';
        }
        else if (word[a] == 'o')
        {
            word[a] = '0';
        }
    }
    while(word[a]!=0);
    printf("%s ",word);
    return a;
}
