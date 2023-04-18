%{
#include<stdio.h>
#include <stdlib.h>
int yylex();
int yydebug = 1;
void yyerror(char *str)
{
printf("Error ");		
}
%}
%token NUMBER
%left '+' '-'
%left '*' '/'
%%
S:E	{ printf("The result is : %d\n",$1);}
;
E:E'+'E		{ $$ = $1+$3; }
|E'-'E		{ $$ = $1-$3; }
|E'*'E		{ $$ = $1*$3; }
|E'/'E		{ $$ = $1/$3; }
|'-'E %prec '*' { $$ = -$2; }
|F	{ $$ = $1; }
;
F:'('E')'	{ $$ = $2; }
|NUMBER		{ $$ = $1; }
;
%%
int main()
{
	yyparse();
	return 0;
}