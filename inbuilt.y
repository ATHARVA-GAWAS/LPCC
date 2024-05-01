%{
#include <stdio.h>
#include <math.h>
#include <string.h>
extern double sqrt(double);
extern size_t strlen(const char *);
%}

%token NUMBER STRING SQRT STRLEN

%%

statement_list : statement '\n' statement_list
               | statement '\n'
               ;

statement : assignment
          | function_call
          ;

assignment : ID '=' expression
           {
               printf("%s = %f\n", $1, $3);
           }
           ;

function_call : ID '=' SQRT '(' expression ')'
              {
                  $$ = sqrt($5);
              }
              | ID '=' STRLEN '(' STRING ')'
              {
                  $$ = strlen($5);
              }
              ;

expression : NUMBER
           {
               $$ = $1;
           }
           ;

%%

int yywrap() { return 1; }

int main() {
    printf("Enter expressions (e.g., u = sqrt(36)):\n");
    yyparse();
    return 0;
}

int yyerror(char *s) {
    printf("error: %s\n", s);
    return 0;
}
