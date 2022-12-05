#include <stdio.h>
#include <cs50.h>
int main(void)
{
    int height  = get_int("height : ");

    if (height >= 1 && height <= 8) {
    printf("height is \n", height);
    }
}