#include <cs50.h>
#include <stdio.h>

int get_start_size(void);
int get_end_size(void);
int return_years_1(int n);

int main(void)
{
        int n = get_start_size();
        int sizee = get_end_size();
        int years = return_years_1(n, sizee);
}
    // TODO: Prompt for end size
    // TODO: Calculate number of years until we reach threshold
    // TODO: Print number of years
int get_start_size (void) {
        int n = get_int("Starting Size: ");
        return n;
}

int get_end_size (void)
{
        int n = get_int("End size: ");
        return n ;
}