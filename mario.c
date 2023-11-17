#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //capture the height in variable called height
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height > 8 || height < 1);
    //print the hashes for the number as per height
    int i;
    for (i = 1; i <= height; ++i)
    {
        int j = height - i;
        printf("%.*s", j, "           ");
        printf("%.*s", i, "#############");
        printf("  ");
        printf("%.*s", i, "############");
        printf("%.*s\n", j, "           ");
    }
}
