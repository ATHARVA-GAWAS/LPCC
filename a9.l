%{
#include <stdio.h>
%}

%%
"{"            { printf("<LBRACE>\n"); }
"}"            { printf("<RBRACE>\n"); }
"="            { printf("<ASSIGN>\n"); }
"int"         { printf("<INT>\n"); }
[0-9]+         { printf("<NUMBER>\n"); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("<ID>\n"); }
[-+*/]         { printf("<OPERATOR>\n"); }
[\n\t ]+       { /* ignore whitespace and newline */ }
.              { printf("Unknown token\n"); }
%%

int main() {
    yyin = fopen("input.txt", "r");
    yylex();
    fclose(yyin);
    return 0;
}



