# Generated from XMLLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .XMLLangParser import XMLLangParser
else:
    from XMLLangParser import XMLLangParser

# This class defines a complete listener for a parse tree produced by XMLLangParser.
class XMLLangListener(ParseTreeListener):

    # Enter a parse tree produced by XMLLangParser#program.
    def enterProgram(self, ctx:XMLLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by XMLLangParser#program.
    def exitProgram(self, ctx:XMLLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by XMLLangParser#funcDef.
    def enterFuncDef(self, ctx:XMLLangParser.FuncDefContext):
        pass

    # Exit a parse tree produced by XMLLangParser#funcDef.
    def exitFuncDef(self, ctx:XMLLangParser.FuncDefContext):
        pass


    # Enter a parse tree produced by XMLLangParser#parameters.
    def enterParameters(self, ctx:XMLLangParser.ParametersContext):
        pass

    # Exit a parse tree produced by XMLLangParser#parameters.
    def exitParameters(self, ctx:XMLLangParser.ParametersContext):
        pass


    # Enter a parse tree produced by XMLLangParser#typedargslist.
    def enterTypedargslist(self, ctx:XMLLangParser.TypedargslistContext):
        pass

    # Exit a parse tree produced by XMLLangParser#typedargslist.
    def exitTypedargslist(self, ctx:XMLLangParser.TypedargslistContext):
        pass


    # Enter a parse tree produced by XMLLangParser#block.
    def enterBlock(self, ctx:XMLLangParser.BlockContext):
        pass

    # Exit a parse tree produced by XMLLangParser#block.
    def exitBlock(self, ctx:XMLLangParser.BlockContext):
        pass


    # Enter a parse tree produced by XMLLangParser#statement.
    def enterStatement(self, ctx:XMLLangParser.StatementContext):
        pass

    # Exit a parse tree produced by XMLLangParser#statement.
    def exitStatement(self, ctx:XMLLangParser.StatementContext):
        pass


    # Enter a parse tree produced by XMLLangParser#simple_statements.
    def enterSimple_statements(self, ctx:XMLLangParser.Simple_statementsContext):
        pass

    # Exit a parse tree produced by XMLLangParser#simple_statements.
    def exitSimple_statements(self, ctx:XMLLangParser.Simple_statementsContext):
        pass


    # Enter a parse tree produced by XMLLangParser#simple_statement.
    def enterSimple_statement(self, ctx:XMLLangParser.Simple_statementContext):
        pass

    # Exit a parse tree produced by XMLLangParser#simple_statement.
    def exitSimple_statement(self, ctx:XMLLangParser.Simple_statementContext):
        pass


    # Enter a parse tree produced by XMLLangParser#expr_statement.
    def enterExpr_statement(self, ctx:XMLLangParser.Expr_statementContext):
        pass

    # Exit a parse tree produced by XMLLangParser#expr_statement.
    def exitExpr_statement(self, ctx:XMLLangParser.Expr_statementContext):
        pass


    # Enter a parse tree produced by XMLLangParser#testlist_star_expr.
    def enterTestlist_star_expr(self, ctx:XMLLangParser.Testlist_star_exprContext):
        pass

    # Exit a parse tree produced by XMLLangParser#testlist_star_expr.
    def exitTestlist_star_expr(self, ctx:XMLLangParser.Testlist_star_exprContext):
        pass


    # Enter a parse tree produced by XMLLangParser#flow_statement.
    def enterFlow_statement(self, ctx:XMLLangParser.Flow_statementContext):
        pass

    # Exit a parse tree produced by XMLLangParser#flow_statement.
    def exitFlow_statement(self, ctx:XMLLangParser.Flow_statementContext):
        pass


    # Enter a parse tree produced by XMLLangParser#compound_statement.
    def enterCompound_statement(self, ctx:XMLLangParser.Compound_statementContext):
        pass

    # Exit a parse tree produced by XMLLangParser#compound_statement.
    def exitCompound_statement(self, ctx:XMLLangParser.Compound_statementContext):
        pass


    # Enter a parse tree produced by XMLLangParser#if_statement.
    def enterIf_statement(self, ctx:XMLLangParser.If_statementContext):
        pass

    # Exit a parse tree produced by XMLLangParser#if_statement.
    def exitIf_statement(self, ctx:XMLLangParser.If_statementContext):
        pass


    # Enter a parse tree produced by XMLLangParser#while_statement.
    def enterWhile_statement(self, ctx:XMLLangParser.While_statementContext):
        pass

    # Exit a parse tree produced by XMLLangParser#while_statement.
    def exitWhile_statement(self, ctx:XMLLangParser.While_statementContext):
        pass


    # Enter a parse tree produced by XMLLangParser#for_statement.
    def enterFor_statement(self, ctx:XMLLangParser.For_statementContext):
        pass

    # Exit a parse tree produced by XMLLangParser#for_statement.
    def exitFor_statement(self, ctx:XMLLangParser.For_statementContext):
        pass


    # Enter a parse tree produced by XMLLangParser#try_statement.
    def enterTry_statement(self, ctx:XMLLangParser.Try_statementContext):
        pass

    # Exit a parse tree produced by XMLLangParser#try_statement.
    def exitTry_statement(self, ctx:XMLLangParser.Try_statementContext):
        pass


    # Enter a parse tree produced by XMLLangParser#except_clause.
    def enterExcept_clause(self, ctx:XMLLangParser.Except_clauseContext):
        pass

    # Exit a parse tree produced by XMLLangParser#except_clause.
    def exitExcept_clause(self, ctx:XMLLangParser.Except_clauseContext):
        pass


    # Enter a parse tree produced by XMLLangParser#switch_statement.
    def enterSwitch_statement(self, ctx:XMLLangParser.Switch_statementContext):
        pass

    # Exit a parse tree produced by XMLLangParser#switch_statement.
    def exitSwitch_statement(self, ctx:XMLLangParser.Switch_statementContext):
        pass


    # Enter a parse tree produced by XMLLangParser#case_block.
    def enterCase_block(self, ctx:XMLLangParser.Case_blockContext):
        pass

    # Exit a parse tree produced by XMLLangParser#case_block.
    def exitCase_block(self, ctx:XMLLangParser.Case_blockContext):
        pass


    # Enter a parse tree produced by XMLLangParser#pattern.
    def enterPattern(self, ctx:XMLLangParser.PatternContext):
        pass

    # Exit a parse tree produced by XMLLangParser#pattern.
    def exitPattern(self, ctx:XMLLangParser.PatternContext):
        pass


    # Enter a parse tree produced by XMLLangParser#closed_pattern.
    def enterClosed_pattern(self, ctx:XMLLangParser.Closed_patternContext):
        pass

    # Exit a parse tree produced by XMLLangParser#closed_pattern.
    def exitClosed_pattern(self, ctx:XMLLangParser.Closed_patternContext):
        pass


    # Enter a parse tree produced by XMLLangParser#literal_pattern.
    def enterLiteral_pattern(self, ctx:XMLLangParser.Literal_patternContext):
        pass

    # Exit a parse tree produced by XMLLangParser#literal_pattern.
    def exitLiteral_pattern(self, ctx:XMLLangParser.Literal_patternContext):
        pass


    # Enter a parse tree produced by XMLLangParser#value_pattern.
    def enterValue_pattern(self, ctx:XMLLangParser.Value_patternContext):
        pass

    # Exit a parse tree produced by XMLLangParser#value_pattern.
    def exitValue_pattern(self, ctx:XMLLangParser.Value_patternContext):
        pass


    # Enter a parse tree produced by XMLLangParser#attr.
    def enterAttr(self, ctx:XMLLangParser.AttrContext):
        pass

    # Exit a parse tree produced by XMLLangParser#attr.
    def exitAttr(self, ctx:XMLLangParser.AttrContext):
        pass


    # Enter a parse tree produced by XMLLangParser#test.
    def enterTest(self, ctx:XMLLangParser.TestContext):
        pass

    # Exit a parse tree produced by XMLLangParser#test.
    def exitTest(self, ctx:XMLLangParser.TestContext):
        pass


    # Enter a parse tree produced by XMLLangParser#and_test.
    def enterAnd_test(self, ctx:XMLLangParser.And_testContext):
        pass

    # Exit a parse tree produced by XMLLangParser#and_test.
    def exitAnd_test(self, ctx:XMLLangParser.And_testContext):
        pass


    # Enter a parse tree produced by XMLLangParser#not_test.
    def enterNot_test(self, ctx:XMLLangParser.Not_testContext):
        pass

    # Exit a parse tree produced by XMLLangParser#not_test.
    def exitNot_test(self, ctx:XMLLangParser.Not_testContext):
        pass


    # Enter a parse tree produced by XMLLangParser#comparison.
    def enterComparison(self, ctx:XMLLangParser.ComparisonContext):
        pass

    # Exit a parse tree produced by XMLLangParser#comparison.
    def exitComparison(self, ctx:XMLLangParser.ComparisonContext):
        pass


    # Enter a parse tree produced by XMLLangParser#comp_op.
    def enterComp_op(self, ctx:XMLLangParser.Comp_opContext):
        pass

    # Exit a parse tree produced by XMLLangParser#comp_op.
    def exitComp_op(self, ctx:XMLLangParser.Comp_opContext):
        pass


    # Enter a parse tree produced by XMLLangParser#expr.
    def enterExpr(self, ctx:XMLLangParser.ExprContext):
        pass

    # Exit a parse tree produced by XMLLangParser#expr.
    def exitExpr(self, ctx:XMLLangParser.ExprContext):
        pass


    # Enter a parse tree produced by XMLLangParser#atom_expr.
    def enterAtom_expr(self, ctx:XMLLangParser.Atom_exprContext):
        pass

    # Exit a parse tree produced by XMLLangParser#atom_expr.
    def exitAtom_expr(self, ctx:XMLLangParser.Atom_exprContext):
        pass


    # Enter a parse tree produced by XMLLangParser#atom.
    def enterAtom(self, ctx:XMLLangParser.AtomContext):
        pass

    # Exit a parse tree produced by XMLLangParser#atom.
    def exitAtom(self, ctx:XMLLangParser.AtomContext):
        pass


    # Enter a parse tree produced by XMLLangParser#trailer.
    def enterTrailer(self, ctx:XMLLangParser.TrailerContext):
        pass

    # Exit a parse tree produced by XMLLangParser#trailer.
    def exitTrailer(self, ctx:XMLLangParser.TrailerContext):
        pass


    # Enter a parse tree produced by XMLLangParser#exprlist.
    def enterExprlist(self, ctx:XMLLangParser.ExprlistContext):
        pass

    # Exit a parse tree produced by XMLLangParser#exprlist.
    def exitExprlist(self, ctx:XMLLangParser.ExprlistContext):
        pass


    # Enter a parse tree produced by XMLLangParser#testlist.
    def enterTestlist(self, ctx:XMLLangParser.TestlistContext):
        pass

    # Exit a parse tree produced by XMLLangParser#testlist.
    def exitTestlist(self, ctx:XMLLangParser.TestlistContext):
        pass


    # Enter a parse tree produced by XMLLangParser#arglist.
    def enterArglist(self, ctx:XMLLangParser.ArglistContext):
        pass

    # Exit a parse tree produced by XMLLangParser#arglist.
    def exitArglist(self, ctx:XMLLangParser.ArglistContext):
        pass


    # Enter a parse tree produced by XMLLangParser#argument.
    def enterArgument(self, ctx:XMLLangParser.ArgumentContext):
        pass

    # Exit a parse tree produced by XMLLangParser#argument.
    def exitArgument(self, ctx:XMLLangParser.ArgumentContext):
        pass



del XMLLangParser