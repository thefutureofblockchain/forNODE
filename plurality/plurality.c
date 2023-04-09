#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    string b;
    int i;
    for (i = 0; i < candidate_count; i++) {
        b =  candidates[i].name;
        if (strcmp(b, name) == 0)  {

         printf("no.\n");
         candidates[i].votes +=1;
         return true;
         }
    }
    return false;}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int a;
    int w = 0;
    for (a = 0; a < candidate_count; a++) {
        candidate n = candidates[a];
        //printf("%d\n", n.votes);
        candidate m = candidates[a+1];
        if (n.votes > m.votes) {
            if (n.votes > w){
                w = n.votes;
            }
        }
        else {
            if (m.votes > w){
                w = m.votes;
            }

        }
    }
    int q=0;
    int in = 0;
    string x[MAX];
    while (q<MAX) {
        if (candidates[q].votes == w) {
            x[in] = candidates[q].name;
            in++;
        }
        q++;
    }
    for (int j = 0; j < in; j++){
        string winname = x[j];
        printf("%s\n", winname);
    }


    printf("%d\n", w);
    return;
}