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
    printf("%lu\n", strlen(a));
    char c;
    int n;
    for (n= 1; n <= strlen(a); n = n+1) {
        c = a[n-1];
        if (isalpha(c) != 0) {
            printf("hell yes");
        }
    }
    printf("\n");
    return 1;
}

int sentence(string a ){
    return 0;
}

int words(string a){
    return 0;
}