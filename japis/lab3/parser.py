import sys
from antlr4 import *
from XMLLangLexer import XMLLangLexer
from XMLLangParser import XMLLangParser
from antlr4.error.ErrorListener import ConsoleErrorListener
from semantic_analizer import SemanticAnalyzer, SemanticError


class CustomErrorListener(ConsoleErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"\033[31mОшибка на строке {line}:{column} - {msg}\033[0m")



def main(input_file):
    input_stream = FileStream(input_file, encoding='utf-8') 
    lexer = XMLLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = XMLLangParser(stream)  

    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    tree = parser.program()  
    
    semantic_analyzer = SemanticAnalyzer()
    try:
        semantic_analyzer.analyze(tree)
    except SemanticError as e:
        print(f"Semantic error: {e}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Используйте: python parser.py <имя_входного_файла>")
