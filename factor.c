#include "factor.h"

/**
 * main - main is fun
 *
 *
 *
 * Return: void
 */
int main(int argc, char *argv[])
{
FILE *fptr;
size_t couunt;
ssize_t line;
char *buffer = NULL;


if (argc != 2)
{
fprintf(stderr, "Usage: factor <filename>\n");
exit(EXIT_FAILURE);
}
fptr = fopen(argv[1], "r");
if (fptr == NULL)
{
fprintf(stderr, "Error: can't open file %s\n", argv[1]);
exit(EXIT_FAILURE);
}
while((line = getline(&buffer, &couunt, fptr)) != -1)
{
factorisze(buffer);
}
return (0);
}
