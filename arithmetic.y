%{
#include <stdio.h>
#include <stdlib.h>
%}

%token NUMBER
%left '+' '-'
%left '*' '/'

%%
input: expr { printf("Result: %f\n", $1); }
     ;

expr: expr '+' expr   { $$ = $1 + $3; }
    | expr '-' expr   { $$ = $1 - $3; }
    | expr '*' expr   { $$ = $1 * $3; }
    | expr '/' expr   { $$ = $1 / $3; }
    | '(' expr ')'    { $$ = $2; }
    | NUMBER          { $$ = $1; }
    ;

%%

int yylex() {
    char c = getchar();
    if (c == EOF) return 0;
    if (c == '+' || c == '-' || c == '*' || c == '/' || c == '(' || c == ')') return c;
    if (c >= '0' && c <= '9') {
        ungetc(c, stdin);
        scanf("%lf", &yylval);
        return NUMBER;
    }
    return 0;
}

int main() {
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
