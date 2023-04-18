%{
int c=0,v=0;
%}
%%
[aeiouAeiou] v++;
[A-Za-z] c++;
%%
main()
{
printf("Enter the string \n");
yylex();
printf("The number of vowels are %d \n",v);
printf("The number of consonants are %d \n",c);
}
/* flex Q1.l    gcc lex.yy.c ./a.out   Control D to terminate*/ 
