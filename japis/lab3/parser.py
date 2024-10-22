import sys
from antlr4 import *
from XMLLangLexer import XMLLangLexer  # Lexer
from XMLLangParser import XMLLangParser  # Parser
from antlr4.error.ErrorListener import ConsoleErrorListener

# Custom error listener to print syntax errors
class CustomErrorListener(ConsoleErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # ANSI escape code for red text: \033[31m
        # Reset color to default: \033[0m
        print(f"\033[31mОшибка на строке {line}:{column} - {msg}\033[0m")

def main(input_file):
    input_stream = FileStream(input_file, encoding='utf-8') 
    lexer = XMLLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = XMLLangParser(stream)  

    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    tree = parser.program()  
    print(tree.toStringTree(recog=parser))  

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Используйте: python parser.py <имя_входного_файла>")
