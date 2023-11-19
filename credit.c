#include <cs50.h>
#include <math.h>
#include <stdio.h>


// function to check length of card
int get_int_len(long value)
{
    int l=1;
    while(value>9)
    {
        value = value / 10;
        l++;
    }
    return l;
}

//function to get the first 2 numbers of the card
void get_card_bin(long value, int *bin, int *bin2)
{
    if (get_int_len(value) == 13)
    {
        *bin = value / 1000000000000;
        *bin2 = value / 100000000000;
    }
    if (get_int_len(value) == 14)
    {
        *bin = value / 10000000000000;
        *bin2 = value / 1000000000000;
    }
    if (get_int_len(value) == 15)
    {
        *bin = value / 100000000000000;
        *bin2 = value / 10000000000000;
    }
    if (get_int_len(value) == 16)
    {
        *bin = value / 1000000000000000;
        *bin2 = value / 100000000000000;
    }
}

bool checksum(long value)
{
    int len = get_int_len(value);
    int cs1 = 0;
    int cs2 = 0;
    int number;
    for (number = 2; number <= len; number=number+2)
    {
        long p = pow(10, number);
        long pp = (value % p);
        long d = p/10;
        int digitodd;
        int temp = pp / d * 2;
        if (temp >= 10)
        {
            int temp1 = temp/10;
            int temp2 = temp%10;
            digitodd = temp1 + temp2;
        }
        else
        {
            digitodd = temp;
        }
        cs1 = cs1 + digitodd;
        //printf("%i\n",digitodd);
    }
    for (number = 1; number <=len; number=number+2)
    {
        long p = pow(10, number);
        long pp = (value % p);
        long d = p/10;
        int digiteven = pp / d;
        cs2 = cs2 + digiteven;
        //printf("%i\n",digiteven);
    }
    //printf("%i\n",cs1);
    //printf("%i\n",cs2);

    if ((cs1+cs2)%10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main(void)
{

    // take input for the card number
    long card;
    do
    {
        card = get_long("Number: ");
    }
    // check length of card
    while (get_int_len(card) < 7);

    // checksum1 check sum of 2 * alternate numbers

    bool cs = checksum(card);

    // check card bin for amex, master or visa
    int bin;
    int bin2;
    get_card_bin(card, &bin, &bin2);
    string card_type;
    if (bin == 3 && (bin2 == 34 || bin2 == 37) && get_int_len(card) == 15)
    {
        card_type = "AMEX";
    }
    else if (bin == 5 && (bin2 == 51 || bin2 == 52 || bin2 == 53 || bin2 == 54 || bin2 == 55) && get_int_len(card) != 15)
    {
        card_type = "MASTERCARD";
    }
    else if (bin == 4 && get_int_len(card) != 15)
    {
        card_type = "VISA";
    }
    else
    {
        card_type = "INVALID";
    }

    if (cs == true)
    {
        printf("%s\n",card_type);
    }
    else
    {
        printf("INVALID\n");
    }
}


