#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int letters(string a);
int sentence(string a);
int words(string a);

int main(void)
{
    string a = get_string("Text: ");
    int L = letters(a);
    int S = sentence(a);
    int W = words(a);
}

int letters(string a) {
    while (isalpha(a)) {
        printf("%s\n", a)
        
    }
}

int sentence(string a ){

}

int words(string a){

}