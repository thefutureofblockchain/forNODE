#include <cs50.h>
#include <stdio.h>

int letters(string a);
int sentence(string a);
int words(string a);

int main(void)
{
    string a = get_string("Text: ");
    printf("%s\n", a);
    string L = a;
    string S = a;
    string W = a;
}