%{
#include <stdio.h>
#include <ctype.h>
%}

%token IDENTIFIER
%token END

%%

input: /* empty */
     | input line
     ;

line: identifier END
    {
        printf("Valid variable name: %s\n", $1);
    }
    ;

identifier: [a-zA-Z][a-zA-Z0-9_]* 
    {
        yylval = strdup(yytext);
        return IDENTIFIER;
    }
    ;

%%

int yyerror(char *s) {
    fprintf(stderr, "Error: %s\n", s);
    return 0;
}

int main() {
    yyparse();
    return 0;
}
