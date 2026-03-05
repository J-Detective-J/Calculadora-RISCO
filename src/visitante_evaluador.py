#!/usr/bin/env python3
"""
Visitante evaluador para RC_Calculadora
"""

from antlr4 import *
from gramaticas.CalculadoraParser import CalculadoraParser
from gramaticas.CalculadoraVisitor import CalculadoraVisitor

class VisitanteEvaluador(CalculadoraVisitor):
    """
    Visitante que evalúa expresiones y mantiene estado de variables
    """
    
    def __init__(self):
        self.memoria = {}  # diccionario para variables
        
    # Programa
    def visitPrograma(self, ctx: CalculadoraParser.ProgramaContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return None
    
    # Sentencias
    def visitDeclaracion_variable(self, ctx: CalculadoraParser.Declaracion_variableContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        
        if ctx.getChild(0).getText() == 'val':
            # Inmutable - solo permitir si no existe
            if nombre in self.memoria:
                raise Exception(f"Error: '{nombre}' ya está definida como val")
            self.memoria[nombre] = valor
        else:  # var
            self.memoria[nombre] = valor
        return valor
    
    def visitAsignacion(self, ctx: CalculadoraParser.AsignacionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        
        if nombre not in self.memoria:
            raise Exception(f"Error: Variable '{nombre}' no definida")
        self.memoria[nombre] = valor
        return valor
    
    def visitExpresion_stmt(self, ctx: CalculadoraParser.Expresion_stmtContext):
        resultado = self.visit(ctx.expresion())
        print(f"> {resultado}")
        return resultado
    
    # Expresiones
    def visitExpresion(self, ctx: CalculadoraParser.ExpresionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.termino(0))
        
        resultado = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            operador = ctx.getChild(2*i - 1).getText()
            valor = self.visit(ctx.termino(i))
            
            if operador == '+':
                resultado += valor
            elif operador == '-':
                resultado -= valor
        return resultado
    
    def visitTermino(self, ctx: CalculadoraParser.TerminoContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor(0))
        
        resultado = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            operador = ctx.getChild(2*i - 1).getText()
            valor = self.visit(ctx.factor(i))
            
            if operador == '*':
                resultado *= valor
            elif operador == '/':
                if valor == 0:
                    raise Exception("Error: División por cero")
                resultado /= valor
            elif operador == '%':
                resultado %= valor
        return resultado
    
    def visitFactor(self, ctx: CalculadoraParser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.potencia(0))
        
        resultado = self.visit(ctx.potencia(0))
        for i in range(1, len(ctx.potencia())):
            operador = ctx.getChild(2*i - 1).getText()
            valor = self.visit(ctx.potencia(i))
            
            if operador == '^':
                resultado = resultado ** valor
        return resultado
    
    def visitPotencia(self, ctx: CalculadoraParser.PotenciaContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primario())
        # recursión para asociatividad derecha
        return self.visit(ctx.primario(0)) ** self.visit(ctx.potencia())
    
    def visitPrimario(self, ctx: CalculadoraParser.PrimarioContext):
        if ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        
        if ctx.DECIMAL():
            return float(ctx.DECIMAL().getText())
        
        if ctx.IDENTIFICADOR():
            nombre = ctx.IDENTIFICADOR().getText()
            if nombre not in self.memoria:
                raise Exception(f"Error: Variable '{nombre}' no definida")
            return self.memoria[nombre]
        
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expresion())
        
        if ctx.getChild(0).getText() == '-':
            return -self.visit(ctx.primario())
        
        if ctx.getChild(0).getText() == '!':
            valor = self.visit(ctx.primario())
            return 1 if valor == 0 else 0  # not lógico
        
        return None
