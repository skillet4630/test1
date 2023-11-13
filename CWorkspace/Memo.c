#include <stdio.h>
main(void)
{
    printf("for 반복문 예제1 : ");

    int i;
    for (i=0; i<10; ++i)
    {
        printf("%d", i);
    }
    printf("\n");

    printf("for 반복문 예제2 : ");

    for(int j=0; j<5; ++j)
    {
        printf("%d", j);
    }

    return 0;
}