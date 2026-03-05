#!/usr/bin/env python3
"""
RC_Calculadora - Versión simplificada
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from gramaticas.CalculadoraLexer import CalculadoraLexer
from gramaticas.CalculadoraParser import CalculadoraParser
from src.visitante_evaluador import VisitanteEvaluador

def ejecutar(texto):
    """Ejecuta código RC"""
    # Asegurar que termina con newline
    if not texto.endswith('\n'):
        texto += '\n'
    
    # Lexer y parser
    input_stream = InputStream(texto)
    lexer = CalculadoraLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CalculadoraParser(tokens)
    
    # Parsear
    arbol = parser.programa()
    
    # Evaluar
    visitante = VisitanteEvaluador()
    visitante.visit(arbol)

def main():
    if len(sys.argv) > 1:
        # Ejecutar archivo
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            contenido = f.read()
        ejecutar(contenido)
    else:
        # Modo interactivo
        print("RC_Calculadora - Modo interactivo")
        print("Escribe 'salir' para terminar")
        while True:
            try:
                linea = input("rc> ")
                if linea.lower() in ('salir', 'exit', 'quit'):
                    break
                ejecutar(linea)
            except KeyboardInterrupt:
                print("\nAdiós")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
