#include <cs50.h>
#include <stdio.h>

int letters(string a);
int sentence(string a);
int words(string a);

int main(void)
{
    string a = get_string("Enter: ");
    int L = letters(a);
}