%{
#include <stdlib.h>
#include <stdio.h>

int a;
int b;
%}

%%

%%

int yywrap(){ return 1; }
/*	 After inputting press ctrl+d		 */

// MAIN FUNCTION
int main(){
    printf("Enter number 1 : ");
    scanf("%d" , &a);
    // a = yylex();
    printf("Enter number 2 : ");
    scanf("%d" , &b);
    // b = yylex();÷\
	yylex();
    printf("The sum is %d ",a+b);
	
	return 0;
}
