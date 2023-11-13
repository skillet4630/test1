#include <stdio.h>
main(void)
{
    char op;
    int a, b;

    printf("===계산기 프로그램=== \n");
    printf("계산식을 입력하세요.(예: 3+3) \n");
    scanf("%d %c %d", &a, &op, &b);

    if(op=='+') printf("\n%d", a+b);
    else if(op=='-') printf("\n%d", a-b);
    else if(op=='*') printf("\n%d", a*b);
    else if(op=='/') printf("\n%d", a/b);
    else printf("\n잘못입력하셨습니다.");

    return 0;
}