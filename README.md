# Calculadora-RISCO
Un lenguaje de dominio específico para cálculos matemáticos

Un lenguaje de dominio específico para cálculos matemáticos, implementado con ANTLR4 y Python.

## Características

- Variables inmutables (`val`) y mutables (`var`)
- Operaciones aritméticas básicas (+, -, *, /, %, ^)
- Comparaciones (==, !=, >, <, >=, <=)
- Operadores lógicos (&&, ||, !)
- Listas y comprensiones matemáticas
- Funciones built-in (print, length, sum, sqrt, map, filter, reduce)
- Pipelines con operador `|>`
- Comentarios de línea, documentación y bloque anidado

## Instalación


# Instalar dependencias
```
pip install -r requirements.txt
```

# Generar parser con ANTLR (si se modifica la gramática)
```
cd grammar
```
```
antlr4 -Dlanguage=Python3 -visitor -no-listener DSLcalculadora.g4
```
