#!/usr/bin/env python3
"""
RC_Calculadora - Lenguaje DSL para cálculos matemáticos
"""

import sys
import os
import argparse

# Asegurar que podemos importar desde el directorio padre
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener
from gramaticas.CalculadoraLexer import CalculadoraLexer
from gramaticas.CalculadoraParser import CalculadoraParser
from src.visitante_evaluador import VisitanteEvaluador
from src.manejador_errores import ManejadorErrores

class RCCalculadora:
    """
    Intérprete principal de la calculadora
    """
    
    def __init__(self):
        self.visitante = VisitanteEvaluador()
        # NO definir un atributo llamado 'modo_interactivo' aquí
        # Eso causaría que el método sea sobrescrito
        
    def ejecutar_archivo(self, ruta_archivo):
        """
        Ejecuta un archivo .rc
        """
        try:
            # Leer archivo
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                codigo = f.read()
            
            # Ejecutar código
            self._ejecutar_codigo(codigo, ruta_archivo)
            
        except FileNotFoundError:
            print(f"Error: No se encuentra el archivo '{ruta_archivo}'")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    def _ejecutar_codigo(self, codigo, fuente="<entrada>"):
        """
        Ejecuta código fuente directamente (método interno)
        """
        # Configurar entrada
        entrada = InputStream(codigo)
        
        # Lexer
        lexer = CalculadoraLexer(entrada)
        lexer.removeErrorListener(ConsoleErrorListener.INSTANCE)
        
        # Token stream
        tokens = CommonTokenStream(lexer)
        
        # Parser
        parser = CalculadoraParser(tokens)
        parser.removeErrorListener(ConsoleErrorListener.INSTANCE)
        
        # Añadir manejador de errores personalizado
        manejador = ManejadorErrores()
        parser.addErrorListener(manejador)
        lexer.addErrorListener(manejador)
        
        # Parsear
        try:
            arbol = parser.programa()
        except Exception as e:
            print(f"Error durante el parseo: {e}")
            return
        
        if manejador.tiene_error:
            return
        
        # Evaluar
        try:
            self.visitante.visit(arbol)
        except Exception as e:
            print(f"Error en evaluación: {e}")
    
    def modo_interactivo(self):
        """
        Modo REPL (Read-Eval-Print Loop) interactivo
        """
        print("RC_Calculadora v1.0 - Modo interactivo")
        print("Escribe expresiones o 'salir' para terminar")
        print("Ejemplos: val x = 5, 3 + 4 * 2, x ^ 2")
        print("-" * 50)
        
        historial = []
        
        while True:
            try:
                # Leer línea
                linea = input("rc> ").strip()
                
                if not linea:
                    continue
                
                if linea.lower() in ('salir', 'exit', 'quit'):
                    break
                
                # Guardar en historial
                historial.append(linea)
                
                # Añadir newline si no tiene
                if not linea.endswith('\n'):
                    linea += '\n'
                
                # Ejecutar
                self._ejecutar_codigo(linea)
                
            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego!")
                break
            except EOFError:
                print("\n\n👋 ¡Hasta luego!")
                break
            except Exception as e:
                print(f"Error: {e}")

def main():
    """
    Punto de entrada principal
    """
    parser = argparse.ArgumentParser(
        description="RC_Calculadora - Lenguaje DSL para cálculos matemáticos"
    )
    parser.add_argument(
        'archivo',
        nargs='?',
        help="Archivo .rc a ejecutar"
    )
    parser.add_argument(
        '--version',
        action='version',
        version='RC_Calculadora 1.0'
    )
    parser.add_argument(
        '--prueba',
        action='store_true',
        help="Ejecutar pruebas rápidas"
    )
    
    args = parser.parse_args()
    
    calc = RCCalculadora()
    
    if args.prueba:
        # Ejecutar pruebas rápidas
        pruebas = [
            "3 + 4",
            "10 - 3",
            "6 * 7",
            "15 / 3",
            "2 ^ 3",
            "val x = 5\nx + 3"
        ]
        print("=== PRUEBAS RÁPIDAS ===")
        for expr in pruebas:
            print(f"\n▶ {expr}")
            calc._ejecutar_codigo(expr + "\n")
    elif args.archivo:
        calc.ejecutar_archivo(args.archivo)
    else:
        calc.modo_interactivo()

if __name__ == "__main__":
    main()
