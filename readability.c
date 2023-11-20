#include <ctype.h>
#include <cs50.h>
#include <stdio.h>

void global_count(string text, int *letters, int *words, int *sentences);

int main(void)
{
    string text = get_string("Text: ");
    int letters;
    int words;
    int sentences;
    global_count(text, &letters, &words, &sentences);
    //printf("%i letters\n%i words \n%i sentences\n", letters, words, sentences);
    float l = (float) letters / (float) words * 100;
    float s = (float) sentences / (float) words * 100;
    float index = 0.0588 * l - 0.296 * s - 15.8;
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >=1 && index <= 16)
    {
        int ind = (int) index;
        printf("Grade %d\n",ind);
    }
    else
    {
        printf("Grade 16+\n");
    }
}

void global_count(string text, int *letters, int *words, int *sentences)
{
    int a = 0;
    int letter = 1;
    int word = 1;
    int sentence = 0;
    do
    {
        a++;
        if (isalpha(text[a]))
        {
            letter ++;
        }
        else if (isspace(text[a]))
        {
            word ++;
        }
        else if (text[a] == '.' || text[a] == '!' || text[a] == '?')
        {
            sentence ++;
        }
    }
    while(text[a]!='\0');
    //printf("%s length is %i\n",text,a);
    *letters = letter;
    *words = word;
    *sentences = sentence;
}
