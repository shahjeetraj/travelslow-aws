#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int len(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    // finding length of the word
    int wlen = len(word);
    // a loop to get the letter wise score
    int score = 0;
    for (int i = 0; i < wlen; i++)
    {
        //conditions for assigning score letter wise
        if (word[i] == 'a' || word[i] == 'A')
        {
            score += POINTS[0];
        }
        else if (word[i] == 'b' || word[i] == 'B')
        {
            score += POINTS[1];
        }
        else if (word[i] == 'c' || word[i] == 'C')
        {
            score += POINTS[2];
        }
        else if (word[i] == 'd' || word[i] == 'D')
        {
            score += POINTS[3];
        }
        else if (word[i] == 'e' || word[i] == 'E')
        {
            score += POINTS[4];
        }
        else if (word[i] == 'f' || word[i] == 'F')
        {
            score += POINTS[5];
        }
        else if (word[i] == 'g' || word[i] == 'G')
        {
            score += POINTS[6];
        }
        else if (word[i] == 'h' || word[i] == 'H')
        {
            score += POINTS[7];
        }
        else if (word[i] == 'i' || word[i] == 'I')
        {
            score += POINTS[8];
        }
        else if (word[i] == 'j' || word[i] == 'J')
        {
            score += POINTS[9];
        }
        else if (word[i] == 'k' || word[i] == 'K')
        {
            score += POINTS[10];
        }
        else if (word[i] == 'l' || word[i] == 'L')
        {
            score += POINTS[11];
        }
        else if (word[i] == 'm' || word[i] == 'M')
        {
            score += POINTS[12];
        }
        else if (word[i] == 'n' || word[i] == 'N')
        {
            score += POINTS[13];
        }
        else if (word[i] == 'o' || word[i] == 'O')
        {
            score += POINTS[14];
        }
        else if (word[i] == 'p' || word[i] == 'P')
        {
            score += POINTS[15];
        }
        else if (word[i] == 'q' || word[i] == 'Q')
        {
            score += POINTS[16];
        }
        else if (word[i] == 'r' || word[i] == 'R')
        {
            score += POINTS[17];
        }
        else if (word[i] == 's' || word[i] == 'S')
        {
            score += POINTS[18];
        }
        else if (word[i] == 't' || word[i] == 'T')
        {
            score += POINTS[19];
        }
        else if (word[i] == 'u' || word[i] == 'U')
        {
            score += POINTS[20];
        }
        else if (word[i] == 'v' || word[i] == 'V')
        {
            score += POINTS[21];
        }
        else if (word[i] == 'w' || word[i] == 'W')
        {
            score += POINTS[22];
        }
        else if (word[i] == 'x' || word[i] == 'X')
        {
            score += POINTS[23];
        }
        else if (word[i] == 'y' || word[i] == 'Y')
        {
            score += POINTS[24];
        }
        else if (word[i] == 'z' || word[i] == 'Z')
        {
            score += POINTS[25];
        }
    }
    return score;
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
