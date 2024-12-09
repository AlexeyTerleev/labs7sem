import sys
import os
from antlr4 import *
from antlr.SetLexer import SetLexer
from antlr.SetLexerParser import SetLexerParser
from semantic_analyzer.core import SemanticAnalyzer, SemanticError
from cil_generator.core import CILGenerator


def main(input_file):
    input_stream = FileStream(input_file)
    lexer = SetLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SetLexerParser(stream)

    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    semantic_analyzer = SemanticAnalyzer()
    
    try:
        semantic_analyzer.analyze(tree)
        print("Семантический анализ завершен успешно, ошибок не найдено.")
    except SemanticError as e:
        print(f"Семантическая ошибка: {e}")
        return

    cil_generator = CILGenerator()
    cil_generator.generate(tree)

    cil_code = "\n".join(cil_generator.cil_code)

    output_dir = "/home/user/OwnLanguage/src/compiled_code"
    output_name = "Program.cs"  

    output_path = os.path.join(output_dir, output_name)
    with open(output_path, "w") as f:
        f.write(cil_code)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python main.py <input_file>")