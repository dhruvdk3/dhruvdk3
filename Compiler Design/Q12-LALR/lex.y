%{
#include<stdio.h>
#include<stdlib.h>
int yylex();
int yydebug=0;
void yyerror(char *s)
{
printf("Error %s",s);
}
%}

%token NUMBER
%left '+' '-'
%left '*' '/'

%%
S:E	{ printf("The Result is %d\n",$1); }
;
E:E'+'T		{ $$ = $1+$3; }
|E'-'T		{ $$ = $1+$3; }
|T		{ $$ = $1; }
;
T:T'*'F		{ $$ = $1+$3; }
|T'/'F		{ $$ = $1+$3; }
|F		{ $$ = $1; }
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