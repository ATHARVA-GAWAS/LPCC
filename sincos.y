%{
#include <stdio.h>
#include <math.h>
%}

%token NUM
%token SIN COS
%token PLUS MINUS TIMES DIV LPAREN RPAREN

%left PLUS MINUS
%left TIMES DIV

%%

expression: expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIV expression
    | SIN LPAREN expression RPAREN    { $$ = sin($3); }
    | COS LPAREN expression RPAREN    { $$ = cos($3); }
    | LPAREN expression RPAREN
    | NUM                              { $$ = $1; }
    ;

%%

int yylex() {
    int c = getchar();
    if (c == '+' || c == '-' || c == '*' || c == '/' || c == '(' || c == ')')
        return c;
    if (c == 's' && getchar() == 'i' && getchar() == 'n' && getchar() == '(') {
        ungetc('(', stdin);
        return SIN;
    }
    if (c == 'c' && getchar() == 'o' && getchar() == 's' && getchar() == '(') {
        ungetc('(', stdin);
        return COS;
    }
    if (c == '\n' || c == EOF)
        return 0;
    if (c >= '0' && c <= '9') {
        ungetc(c, stdin);
        scanf("%lf", &yylval);
        return NUM;
    }
    return 0;
}

int main() {
    printf("Enter expression (end with newline):\n");
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
