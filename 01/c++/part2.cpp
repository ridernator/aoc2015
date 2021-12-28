#include <stdlib.h>
#include <stdio.h>

#define INPUT "../data/input"

int main() {
    int floor=0;

    // Open file
    FILE* fptr;
    if ((fptr = fopen(INPUT, "r")) == NULL) {
        fprintf(stderr, "Error opening file \"%s\"\n", INPUT);
        exit(EXIT_FAILURE);
    }

    // Read each char in file
    char c;
    int index = 0;
    while ((c = fgetc(fptr)) != EOF) {
        if (c == '(') {
            ++floor;
        } else if (c == ')') {
            --floor;
        }

        ++index;

        if (floor == -1) {
            break;
        }
    }

    fclose(fptr);

    fprintf(stdout, "Got to the basement at character %i\n", index);

    return 0;
}