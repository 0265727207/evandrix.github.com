#include <stdio.h>

/* gcc -O3 -S -m32 hello.c; cat hello.s */

int foo_stupid()
{
    int i = 0;
    i = i + 1;
    return i;
}

main()
{
    foo_stupid();
}
