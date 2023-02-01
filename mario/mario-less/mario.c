#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = 10;
    int y = 1;
    for (int i = 0; i < x; i++) {
        for (int q = x-i-1; q > 0; q--) {
                printf(".");
            }
        for (int j = x-i; j < x; j++) {
            printf("#");
        }
    printf("\n");
    }
}