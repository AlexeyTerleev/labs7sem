from antlr.SetLexerParser import SetLexerParser


class SemanticError(Exception):
    """Класс для семантических ошибок."""
    def __init__(self, message):
        super().__init__(message)

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_tables = [{}]
        self.function_table = {}
        self.in_loop = 0
        self.in_function = False

    def enter_scope(self):
        """Создает новую таблицу символов для новой области видимости."""
        self.symbol_tables.append({})

    def exit_scope(self):
        """Удаляет последнюю таблицу символов при выходе из области видимости."""
        self.symbol_tables.pop()

    def current_scope(self):
        """Возвращает текущую таблицу символов."""
        return self.symbol_tables[-1]

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
        """Анализ основного блока программы."""
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


    def analyze_Simple_statementContext(self, node):
        """Анализ простого выражения."""
        if node.expr_statement():
            self.analyze_Expr_statementContext(node.expr_statement())
        elif node.flow_statement():
            self.analyze_Flow_statementContext(node.flow_statement())

    def analyze_FuncDefContext(self, node):
        """Анализ определения функции."""
        func_name = node.ID().getText()
        if func_name in self.function_table:
            raise SemanticError(f"Функция '{func_name}' уже объявлена.")
        
        self.enter_scope()
        self.in_function = True
        parameters = self.analyze_ParametersContext(node.parameters())
        self.function_table[func_name] = {'params': parameters, 'block': node.block()}
        self.analyze_BlockContext(node.block())
        self.exit_scope()
        self.in_function = False

    def analyze_ParametersContext(self, node):
        """Анализ параметров функции."""
        params = []
        if node.typedargslist():
            for param in node.typedargslist().ID():
                param_name = param.getText()
                if param_name in self.current_scope():
                    raise SemanticError(f"Параметр '{param_name}' уже объявлен.")
                
                params.append(param_name)
                self.current_scope()[param_name] = 'Set'
                
        return params

    def analyze_BlockContext(self, node):
        """Анализ блока кода."""
        for statement in node.statement():
            self.analyze_StatementContext(statement)

    def analyze_If_statementContext(self, node):
        """Анализ конструкции if."""
        self.analyze_TestContext(node.test())
        self.enter_scope()
        self.analyze_BlockContext(node.block(0))
        self.exit_scope()
        if node.ELSE():
            self.enter_scope()
            self.analyze_BlockContext(node.ELSE().block())
            self.exit_scope()

    def analyze_While_statementContext(self, node):
        """Анализ конструкции while."""
        self.analyze_TestContext(node.test())
        self.enter_scope()
        self.in_loop += 1
        self.analyze_BlockContext(node.block())
        self.exit_scope()
        self.in_loop -= 1

    def analyze_For_statementContext(self, node):
        """Анализ конструкции for."""
        self.analyze_TestlistContext(node.testlist())
        self.enter_scope()
        self.current_scope()[node.exprlist().getText()] = 'dynamic'
        self.in_loop += 1
        self.analyze_BlockContext(node.block())
        self.exit_scope()
        self.in_loop -= 1   

    def analyze_TestlistContext(self, node):
        current_var = node.getText()
        if current_var not in self.current_scope():
                raise SemanticError(f"Переменная '{current_var}' не объявлена.")

    def analyze_Flow_statementContext(self, node):
        """Анализ операторов управления потоком (break, continue, return)."""
        if node.BREAK():
            if self.in_loop == 0:
                raise SemanticError("Команда 'break' может быть использована только внутри цикла.")
        elif node.CONTINUE():
            if self.in_loop == 0:
                raise SemanticError("Команда 'continue' может быть использована только внутри цикла.")
        elif node.RETURN():
            if not self.in_function:
                raise SemanticError("Команда 'return' может быть использована только внутри функции.")
            self.analyze(node.testlist())

    def analyze_Expr_statementContext(self, node):
        """Анализ выражений, включая присваивание."""
        left_var = node.test(0)
        left_var_name = left_var.getText()
        if len(node.test()) > 1 and node.getChild(1).getText() == '=':                
            right_var = node.test(1)
            expr_node = self.find_expr_node(right_var)

            function_call_node = expr_node.functionCall()
            if function_call_node is not None:
                type_of_var = function_call_node.ID(0).getText()
                if left_var_name not in self.current_scope() and type_of_var in ['Set', 'Element']:
                    self.current_scope()[left_var_name] = type_of_var
                else:
                    self.current_scope()[left_var_name] = 'Set'
            
            set_operation_node = expr_node.set_operation()
            if set_operation_node is not None:
                right_var_text = right_var.getText()
                if any(op in right_var_text for op in ['+', '-', '*', '^']):
                    self.current_scope()[left_var_name] = 'Set'
                    self.analyze_Set_operationContext(set_operation_node, True)
        else:
            expr_node = self.find_expr_node(left_var)
            function_call_node = expr_node.functionCall()
            self.analyze_FunctionCallContext(function_call_node)

    def analyze_TestContext(self, node):
            self.analyze_Or_testContext(node.or_test())

    def analyze_Or_testContext(self, node):
        for and_test in node.and_test():
            self.analyze_And_testContext(and_test)

    def analyze_And_testContext(self, node):
        for not_test in node.not_test():
            self.analyze_Not_testContext(not_test)

    def analyze_Not_testContext(self, node):
        if node.NOT():
            self.analyze_Not_testContext(node.not_test())
        else:
            self.analyze_ComparisonContext(node.comparison())

    def analyze_ComparisonContext(self, node):
        left_expr = node.expr(0)
        right_expr = node.expr(1) if node.expr(1) else None

        left_type = self.get_expr_type(left_expr)
        right_type = self.get_expr_type(right_expr) if right_expr else None

        if node.comp_op() and left_type == 'Set' and right_type == 'Set':
            comp_op = node.comp_op(0).getText()
            if comp_op in ['==', '!=', '<', '>', '<=', '>=']:
                pass
            elif comp_op in ['UNION', 'DIFFERENCE', 'INTERSECTION', 'SYMMETRIC_DIFFERENCE']:
                if left_type != 'Set' or right_type != 'Set':
                    raise SemanticError("Операции над множествами поддерживаются только для типа 'Set'.")
            else:
                raise SemanticError(f"Оператор '{comp_op}' не поддерживается для множеств.")     
            
        elif node.comp_op() and (left_type == 'Set' and right_type == 'Element') or (left_type == 'Element' and right_type == 'Set'):
            raise SemanticError(f"Операция над разными типами объектов") 
        
    
    def get_expr_type(self, expr):
        """Получает тип выражения, используя текущую область видимости и проверяя вызовы методов."""
        if isinstance(expr, SetLexerParser.ExprContext):
            func_call_node = expr.functionCall()
            if func_call_node:
                self.analyze_FunctionCallContext(func_call_node)
            expr_name = expr.getText()
            if expr_name in self.current_scope():
                return self.current_scope()[expr_name]
        
        if isinstance(expr, SetLexerParser.FunctionCallContext):
            func_name = expr.ID(0).getText()
            if func_name in {"contains", "isEmpty"}:
                return 'bool'
            elif func_name in {"add", "remove", "clear"}:
                return 'Set'
        
        return None
    
    def analyze_Set_operationContext(self, node, expression = False):
        """Анализ операций объединения, пересечения, разности и симметрической разности над множествами."""
        set_exprs = node.atom()

        if expression:
            for i in range(0, len(set_exprs)):
                current_var = set_exprs[i].getText()
                if current_var not in self.current_scope():
                    raise SemanticError(f"Переменная '{current_var}' не объявлена.")

                if self.current_scope()[current_var] != 'Set':
                    raise SemanticError(f"'{current_var}' должно быть множеством.")

    def analyze_FunctionCallContext(self, node):
        """Анализ вызова метода для объектов типа 'Set'."""
        if node.getChildCount() == 4:
            obj_name = node.ID(0).getText()
            func_name = node.getChild(2).getText()
        elif node.getChildCount() == 6 or node.getChildCount() == 5:
            obj_name = node.getChild(0).getText()
            func_name = node.getChild(2).getText()
        else:
            raise SemanticError("Ошибка: неверная структура вызова функции.")
        
        if obj_name == "print":
            if node.arglist():
                args = node.arglist()
                for i in range(args.getChildCount()):
                    child_node = args.getChild(i)
                    expr_node = self.find_expr_node(child_node.test())
                    if expr_node and expr_node.functionCall():
                        self.analyze_FunctionCallContext(expr_node.functionCall())
                    if expr_node and expr_node.set_operation():
                        if '"' in expr_node.set_operation().getText():
                            break
                        self.analyze_Set_operationContext(expr_node.set_operation())
            return

        if obj_name not in self.current_scope():
            raise SemanticError(f"Метод '{func_name}' вызван у необъявленного объекта '{obj_name}'.")

        obj_type = self.current_scope()[obj_name]

        if obj_type == "Set":
            if func_name not in {"add", "remove", "contains", "size", "isEmpty", "clear"}:
                raise SemanticError(f"Метод '{func_name}' не поддерживается для объектов типа 'Set'.")
            if node.arglist():
                args = node.arglist()
                if func_name in {"add", "remove", "contains"}:
                    if args.getChildCount() != 1:
                        raise SemanticError(f"Метод '{func_name}' должен принимать 1 аргумент, получено {args.getChildCount()}.")

        elif obj_type == "Element":
            raise SemanticError(f"Объекты типа 'Element' не поддерживают методы '{func_name}'.")
        else:
            raise SemanticError(f"Метод '{func_name}' вызван у объекта '{obj_name}' с неподдерживаемым типом '{obj_type}'.")

        if func_name in {"size", "isEmpty", "clear"}:
            return

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