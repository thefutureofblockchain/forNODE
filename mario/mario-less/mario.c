#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = 10;
    int y = 1;
    for (int i = 0; i < x; i++) {
        for (int j = x-i; j < x; j++) {
            for (int q = x-i; q > 0; q--) {
                printf(".");
            }
            printf("#");
        }
    printf("\n");
    }
}