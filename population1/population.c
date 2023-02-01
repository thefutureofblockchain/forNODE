#include <cs50.h>
#include <stdio.h>

int get_start_size(void);
int get_end_size(void);
int return_years(int n, int m);

int main(void)
{
        int n = get_start_size();
        printf("a%i", n );
        int sizee = get_end_size();
    // TODO: Prompt for end size
    // TODO: Calculate number of years until we reach threshold
    // TODO: Print number of years
int get_start_size (void) {
        int n = get_int("Starting Size: ");
}
