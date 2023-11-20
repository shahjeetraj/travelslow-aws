#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <math.h>

void global_count(string text, int *letters, int *words, int *sentences);

int main(void)
{
    // ask for text from user
    string text = get_string("Text: ");
    int letters;
    int words;
    int sentences;
    global_count(text, &letters, &words, &sentences);
    // calculation
    float l = (float) letters / (float) words * 100;
    float s = (float) sentences / (float) words * 100;
    // final grading
    int index = round(0.0588 * l - 0.296 * s - 15.8);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >=1 && index <= 16)
    {
        printf("Grade %i\n",index);
    }
    else
    {
        printf("Grade 16+\n");
    }
}

// single function to calculate everything at once.
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
