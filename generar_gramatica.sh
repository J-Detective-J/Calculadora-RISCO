#!/bin/zsh

# Script para generar código ANTLR
# Activar entorno virtual
source venv/bin/activate

# Directorios
GRAMATICA_DIR="gramaticas"
GENERADO_DIR="generado"

# Crear directorio temporal para generación
mkdir -p $GENERADO_DIR

# Generar lexer y parser
echo "Generando lexer y parser desde gramática..."
antlr4 -Dlanguage=Python3 -visitor -no-listener \
    -o $GENERADO_DIR \
    $GRAMATICA_DIR/Calculadora.g4

# Mover archivos generados al directorio de gramáticas
echo "Moviendo archivos generados..."
cp $GENERADO_DIR/gramaticas/*.py $GRAMATICA_DIR/

# Limpiar
rm -rf $GENERADO_DIR

# Crear archivo __init__.py
touch $GRAMATICA_DIR/__init__.py

echo "✅ Generación completada"
