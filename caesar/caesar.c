#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
char rotate(char c, int n);
bool o_digits(string a);

int main(int argc,  string argv[])
{

    string k = argv[1];
    char c;

    if (argc != 2) {
        printf("error\n");
        return 1;
    }
    //printf("%d", isdigit(argv[1][2]));
    if (o_digits(argv[1]) == true) {
            printf("error\n");
            return 1;
    }

    int b = atoi(k);
    string a = get_string("plaintext: ");
    int it = 0;
    char d;
    printf("ciphertext: ");
    while (it < strlen(a)) {
        d = a[it];
        printf("%c",rotate(d,b));
        it++;
    }
    printf("\n");





        }
char rotate(char d, int b) {
        int cast = d;
        if (isupper(d)) {
            int answer = ((cast - 65)+b)%26+65;
            return answer;
        }
        else if (islower(d)) {
            int answer = ((cast - 97)+b)%26+97;
            return answer;

        }
        else {

        return d;
        }


}

bool o_digits(string a){
    int l = strlen(a);
    int i = 0;
    char da;
    for (int n = 0; n<l; n++) {
        da = a[n];
        if (isdigit(da)){
            i+=1;
        }
        else{
            i = 50;
        }
    }
    if (i != 50) {
        return false;
    }
    else {
        return true;
    }

}