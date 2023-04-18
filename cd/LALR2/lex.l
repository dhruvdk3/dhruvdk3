%option noyywrap
%{
  #include "y.tab.h"
%}

%%
[0-9]+ {yylval=strtol(yytext,(char **)NULL, 10);
	return NUMBER;
	}
[\t]	;
\n	return 0;
.	return yytext[0];
%%