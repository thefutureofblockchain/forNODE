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
    char c;
    int n;
    int i = 0;
    for (n= 1; n <= strlen(a); n = n+1) {
        c = a[n-1];
        if (isalpha(c) != 0) {
            i = i+1;

        }
    }
    printf("words is %d\n", i);
    return i;
}

int sentence(string a ){

    return 0;
}

int words(string a){
    char c;
    int j;
    int n;
    for (n= 1; n <= strlen(a); n = n+1) {
        c = a[n-1];
        if ( c == ' ') {
            j = j+1;
            printf("%d\n", j);}}
    return 0;
    }