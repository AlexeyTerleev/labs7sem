from antlr.SetLexerParser import SetLexerParser

class CILGenerator:
    def __init__(self):
        self.cil_code = []
        self.indentation_level = 0

    def add_line(self, line):
        indent = "\t" * self.indentation_level
        self.cil_code.append(indent + line)

    def generate(self, ast):
        self.add_line('class Program')

        self.add_line("{")
        self.indentation_level += 1

        self.analyze(ast)

        self.indentation_level -= 1
        self.add_line("}")

        return "\n".join(self.cil_code)

    def analyze(self, node):
        """Рекурсивный метод для анализа узлов дерева."""
        method_name = f'analyze_{type(node).__name__}'
        analyze_method = getattr(self, method_name, self.generic_analyze)
        analyze_method(node)
    
    def generic_analyze(self, node):
        """Обработка по умолчанию для неизвестных узлов, рекурсивно обрабатывает дочерние узлы."""
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            self.analyze(child)

    def analyze_ProgramContext(self, node):
        for statement in node.statement():
            self.analyze(statement)

    def analyze_StatementContext(self, node):
        """Анализ оператора, который может быть простым или составным."""
        if node.simple_statement():
            self.analyze_Simple_statementContext(node.simple_statement())
        elif node.compound_statement():
            self.analize_Compound_statementContext(node.compound_statement())

    def analize_Compound_statementContext(self, node):
        """Анализ составного оператора."""

        if node.if_statement():
            self.analyze_If_statementContext(node.if_statement())
        elif node.while_statement():
            self.analyze_While_statementContext(node.while_statement())
        elif node.for_statement():
            self.analyze_For_statementContext(node.for_statement())
        elif node.funcDef():
            self.analyze_FuncDefContext(node.funcDef())

    def analyze_If_statementContext(self, node):
        cil_code = self.analyze_TestContext(node.test())
        self.add_line(f"if ({cil_code})")
        self.add_line("{")
        self.indentation_level += 1

        self.analyze_BlockContext(node.block(0))

        self.indentation_level -= 1
        self.add_line("}")


    def analyze_For_statementContext(self, node):
        """Анализ конструкции for."""
        cil_code = f'var {node.exprlist().getText()} in {node.testlist().getText()}'
        self.add_line(f"foreach ({cil_code})")
        self.add_line("{")
        self.indentation_level += 1

        self.analyze_BlockContext(node.block())

        self.indentation_level -= 1
        self.add_line("}")
    
    def analyze_TestContext(self, node):
            return self.analyze_Or_testContext(node.or_test())

    def analyze_Or_testContext(self, node):
        for and_test in node.and_test():
            return self.analyze_And_testContext(and_test)

    def analyze_And_testContext(self, node):
        for not_test in node.not_test():
            return self.analyze_Not_testContext(not_test)

    def analyze_Not_testContext(self, node):
        if node.NOT():
            return self.analyze_Not_testContext(node.not_test())
        else:
            return self.analyze_ComparisonContext(node.comparison())

    def analyze_ComparisonContext(self, node):
        left_expr = node.expr(0)
        right_expr = node.expr(1) if node.expr(1) else None

        if left_expr.functionCall():
            cil_code = self.analyze_FunctionCallContext(left_expr.functionCall()).rstrip(';')
        else:
            cil_code = left_expr.getText()

        if node.comp_op():
            comp_op = node.comp_op(0).getText()
            cil_code += f' {comp_op} '
            if right_expr.functionCall():
                cil_code += self.analyze_FunctionCallContext(right_expr.functionCall()).rstrip(';')
            else:
                cil_code += right_expr.getText()
            return cil_code
        else:
            return cil_code

    def analyze_Simple_statementContext(self, node):
        """Анализ простого выражения."""
        if node.expr_statement():
            self.analyze_Expr_statementContext(node.expr_statement())
        elif node.flow_statement():
            self.analyze_Flow_statementContext(node.flow_statement())

    def analyze_Flow_statementContext(self, node):
        self.add_line(f'return {node.testlist().getText()};')

    def analyze_FuncDefContext(self, node):
        """Анализ определения функции."""
        func_name = node.ID().getText()
        params = node.parameters()

        if params.typedargslist():
            params = params.typedargslist().getText().split(',')
            params = [param.strip() for param in params]
        else:
            params = []

        if params:
            param_str = ', '.join([f'dynamic {param}' for param in params])
        else:
            param_str = ''
        
        type_of_func = 'void' if func_name == 'main' else 'dynamic'
        self.add_line(f"static {type_of_func} {func_name.capitalize()}({param_str})")
        
        self.add_line("{")
        self.indentation_level += 1

        self.analyze_BlockContext(node.block())

        self.indentation_level -= 1
        self.add_line("}")

    def analyze_BlockContext(self, node):
        """Анализ блока кода."""
        for statement in node.statement():
            self.analyze_StatementContext(statement)

    def analyze_Expr_statementContext(self, node):
        """Анализ выражений, включая присваивание и операции с множествами."""

        left_var = node.test(0)
        left_var_name = left_var.getText()

        if len(node.test()) > 1 and node.getChild(1).getText() == '=':
            right_var = node.test(1)
            expr_node = self.find_expr_node(right_var)

            function_call_node = expr_node.functionCall()
            if function_call_node is not None:
                type_of_var = function_call_node.ID(0).getText()
                if type_of_var == 'Set':
                    self.add_line(f'HashSet<string> {left_var_name} = new HashSet<string>();')
                elif type_of_var == 'Element':
                    arg = function_call_node.arglist().getChild(0).getText()
                    self.add_line(f'string {left_var_name} = {arg};')
                else:
                    self.add_line(f'HashSet<string> {left_var_name} = {function_call_node.getText().capitalize()};')

            set_operation_node = expr_node.set_operation()
            if set_operation_node is not None:
                operation = self.analyze_Set_operationContext(set_operation_node, left_var_name)
                if operation is not None:
                    new_set = f'HashSet<string> {left_var_name} = new HashSet<string>({operation});'
                    self.add_line(new_set)

        else:
            expr_node = self.find_expr_node(left_var)
            function_call_node = expr_node.functionCall()
            if function_call_node:
                cil_code = self.analyze_FunctionCallContext(function_call_node)
                if cil_code:
                    self.add_line(cil_code)

    def analyze_Set_operationContext(self, node, left_var_name = None):
        """Анализирует операцию с множествами и генерирует CIL код с использованием HashSet<T>."""
        set_exprs = node.atom()
        sets = []
        for i in range(0, len(set_exprs)):
            current_var = set_exprs[i].getText()
            sets.append(current_var)

        operation_text = node.getText()

        if '+' in operation_text:
            operation = 'Union'
        elif '-' in operation_text:
            operation = 'Except'
        elif '*' in operation_text:
            operation = 'Intersect'
        else:
            self.add_line(f'HashSet<string> {left_var_name} = new HashSet<string>({sets[0]});')
            self.add_line(f'{left_var_name}.SymmetricExceptWith({sets[1]});')
            return None

        cil_code = f'{sets[0]}.{operation}({sets[1]})'
        return cil_code


    def analyze_FunctionCallContext(self, node):
        """Анализ вызова метода для объектов типа 'Set'."""
        obj_name = node.ID(0).getText()
        func_name = node.getChild(2).getText()

        if obj_name == "print":
            cil_code = ''
            if node.arglist():
                args = node.arglist().getChildren()
                for arg in args:
                    if arg.getText() == ',':
                        continue
                    expr_node = self.find_expr_node(arg.test())
                    if expr_node:
                        function_call_node = expr_node.functionCall()
                        if function_call_node:
                            cil_code += self.analyze_FunctionCallContext(function_call_node).rstrip(';') + ' + '
                        else:
                            cil_code += arg.getText()  + ' + '
                    else:
                        cil_code += arg.getText()  + ' + '
                    
                cil_code = cil_code.rstrip(' + ')
                self.add_line(f'Console.WriteLine({cil_code});')

        else:
            if func_name == "add":
                arg = node.arglist().getChild(0).getText()
                cil_code = f'{obj_name}.Add({arg});'

            elif func_name == "remove":
                arg = node.arglist().getChild(0).getText()
                cil_code = f'{obj_name}.Remove({arg});'

            elif func_name == "contains":
                arg = node.arglist().getChild(0).getText()
                cil_code = f'{obj_name}.Contains({arg});'

            elif func_name == "clear":
                cil_code = f'{obj_name}.Clear();'

            elif func_name == "size":
                cil_code = f'{obj_name}.Count;'
            return cil_code
        

    def find_expr_node(self, node):
        """Рекурсивный метод для поиска узла типа expr в дереве синтаксического разбора."""
        if isinstance(node, SetLexerParser.ExprContext):
            return node
        elif isinstance(node, SetLexerParser.TestContext):
            return self.find_expr_node(node.or_test())
        elif isinstance(node, SetLexerParser.Or_testContext):
            if node.and_test():
                return self.find_expr_node(node.and_test(0))
        elif isinstance(node, SetLexerParser.And_testContext):
            if node.not_test():
                return self.find_expr_node(node.not_test(0))
        elif isinstance(node, SetLexerParser.Not_testContext):
            if node.comparison():
                return self.find_expr_node(node.comparison())
        elif isinstance(node, SetLexerParser.ComparisonContext):
            if node.expr():
                return self.find_expr_node(node.expr(0))

        return None