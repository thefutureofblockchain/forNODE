#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

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
    for (n=1; n <= strlen(a); n++) {
        char c;
        c = 'm';
        printf("%d\n", isalpha(c));
        return 0;
    }
}

int sentence(string a ){
    return 0;
}

int words(string a){
    return 0;
}