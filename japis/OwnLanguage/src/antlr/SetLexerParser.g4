parser grammar SetLexerParser;
options { tokenVocab=SetLexer; }

program
    : (statement)* EOF
    ;

funcDef
    : DEF ID parameters block
    ;

parameters
    : OPEN_PAREN typedargslist? CLOSE_PAREN
    ;

typedargslist
    : ID (COMMA ID)*
    ;

block
    : INDENT statement+ DEDENT
    ;

statement
    : simple_statement
    | compound_statement
    ;

simple_statement
    : expr_statement
    | flow_statement
    ;

expr_statement
    : test (ASSIGN test)*
    ;

flow_statement
    : BREAK
    | CONTINUE
    | RETURN testlist?
    ;

compound_statement
    : if_statement
    | while_statement
    | for_statement
    | funcDef
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

test
    : or_test
    ;

or_test
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
    | UNION
    | DIFFERENCE
    | INTERSECTION
    | SYMMETRIC_DIFFERENCE
    ;

expr
    : set_operation              
    | functionCall               
    | atom                       
    ;

set_operation
    : atom (UNION atom | INTERSECTION atom | DIFFERENCE atom | SYMMETRIC_DIFFERENCE atom)*
    ;

atom
    : ID
    | NUMBER
    | STRING+
    | NONE
    | TRUE
    | FALSE
    ;

functionCall
    : ID (DOT ID)? OPEN_PAREN arglist? CLOSE_PAREN
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
