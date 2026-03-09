source venv/bin/activate

echo "Generando con ANTLR 4"

# Limpiar
rm -f gramaticas/Calculadora*.py

# Generar
java -jar /usr/local/lib/antlr-4.13.2-complete.jar \
    -Dlanguage=Python3 \
    -visitor \
    -no-listener \
    -o generado \
    gramaticas/Calculadora.g4

# Mover
cp generado/gramaticas/*.py gramaticas/
touch gramaticas/__init__.py
rm -rf generado

echo "Listo"
ls -la gramaticas/Calculadora*.py
