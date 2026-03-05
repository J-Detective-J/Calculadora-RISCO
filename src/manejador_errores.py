import sys
from antlr4.error.ErrorListener import ErrorListener

class ManejadorErrores(ErrorListener):
    """
    Manejador personalizado para errores de sintaxis
    """
    
    def __init__(self):
        super().__init__()
        self.tiene_error = False
        
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.tiene_error = True
        mensaje = f"Error sintáctico línea {line}:{column} - {msg}"
        print(mensaje, file=sys.stderr)
        
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass
        
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass
        
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass
