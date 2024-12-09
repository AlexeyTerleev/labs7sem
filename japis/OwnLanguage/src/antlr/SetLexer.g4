lexer grammar SetLexer;

INDENT : '{';
DEDENT : '}';

STRING: '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f"])* '"';

NUMBER: DECIMAL_INTEGER;

AND        : 'and';
BREAK      : 'break';
CONTINUE   : 'continue';
DEF        : 'def';
ELSE       : 'else';
FALSE      : 'False';
FOR        : 'for';
IF         : 'if';
IN         : 'in';
NONE       : 'None';
NOT        : 'not';
OR         : 'or';
RETURN     : 'return';
TRUE       : 'True';
WHILE      : 'while';

WS: [ \t\n\r\f]+ -> skip ;

NEWLINE: SPACES | ( '\r'? '\n' | '\r' | '\f') SPACES?;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;

DECIMAL_INTEGER: NON_ZERO_DIGIT DIGIT* | '0'+;

DOT                : '.';
OPEN_PAREN         : '(' {self.openBrace();};
CLOSE_PAREN        : ')' {self.closeBrace();};
OPEN_BRACK         : '[' {self.openBrace();};
CLOSE_BRACK        : ']' {self.closeBrace();};
COMMA              : ',';
COLON              : ':';
SEMI_COLON         : ';';
ASSIGN             : '=';
UNION              : '+';
DIFFERENCE         : '-';
INTERSECTION       : '*';
SYMMETRIC_DIFFERENCE : '^';
EQUALS             : '==';
NOT_EQ_2           : '!=';

UNKNOWN_CHAR: .;

fragment STRING_ESCAPE_SEQ: '\\' . | '\\' NEWLINE;

fragment NON_ZERO_DIGIT: [1-9];

fragment DIGIT: [0-9];

fragment SPACES: [ \t]+;

fragment COMMENT: '#' ~[\r\n\f]*;