grammar XMLLang;

program
    : (
        statement | funcDef
    )* EOF
    ;

funcDef
    : DEF ID parameters block
    ;

parameters
    : OPEN_PAREN typedargslist? CLOSE_PAREN
    ;

typedargslist
    : ID (COMMA ID ?)*
    ;

block
    : INDENT statement+ DEDENT
    ;
    
statement
    : simple_statements
    | compound_statement
    ;
    
simple_statements
    : simple_statement (SEMI_COLON simple_statement)* SEMI_COLON?
    ;
    
simple_statement
    : (
        expr_statement
        | flow_statement
    )
    ;
    
expr_statement
    : testlist_star_expr (ASSIGN testlist_star_expr)*
    ;
    
testlist_star_expr
    : test (COMMA test)* COMMA?
    ;
    
flow_statement
    : BREAK
    | CONTINUE
    | RETURN testlist?
    | RAISE test?
    ;
    
compound_statement
    : if_statement
    | while_statement
    | for_statement
    | try_statement
    | funcDef
    | switch_statement
    ;
    
if_statement
    : IF test block (ELSE block)?
    ;

while_statement
    : WHILE test block
    ;

for_statement
    : FOR exprlist IN testlist block
    ;

try_statement
    : (
        TRY block (
            (except_clause block)+ (FINALLY block)?
            | FINALLY block
        )
    )
    ;

except_clause
    : EXCEPT test?
    ;

switch_statement
    : SWITCH test INDENT case_block+ DEDENT
    ;

case_block
    : CASE pattern block
    ;

pattern
    : closed_pattern+
    ;

closed_pattern
    : literal_pattern
    | value_pattern
    ;

literal_pattern
    : NUMBER
    | STRING+
    | NONE
    | TRUE
    | FALSE
    ;

value_pattern
    : attr
    ;

attr
    : ID (DOT ID)*
    ;
    
test
    : and_test (OR and_test)*
    ;

and_test
    : not_test (AND not_test)*
    ;

not_test
    : NOT not_test
    | comparison
    ;

comparison
    : expr (comp_op expr)*
    ;

comp_op
    : EQUALS
    | NOT_EQ_2
    | IN
    | NOT IN
    ;

expr
    : atom_expr
    ;

atom_expr
    : atom trailer*
    ;

atom
    : ID
    | NUMBER
    | STRING+
    | NONE
    | TRUE
    | FALSE
    ;

trailer
    : OPEN_PAREN arglist? CLOSE_PAREN
    | OPEN_BRACK test CLOSE_BRACK
    | DOT ID
    ;

exprlist
    : expr (COMMA expr)* COMMA?
    ;

testlist
    : test (COMMA test)* COMMA?
    ;

arglist
    : argument (COMMA argument)* COMMA?
    ;

argument
    : test
    ;

INDENT : '{';
DEDENT : '}';

STRING: '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f"])* '"';

NUMBER: DECIMAL_INTEGER;

AND        : 'and';
BREAK      : 'break';
CASE       : 'case';
CONTINUE   : 'continue';
DEF        : 'def';
ELSE       : 'else';
EXCEPT     : 'except';
FALSE      : 'False';
FINALLY    : 'finally';
FOR        : 'for';
IF         : 'if';
IN         : 'in';
SWITCH     : 'switch';
NONE       : 'None';
NOT        : 'not';
OR         : 'or';
RAISE      : 'raise';
RETURN     : 'return';
TRUE       : 'True';
TRY        : 'try';
WHILE      : 'while';

WS: [ \t\n\r\f]+ -> skip ;

NEWLINE: SPACES | ( '\r'? '\n' | '\r' | '\f') SPACES?;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;

DECIMAL_INTEGER: NON_ZERO_DIGIT DIGIT* | '0'+;

DOT                : '.';
OPEN_PAREN         : '(' {this.openBrace();};
CLOSE_PAREN        : ')' {this.closeBrace();};
OPEN_BRACK         : '[' {this.openBrace();};
CLOSE_BRACK        : ']' {this.closeBrace();};
COMMA              : ',';
COLON              : ':';
SEMI_COLON         : ';';
ASSIGN             : '=';
ADD                : '+';
MINUS              : '-';
EQUALS             : '==';
NOT_EQ_2           : '!=';


UNKNOWN_CHAR: .;

fragment STRING_ESCAPE_SEQ: '\\' . | '\\' NEWLINE;

fragment NON_ZERO_DIGIT: [1-9];

fragment DIGIT: [0-9];

fragment SPACES: [ \t]+;

fragment COMMENT: '#' ~[\r\n\f]*;

