grammar Calculadora;

@header {
from enum import Enum
}

@parser::members {
    # Memoria para variables
    memoria = {}
}

// Programa principal
programa: (sentencia)+ EOF;

// Sentencias
sentencia
    : declaracion_variable
    | expresion_stmt
    | asignacion
    ;

declaracion_variable
    : 'val' IDENTIFICADOR '=' expresion NL
    | 'var' IDENTIFICADOR '=' expresion NL
    ;

asignacion
    : IDENTIFICADOR '=' expresion NL
    ;

expresion_stmt
    : expresion NL
    ;

// Expresiones con precedencia (de menor a mayor)
expresion
    : termino (('+' | '-') termino)*
    ;

termino
    : factor (('*' | '/' | '%') factor)*
    ;

factor
    : potencia ('^' potencia)*
    ;

potencia
    : primario
    | primario '^' potencia  // asociativo derecha
    ;

primario
    : NUMERO
    | DECIMAL
    | IDENTIFICADOR
    | '(' expresion ')'
    | '-' primario  // negativo unario
    | '!' primario  // not lógico
    ;

// Tokens léxicos
NUMERO : DIGITO+;
DECIMAL : DIGITO+ '.' DIGITO+;
IDENTIFICADOR : LETRA (LETRA | DIGITO | '_')*;

// Fragmentos
fragment LETRA : [a-zA-ZáéíóúñÁÉÍÓÚÑ];
fragment DIGITO : [0-9];

// Espacios y nuevas líneas
NL : ('\r'? '\n')+;
WS : [ \t]+ -> skip;

// Comentarios
COMENTARIO_LINEA : '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE : '/-' .*? '-/' -> skip;
COMENTARIO_DOC : '///' ~[\r\n]* -> skip;
