#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc,  string argv[])
{
    if (argc != 2) {
        printf("error\n");
        return 1;
    }
    string k = argv[1];

char c;

for (int n = 1; n <= strlen(k); n = n+1) {

        c = k[n-1];
        if (isdigit(c)) {
            printf("error\n");
            return 1;
        }}}