#include <cs50.h>
#include <stdio.h>

int get_number(void);

int main(void)
{
    int x = get_number();
    int y = 1;
    for (int i = 0; i < x; i++) {
        for (int q = x-i-1; q > 0; q--) {
                printf(".");
            }
        for (int j = x-i-1; j < x; j++) {
            printf("#");
        }
    printf("\n");
    }
}
int get_number(void)
{
    int a;
    do
    {
    a = get_int("enter: ");
    }
    while (a < 0 || a > 8);
    return a;
}