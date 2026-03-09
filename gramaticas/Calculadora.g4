grammar Calculadora;

@parser::members {
    # Memoria para variables
    memoria = {}
}

// Programa principal - acepta saltos de línea entre sentencias
programa: (NL* sentencia NL*)* EOF;

// Sentencias
sentencia
    : declaracion_variable
    | asignacion
    | expresion_stmt
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

// Saltos de línea
NL : ('\r'? '\n')+;

// Espacios en blanco
WS : [ \t]+ -> skip;

// Comentarios
COMENTARIO_LINEA : '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE : '/-' .*? '-/' -> skip;
COMENTARIO_DOC : '///' ~[\r\n]* -> skip;
