#!/usr/bin/env python3
"""
Pruebas unitarias para RC_Calculadora
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.rc_calculadora import RCCalculadora
import io
import contextlib

def probar(codigo, esperado=None):
    """
    Ejecuta código y captura salida
    """
    calc = RCCalculadora()
    f = io.StringIO()
    
    with contextlib.redirect_stdout(f):
        calc.ejecutar_codigo(codigo)
    
    salida = f.getvalue().strip()
    
    if esperado is not None:
        assert esperado in salida, f"Esperado '{esperado}', obtenido '{salida}'"
    
    print(f"✅ {codigo.strip()} -> {salida}")
    return salida

def pruebas_unitarias():
    """
    Suite de pruebas
    """
    print("=" * 50)
    print("PRUEBAS UNITARIAS RC_CALCULADORA")
    print("=" * 50)
    
    # Operaciones básicas
    probar("3 + 4\n", "7")
    probar("10 - 3\n", "7")
    probar("6 * 7\n", "42")
    probar("15 / 3\n", "5.0")
    probar("2 ^ 3\n", "8")
    probar("(2 + 3) * 4\n", "20")
    
    # Variables
    probar("val x = 5\n x + 3\n", "8")
    probar("var y = 10\ny = y - 2\ny\n", "8")
    
    # Precedencia
    probar("3 + 4 * 2\n", "11")
    probar("(3 + 4) * 2\n", "14")
    probar("2 ^ 3 ^ 2\n", "512")  # derecha a izquierda
    
    # Decimales
    probar("3.14 * 2\n", "6.28")
    
    # Unarios
    probar("-5 + 3\n", "-2")
    
    # Expresiones complejas
    probar("val a = 5\nval b = 3\n(a + b) * (a - b)\n", "16")
    
    print("=" * 50)
    print("✅ Todas las pruebas pasaron")
    print("=" * 50)

if __name__ == "__main__":
    pruebas_unitarias()
