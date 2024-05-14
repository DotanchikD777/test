#include <stdio.h>

int main(int argc, char* argv[])
{
    printf("%s", "hello world!\n");


    for(int i = 1; i < argc; i++)
    {
        printf("Your [%d] argument: %s\n", i, argv[i]);
    } 

    return 0;
}