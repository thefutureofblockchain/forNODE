#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
int letters(string a);
int sentence(string a);
int words(string a);

int main(void)
{
    string a = get_string("Text: ");
    int L = letters(a);
    int S = sentence(a);
    int W = words(a);
    int l = round(L/W);
    int s = round(S/W);
    printf("%d and %d\n", l, s);

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
    printf("letters is %d\n", i);
    return i;
}

int sentence(string a ){
    int n = 0;
    int i= 0;
    char c;
    for (n= 1; n <= strlen(a); n = n+1) {
        c = a[n-1];
        if (c == '.' || c == '?' || c == '!') {
            i = i+1;
        }
}
printf(" sentences is %d\n",i);
return i;}

int words(string a){
    char c;
    int j = 1;
    int n;
    for (n= 1; n <= strlen(a); n = n+1) {

        c = a[n-1];
        if (isblank(c)) {
            j = j+1;
        }


        if (c == '.' && n == strlen(a)) {
            printf("words is %d\n", j);
            return j;
        }
        }


    return 0;
    }