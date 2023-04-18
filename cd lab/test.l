%{

%}

%%
\n printf("Hello World ");
%%

int main(){
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}
