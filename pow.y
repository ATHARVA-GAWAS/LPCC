%{
#include <stdio.h>
#include <math.h>
%}

%token NUMBER POW LOG
%left '+' '-'
%left '*' '/'
%left POW LOG

%%
expression : expression '+' expression
           | expression '-' expression
           | expression '*' expression
           | expression '/' expression
           | POW '(' expression ',' expression ')'
           | LOG '(' expression ')'
           | NUMBER
           ;

%%

int yylex() {
    int c = getchar();
    if (isdigit(c)) {
        ungetc(c, stdin);
        scanf("%d", &yylval);
        return NUMBER;
    }
    if (c == '+') return '+';
    if (c == '-') return '-';
    if (c == '*') return '*';
    if (c == '/') return '/';
    if (c == '^') return POW;
    if (c == 'l' && getchar() == 'o' && getchar() == 'g') return LOG;
    return c;
}

int yyerror(char *s) {
    printf("Error: %s\n", s);
    return 0;
}

int main() {
    yyparse();
    return 0;
}
