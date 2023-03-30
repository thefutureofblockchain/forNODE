#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
char rotate(char c, int n);


int main(int argc,  string argv[])
{
    if (argc != 2) {
        printf("error\n");
        return 1;
    }
    string k = argv[1];
    int b = atoi(k);
    string a = get_string("plaintext: ");
    int it = 0;
    char d;
    while (it > strlen(a)) {
        d = a[it];
        printf("%c",rotate(d, b));
        it++;
    }



char c;

for (int n = 1; n <= strlen(k); n = n+1) {

        c = k[n-1];
        if (isdigit(c)) {
            return 0;
        }
        else {
            printf("error\n");
            return 1;
        }}

        }
char rotate(char d, int b) {
        int cast = d;
        if (isupper(d)) {
        int answer = cast - 65;
        answer += b;
        answer += 65;
        printf("%c", answer);
        return answer;
        }
        else if (islower(d)) {
            int answer = cast - 97;
        answer += b;
        answer += 65;
        printf("%c", answer);
        return answer;

        }
        else {

        return d;
        }


}