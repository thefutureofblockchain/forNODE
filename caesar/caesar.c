#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int isnumber(int c, int a);

int main(int argc,  argv)
{
    if (isnumber(argc, argv[1]) == 1) {
        return 1;
    }
    string k = argv[1];

}

// in is number implement it in a way so as to ensure it is a number as well as the side effect of print
//additionally, you need to have something that checks whether it is a number or not.
int isnumber(int c, int a) {
    if (isdigit(a)) {
        return 1;
        printf("Error: Usage is wrong.");
    }
    else {
        return 0;
    }
}