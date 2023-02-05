#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
string alphs[] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int a = strlen(word);
    //printf("%i\n", a);
    for (int i = 0; i<=a; i++) {
        char bake = tolower(word[i]);
      //example
        char merge[2];// this is just temporary array to merge with
        merge[0] = bake;
        merge[1] = '\0';
      for (int ba = 0; ba < 25; ba++){
        if (alphs[ba] == merge) {
            printf("y");
        }
        else {
            printf("%s", merge);
        }
      }
      //printf("%i\n%i\n",POINTS[i], i);
    }
    return POINTS[0];
}
