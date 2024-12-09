from XMLLangLexer import XMLLangLexer


class SemanticError(Exception):
    def __init__(self, message):
        super().__init__(message)


class SemanticAnalyzer:
    def __init__(self):
        self.symbol_tables = [{}]  # Таблицы символов для каждой области видимости
        self.function_table = {}  # Таблица функций
        self.in_loop = 0  # Счётчик вложенности циклов
        self.in_function = False  # Флаг нахождения внутри функции

    def enter_scope(self):
        """Вход в новую область видимости."""
        self.symbol_tables.append({})

    def exit_scope(self):
        """Выход из области видимости."""
        self.symbol_tables.pop()

    def current_scope(self):
        """Возвращает текущую таблицу символов."""
        return self.symbol_tables[-1]

    def analyze(self, node):
        """Анализирует узел, вызывая соответствующий метод анализа."""
        method_name = f'analyze_{type(node).__name__}'
        analyze_method = getattr(self, method_name, self.generic_analyze)
        analyze_method(node)

    def generic_analyze(self, node):
        """Рекурсивный обход дерева для общего случая."""
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            self.analyze(child)

    def analyze_ProgramContext(self, node):
        for statement in node.statement():
            self.analyze(statement)

    def analyze_StatementContext(self, node):
        """Обработка простых и сложных операторов."""
        if node.simple_statements():
            self.analyze(node.simple_statements())
        elif node.compound_statement():
            self.analyze(node.compound_statement())

    def analyze_Expr_statementContext(self, node):
        """Обработка выражений (присваивания или вычислений)."""
        if node.getChildCount() == 3 and node.getChild(1).getText() == '=':
            # Присваивание: <ID> = <expr>
            left_var = node.getChild(0).getText()
            right_expr = node.getChild(2)
            self.analyze(right_expr)
            if left_var not in self.current_scope():
                self.current_scope()[left_var] = 'Unknown'
        elif node.getChildCount() == 1:
            # Простое выражение
            self.analyze(node.getChild(0))
        else:
            raise SemanticError("Неподдерживаемое выражение.")

    def analyze_Compound_statementContext(self, node):
        """Обработка сложных операторов."""
        if node.if_statement():
            self.analyze(node.if_statement())
        elif node.while_statement():
            self.analyze(node.while_statement())
        elif node.for_statement():
            self.analyze(node.for_statement())
        elif node.funcDef():
            self.analyze(node.funcDef())

    def analyze_If_statementContext(self, node):
        """Обработка условного оператора."""
        self.analyze(node.test())
        self.enter_scope()
        self.analyze(node.block(0))
        self.exit_scope()
        if node.ELSE():
            self.enter_scope()
            self.analyze(node.block(1))
            self.exit_scope()

    def analyze_While_statementContext(self, node):
        """Обработка цикла while."""
        self.analyze(node.test())
        self.enter_scope()
        self.in_loop += 1
        self.analyze(node.block())
        self.exit_scope()
        self.in_loop -= 1

    def analyze_For_statementContext(self, node):
        """Обработка цикла for."""
        self.analyze(node.exprlist())
        self.enter_scope()
        self.in_loop += 1
        self.analyze(node.block())
        self.exit_scope()
        self.in_loop -= 1

    def analyze_FuncDefContext(self, node):
        """Обработка определения функции."""
        func_name = node.ID().getText()
        if func_name in self.function_table:
            raise SemanticError(f"Функция '{func_name}' уже объявлена.")
        self.enter_scope()
        self.in_function = True
        parameters = self.analyze_ParametersContext(node.parameters())
        self.function_table[func_name] = {'params': parameters, 'block': node.block()}
        self.analyze(node.block())
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
                self.current_scope()[param_name] = 'Unknown'
        return params

    def analyze_TestContext(self, node):
        """Анализ логических выражений."""
        # Возможно, нужно использовать and_test() или другой метод, в зависимости от вашей грамматики
        if hasattr(node, 'and_test'):
            self.analyze(node.and_test())  # Анализируем выражение с логическим оператором AND
        elif hasattr(node, 'or_test'):
            self.analyze(node.or_test())  # Анализируем выражение с логическим оператором OR
        else:
            raise SemanticError("Неизвестный тип логического выражения в тесте.")


    def analyze_Or_testContext(self, node):
        """Анализ логического оператора OR."""
        for and_test in node.and_test():
            self.analyze(and_test)

    def analyze_And_testContext(self, node):
        """Анализ логического оператора AND."""
        for not_test in node.not_test():
            self.analyze(not_test)

    def analyze_Not_testContext(self, node):
        """Анализ логического оператора NOT."""
        if node.NOT():
            self.analyze(node.not_test())
        else:
            self.analyze(node.comparison())

    def analyze_ComparisonContext(self, node):
        """Анализ сравнения."""
        left_expr = node.expr(0)
        right_expr = node.expr(1) if node.expr(1) else None
        self.analyze(left_expr)
        if right_expr:
            self.analyze(right_expr)
