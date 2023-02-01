#include <cs50.h>
#include <stdio.h>

int get_start_size(void);
int get_end_size(int q);
int return_years_1(int n, int m);

int main(void)
{
        int n = get_start_size();
        int sizee = get_end_size(n);
        int years = return_years_1(n, sizee);
        printf("A %i \n" , years);
}
    // TODO: Prompt for end size
    // TODO: Calculate number of years until we reach threshold
    // TODO: Print number of years
int get_start_size (void) {
        int n;
        do
        {
                n = get_int("Starting Size: ");
        }
        while (n < 9);
        return n;
}

int get_end_size (int q)
{
        int n;
        do
        {
                n = get_int("End size: ");
        }
        while (q > n);
        return n ;
}
int return_years_1 (int n , int m)
{
        int a = m - n;
        return a;
}