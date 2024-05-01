%{

#include <stdio.h>

%}

%%

"^[A-Z][a-zA-Z]*$"      { printf("NOUN: %s\n", yytext); }
"[a-zA-Z]+ing$"         { printf("VERB (Gerund): %s\n", yytext); }
"[a-zA-Z]+ed$"          { printf("VERB (Past tense): %s\n", yytext); }
"[a-zA-Z]+s$"           { printf("NOUN (Plural): %s\n", yytext); }
"^[0-9]+$"              { printf("NUMBER: %s\n", yytext); }
"."                     { /* Ignore other characters */ }
\n                      { /* Ignore newlines */ }

%%

int main() {
    
    yylex();
    return 0;
}
