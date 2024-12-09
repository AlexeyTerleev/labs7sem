# Generated from SetLexerParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3)")
        buf.write("\u0103\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\7\2:\n\2\f\2\16")
        buf.write("\2=\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\5\4H\n\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\7\5O\n\5\f\5\16\5R\13\5\3\6\3\6\6")
        buf.write("\6V\n\6\r\6\16\6W\3\6\3\6\3\7\3\7\5\7^\n\7\3\b\3\b\5\b")
        buf.write("b\n\b\3\t\3\t\3\t\7\tg\n\t\f\t\16\tj\13\t\3\n\3\n\3\n")
        buf.write("\3\n\5\np\n\n\5\nr\n\n\3\13\3\13\3\13\3\13\5\13x\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\f\177\n\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\7\20")
        buf.write("\u0090\n\20\f\20\16\20\u0093\13\20\3\21\3\21\3\21\7\21")
        buf.write("\u0098\n\21\f\21\16\21\u009b\13\21\3\22\3\22\3\22\5\22")
        buf.write("\u00a0\n\22\3\23\3\23\3\23\3\23\7\23\u00a6\n\23\f\23\16")
        buf.write("\23\u00a9\13\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u00b4\n\24\3\25\3\25\3\25\5\25\u00b9\n\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u00c4")
        buf.write("\n\26\f\26\16\26\u00c7\13\26\3\27\3\27\3\27\6\27\u00cc")
        buf.write("\n\27\r\27\16\27\u00cd\3\27\3\27\3\27\5\27\u00d3\n\27")
        buf.write("\3\30\3\30\3\30\5\30\u00d8\n\30\3\30\3\30\5\30\u00dc\n")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\7\31\u00e3\n\31\f\31\16\31")
        buf.write("\u00e6\13\31\3\31\5\31\u00e9\n\31\3\32\3\32\3\32\7\32")
        buf.write("\u00ee\n\32\f\32\16\32\u00f1\13\32\3\32\5\32\u00f4\n\32")
        buf.write("\3\33\3\33\3\33\7\33\u00f9\n\33\f\33\16\33\u00fc\13\33")
        buf.write("\3\33\5\33\u00ff\n\33\3\34\3\34\3\34\2\2\35\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66\2\2")
        buf.write("\2\u0114\2;\3\2\2\2\4@\3\2\2\2\6E\3\2\2\2\bK\3\2\2\2\n")
        buf.write("S\3\2\2\2\f]\3\2\2\2\16a\3\2\2\2\20c\3\2\2\2\22q\3\2\2")
        buf.write("\2\24w\3\2\2\2\26y\3\2\2\2\30\u0080\3\2\2\2\32\u0084\3")
        buf.write("\2\2\2\34\u008a\3\2\2\2\36\u008c\3\2\2\2 \u0094\3\2\2")
        buf.write("\2\"\u009f\3\2\2\2$\u00a1\3\2\2\2&\u00b3\3\2\2\2(\u00b8")
        buf.write("\3\2\2\2*\u00ba\3\2\2\2,\u00d2\3\2\2\2.\u00d4\3\2\2\2")
        buf.write("\60\u00df\3\2\2\2\62\u00ea\3\2\2\2\64\u00f5\3\2\2\2\66")
        buf.write("\u0100\3\2\2\28:\5\f\7\298\3\2\2\2:=\3\2\2\2;9\3\2\2\2")
        buf.write(";<\3\2\2\2<>\3\2\2\2=;\3\2\2\2>?\7\2\2\3?\3\3\2\2\2@A")
        buf.write("\7\n\2\2AB\7\30\2\2BC\5\6\4\2CD\5\n\6\2D\5\3\2\2\2EG\7")
        buf.write("\33\2\2FH\5\b\5\2GF\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\7\34")
        buf.write("\2\2J\7\3\2\2\2KP\7\30\2\2LM\7\37\2\2MO\7\30\2\2NL\3\2")
        buf.write("\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\t\3\2\2\2RP\3\2\2")
        buf.write("\2SU\7\3\2\2TV\5\f\7\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2W")
        buf.write("X\3\2\2\2XY\3\2\2\2YZ\7\4\2\2Z\13\3\2\2\2[^\5\16\b\2\\")
        buf.write("^\5\24\13\2][\3\2\2\2]\\\3\2\2\2^\r\3\2\2\2_b\5\20\t\2")
        buf.write("`b\5\22\n\2a_\3\2\2\2a`\3\2\2\2b\17\3\2\2\2ch\5\34\17")
        buf.write("\2de\7\"\2\2eg\5\34\17\2fd\3\2\2\2gj\3\2\2\2hf\3\2\2\2")
        buf.write("hi\3\2\2\2i\21\3\2\2\2jh\3\2\2\2kr\7\b\2\2lr\7\t\2\2m")
        buf.write("o\7\23\2\2np\5\62\32\2on\3\2\2\2op\3\2\2\2pr\3\2\2\2q")
        buf.write("k\3\2\2\2ql\3\2\2\2qm\3\2\2\2r\23\3\2\2\2sx\5\26\f\2t")
        buf.write("x\5\30\r\2ux\5\32\16\2vx\5\4\3\2ws\3\2\2\2wt\3\2\2\2w")
        buf.write("u\3\2\2\2wv\3\2\2\2x\25\3\2\2\2yz\7\16\2\2z{\5\34\17\2")
        buf.write("{~\5\n\6\2|}\7\13\2\2}\177\5\n\6\2~|\3\2\2\2~\177\3\2")
        buf.write("\2\2\177\27\3\2\2\2\u0080\u0081\7\25\2\2\u0081\u0082\5")
        buf.write("\34\17\2\u0082\u0083\5\n\6\2\u0083\31\3\2\2\2\u0084\u0085")
        buf.write("\7\r\2\2\u0085\u0086\5\60\31\2\u0086\u0087\7\17\2\2\u0087")
        buf.write("\u0088\5\62\32\2\u0088\u0089\5\n\6\2\u0089\33\3\2\2\2")
        buf.write("\u008a\u008b\5\36\20\2\u008b\35\3\2\2\2\u008c\u0091\5")
        buf.write(" \21\2\u008d\u008e\7\22\2\2\u008e\u0090\5 \21\2\u008f")
        buf.write("\u008d\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092\37\3\2\2\2\u0093\u0091\3\2")
        buf.write("\2\2\u0094\u0099\5\"\22\2\u0095\u0096\7\7\2\2\u0096\u0098")
        buf.write("\5\"\22\2\u0097\u0095\3\2\2\2\u0098\u009b\3\2\2\2\u0099")
        buf.write("\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a!\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009c\u009d\7\21\2\2\u009d\u00a0\5\"\22")
        buf.write("\2\u009e\u00a0\5$\23\2\u009f\u009c\3\2\2\2\u009f\u009e")
        buf.write("\3\2\2\2\u00a0#\3\2\2\2\u00a1\u00a7\5(\25\2\u00a2\u00a3")
        buf.write("\5&\24\2\u00a3\u00a4\5(\25\2\u00a4\u00a6\3\2\2\2\u00a5")
        buf.write("\u00a2\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a8%\3\2\2\2\u00a9\u00a7\3\2\2")
        buf.write("\2\u00aa\u00b4\7\'\2\2\u00ab\u00b4\7(\2\2\u00ac\u00b4")
        buf.write("\7\17\2\2\u00ad\u00ae\7\21\2\2\u00ae\u00b4\7\17\2\2\u00af")
        buf.write("\u00b4\7#\2\2\u00b0\u00b4\7$\2\2\u00b1\u00b4\7%\2\2\u00b2")
        buf.write("\u00b4\7&\2\2\u00b3\u00aa\3\2\2\2\u00b3\u00ab\3\2\2\2")
        buf.write("\u00b3\u00ac\3\2\2\2\u00b3\u00ad\3\2\2\2\u00b3\u00af\3")
        buf.write("\2\2\2\u00b3\u00b0\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b2")
        buf.write("\3\2\2\2\u00b4\'\3\2\2\2\u00b5\u00b9\5*\26\2\u00b6\u00b9")
        buf.write("\5.\30\2\u00b7\u00b9\5,\27\2\u00b8\u00b5\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9)\3\2\2\2\u00ba")
        buf.write("\u00c5\5,\27\2\u00bb\u00bc\7#\2\2\u00bc\u00c4\5,\27\2")
        buf.write("\u00bd\u00be\7%\2\2\u00be\u00c4\5,\27\2\u00bf\u00c0\7")
        buf.write("$\2\2\u00c0\u00c4\5,\27\2\u00c1\u00c2\7&\2\2\u00c2\u00c4")
        buf.write("\5,\27\2\u00c3\u00bb\3\2\2\2\u00c3\u00bd\3\2\2\2\u00c3")
        buf.write("\u00bf\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c7\3\2\2\2")
        buf.write("\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6+\3\2\2")
        buf.write("\2\u00c7\u00c5\3\2\2\2\u00c8\u00d3\7\30\2\2\u00c9\u00d3")
        buf.write("\7\6\2\2\u00ca\u00cc\7\5\2\2\u00cb\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cd\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce\u00d3\3\2\2\2\u00cf\u00d3\7\20\2\2\u00d0\u00d3")
        buf.write("\7\24\2\2\u00d1\u00d3\7\f\2\2\u00d2\u00c8\3\2\2\2\u00d2")
        buf.write("\u00c9\3\2\2\2\u00d2\u00cb\3\2\2\2\u00d2\u00cf\3\2\2\2")
        buf.write("\u00d2\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3-\3\2\2")
        buf.write("\2\u00d4\u00d7\7\30\2\2\u00d5\u00d6\7\32\2\2\u00d6\u00d8")
        buf.write("\7\30\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9\u00db\7\33\2\2\u00da\u00dc\5\64\33")
        buf.write("\2\u00db\u00da\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd\u00de\7\34\2\2\u00de/\3\2\2\2\u00df\u00e4")
        buf.write("\5(\25\2\u00e0\u00e1\7\37\2\2\u00e1\u00e3\5(\25\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2")
        buf.write("\u00e4\u00e5\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3")
        buf.write("\2\2\2\u00e7\u00e9\7\37\2\2\u00e8\u00e7\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\61\3\2\2\2\u00ea\u00ef\5\34\17\2")
        buf.write("\u00eb\u00ec\7\37\2\2\u00ec\u00ee\5\34\17\2\u00ed\u00eb")
        buf.write("\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2")
        buf.write("\u00f2\u00f4\7\37\2\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4\63\3\2\2\2\u00f5\u00fa\5\66\34\2\u00f6")
        buf.write("\u00f7\7\37\2\2\u00f7\u00f9\5\66\34\2\u00f8\u00f6\3\2")
        buf.write("\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd")
        buf.write("\u00ff\7\37\2\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff\3\2\2")
        buf.write("\2\u00ff\65\3\2\2\2\u0100\u0101\5\34\17\2\u0101\67\3\2")
        buf.write("\2\2\37;GPW]ahoqw~\u0091\u0099\u009f\u00a7\u00b3\u00b8")
        buf.write("\u00c3\u00c5\u00cd\u00d2\u00d7\u00db\u00e4\u00e8\u00ef")
        buf.write("\u00f3\u00fa\u00fe")
        return buf.getvalue()


class SetLexerParser ( Parser ):

    grammarFileName = "SetLexerParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "<INVALID>", "<INVALID>", 
                     "'and'", "'break'", "'continue'", "'def'", "'else'", 
                     "'False'", "'for'", "'if'", "'in'", "'None'", "'not'", 
                     "'or'", "'return'", "'True'", "'while'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'.'", "'('", 
                     "')'", "'['", "']'", "','", "':'", "';'", "'='", "'+'", 
                     "'-'", "'*'", "'^'", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "STRING", "NUMBER", 
                      "AND", "BREAK", "CONTINUE", "DEF", "ELSE", "FALSE", 
                      "FOR", "IF", "IN", "NONE", "NOT", "OR", "RETURN", 
                      "TRUE", "WHILE", "WS", "NEWLINE", "ID", "DECIMAL_INTEGER", 
                      "DOT", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", 
                      "CLOSE_BRACK", "COMMA", "COLON", "SEMI_COLON", "ASSIGN", 
                      "UNION", "DIFFERENCE", "INTERSECTION", "SYMMETRIC_DIFFERENCE", 
                      "EQUALS", "NOT_EQ_2", "UNKNOWN_CHAR" ]

    RULE_program = 0
    RULE_funcDef = 1
    RULE_parameters = 2
    RULE_typedargslist = 3
    RULE_block = 4
    RULE_statement = 5
    RULE_simple_statement = 6
    RULE_expr_statement = 7
    RULE_flow_statement = 8
    RULE_compound_statement = 9
    RULE_if_statement = 10
    RULE_while_statement = 11
    RULE_for_statement = 12
    RULE_test = 13
    RULE_or_test = 14
    RULE_and_test = 15
    RULE_not_test = 16
    RULE_comparison = 17
    RULE_comp_op = 18
    RULE_expr = 19
    RULE_set_operation = 20
    RULE_atom = 21
    RULE_functionCall = 22
    RULE_exprlist = 23
    RULE_testlist = 24
    RULE_arglist = 25
    RULE_argument = 26

    ruleNames =  [ "program", "funcDef", "parameters", "typedargslist", 
                   "block", "statement", "simple_statement", "expr_statement", 
                   "flow_statement", "compound_statement", "if_statement", 
                   "while_statement", "for_statement", "test", "or_test", 
                   "and_test", "not_test", "comparison", "comp_op", "expr", 
                   "set_operation", "atom", "functionCall", "exprlist", 
                   "testlist", "arglist", "argument" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    STRING=3
    NUMBER=4
    AND=5
    BREAK=6
    CONTINUE=7
    DEF=8
    ELSE=9
    FALSE=10
    FOR=11
    IF=12
    IN=13
    NONE=14
    NOT=15
    OR=16
    RETURN=17
    TRUE=18
    WHILE=19
    WS=20
    NEWLINE=21
    ID=22
    DECIMAL_INTEGER=23
    DOT=24
    OPEN_PAREN=25
    CLOSE_PAREN=26
    OPEN_BRACK=27
    CLOSE_BRACK=28
    COMMA=29
    COLON=30
    SEMI_COLON=31
    ASSIGN=32
    UNION=33
    DIFFERENCE=34
    INTERSECTION=35
    SYMMETRIC_DIFFERENCE=36
    EQUALS=37
    NOT_EQ_2=38
    UNKNOWN_CHAR=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SetLexerParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.StatementContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.StatementContext,i)


        def getRuleIndex(self):
            return SetLexerParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = SetLexerParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetLexerParser.STRING) | (1 << SetLexerParser.NUMBER) | (1 << SetLexerParser.BREAK) | (1 << SetLexerParser.CONTINUE) | (1 << SetLexerParser.DEF) | (1 << SetLexerParser.FALSE) | (1 << SetLexerParser.FOR) | (1 << SetLexerParser.IF) | (1 << SetLexerParser.NONE) | (1 << SetLexerParser.NOT) | (1 << SetLexerParser.RETURN) | (1 << SetLexerParser.TRUE) | (1 << SetLexerParser.WHILE) | (1 << SetLexerParser.ID))) != 0):
                self.state = 54
                self.statement()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(SetLexerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(SetLexerParser.DEF, 0)

        def ID(self):
            return self.getToken(SetLexerParser.ID, 0)

        def parameters(self):
            return self.getTypedRuleContext(SetLexerParser.ParametersContext,0)


        def block(self):
            return self.getTypedRuleContext(SetLexerParser.BlockContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)




    def funcDef(self):

        localctx = SetLexerParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(SetLexerParser.DEF)
            self.state = 63
            self.match(SetLexerParser.ID)
            self.state = 64
            self.parameters()
            self.state = 65
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(SetLexerParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(SetLexerParser.CLOSE_PAREN, 0)

        def typedargslist(self):
            return self.getTypedRuleContext(SetLexerParser.TypedargslistContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = SetLexerParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(SetLexerParser.OPEN_PAREN)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetLexerParser.ID:
                self.state = 68
                self.typedargslist()


            self.state = 71
            self.match(SetLexerParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedargslistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.ID)
            else:
                return self.getToken(SetLexerParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.COMMA)
            else:
                return self.getToken(SetLexerParser.COMMA, i)

        def getRuleIndex(self):
            return SetLexerParser.RULE_typedargslist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedargslist" ):
                listener.enterTypedargslist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedargslist" ):
                listener.exitTypedargslist(self)




    def typedargslist(self):

        localctx = SetLexerParser.TypedargslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typedargslist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SetLexerParser.ID)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetLexerParser.COMMA:
                self.state = 74
                self.match(SetLexerParser.COMMA)
                self.state = 75
                self.match(SetLexerParser.ID)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(SetLexerParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(SetLexerParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.StatementContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.StatementContext,i)


        def getRuleIndex(self):
            return SetLexerParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = SetLexerParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(SetLexerParser.INDENT)
            self.state = 83 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                self.statement()
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetLexerParser.STRING) | (1 << SetLexerParser.NUMBER) | (1 << SetLexerParser.BREAK) | (1 << SetLexerParser.CONTINUE) | (1 << SetLexerParser.DEF) | (1 << SetLexerParser.FALSE) | (1 << SetLexerParser.FOR) | (1 << SetLexerParser.IF) | (1 << SetLexerParser.NONE) | (1 << SetLexerParser.NOT) | (1 << SetLexerParser.RETURN) | (1 << SetLexerParser.TRUE) | (1 << SetLexerParser.WHILE) | (1 << SetLexerParser.ID))) != 0)):
                    break

            self.state = 87
            self.match(SetLexerParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_statement(self):
            return self.getTypedRuleContext(SetLexerParser.Simple_statementContext,0)


        def compound_statement(self):
            return self.getTypedRuleContext(SetLexerParser.Compound_statementContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = SetLexerParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetLexerParser.STRING, SetLexerParser.NUMBER, SetLexerParser.BREAK, SetLexerParser.CONTINUE, SetLexerParser.FALSE, SetLexerParser.NONE, SetLexerParser.NOT, SetLexerParser.RETURN, SetLexerParser.TRUE, SetLexerParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.simple_statement()
                pass
            elif token in [SetLexerParser.DEF, SetLexerParser.FOR, SetLexerParser.IF, SetLexerParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.compound_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_statement(self):
            return self.getTypedRuleContext(SetLexerParser.Expr_statementContext,0)


        def flow_statement(self):
            return self.getTypedRuleContext(SetLexerParser.Flow_statementContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_simple_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_statement" ):
                listener.enterSimple_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_statement" ):
                listener.exitSimple_statement(self)




    def simple_statement(self):

        localctx = SetLexerParser.Simple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_simple_statement)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetLexerParser.STRING, SetLexerParser.NUMBER, SetLexerParser.FALSE, SetLexerParser.NONE, SetLexerParser.NOT, SetLexerParser.TRUE, SetLexerParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.expr_statement()
                pass
            elif token in [SetLexerParser.BREAK, SetLexerParser.CONTINUE, SetLexerParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.flow_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.TestContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.TestContext,i)


        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.ASSIGN)
            else:
                return self.getToken(SetLexerParser.ASSIGN, i)

        def getRuleIndex(self):
            return SetLexerParser.RULE_expr_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_statement" ):
                listener.enterExpr_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_statement" ):
                listener.exitExpr_statement(self)




    def expr_statement(self):

        localctx = SetLexerParser.Expr_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.test()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetLexerParser.ASSIGN:
                self.state = 98
                self.match(SetLexerParser.ASSIGN)
                self.state = 99
                self.test()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Flow_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(SetLexerParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(SetLexerParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(SetLexerParser.RETURN, 0)

        def testlist(self):
            return self.getTypedRuleContext(SetLexerParser.TestlistContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_flow_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlow_statement" ):
                listener.enterFlow_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlow_statement" ):
                listener.exitFlow_statement(self)




    def flow_statement(self):

        localctx = SetLexerParser.Flow_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_flow_statement)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetLexerParser.BREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(SetLexerParser.BREAK)
                pass
            elif token in [SetLexerParser.CONTINUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(SetLexerParser.CONTINUE)
                pass
            elif token in [SetLexerParser.RETURN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.match(SetLexerParser.RETURN)
                self.state = 109
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 108
                    self.testlist()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compound_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(SetLexerParser.If_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(SetLexerParser.While_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(SetLexerParser.For_statementContext,0)


        def funcDef(self):
            return self.getTypedRuleContext(SetLexerParser.FuncDefContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_compound_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_statement" ):
                listener.enterCompound_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_statement" ):
                listener.exitCompound_statement(self)




    def compound_statement(self):

        localctx = SetLexerParser.Compound_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_compound_statement)
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetLexerParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.if_statement()
                pass
            elif token in [SetLexerParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.while_statement()
                pass
            elif token in [SetLexerParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.for_statement()
                pass
            elif token in [SetLexerParser.DEF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.funcDef()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SetLexerParser.IF, 0)

        def test(self):
            return self.getTypedRuleContext(SetLexerParser.TestContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.BlockContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(SetLexerParser.ELSE, 0)

        def getRuleIndex(self):
            return SetLexerParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = SetLexerParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(SetLexerParser.IF)
            self.state = 120
            self.test()
            self.state = 121
            self.block()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetLexerParser.ELSE:
                self.state = 122
                self.match(SetLexerParser.ELSE)
                self.state = 123
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SetLexerParser.WHILE, 0)

        def test(self):
            return self.getTypedRuleContext(SetLexerParser.TestContext,0)


        def block(self):
            return self.getTypedRuleContext(SetLexerParser.BlockContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = SetLexerParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(SetLexerParser.WHILE)
            self.state = 127
            self.test()
            self.state = 128
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(SetLexerParser.FOR, 0)

        def exprlist(self):
            return self.getTypedRuleContext(SetLexerParser.ExprlistContext,0)


        def IN(self):
            return self.getToken(SetLexerParser.IN, 0)

        def testlist(self):
            return self.getTypedRuleContext(SetLexerParser.TestlistContext,0)


        def block(self):
            return self.getTypedRuleContext(SetLexerParser.BlockContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)




    def for_statement(self):

        localctx = SetLexerParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(SetLexerParser.FOR)
            self.state = 131
            self.exprlist()
            self.state = 132
            self.match(SetLexerParser.IN)
            self.state = 133
            self.testlist()
            self.state = 134
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_test(self):
            return self.getTypedRuleContext(SetLexerParser.Or_testContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTest" ):
                listener.enterTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTest" ):
                listener.exitTest(self)




    def test(self):

        localctx = SetLexerParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_test)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.or_test()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Or_testContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.And_testContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.And_testContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.OR)
            else:
                return self.getToken(SetLexerParser.OR, i)

        def getRuleIndex(self):
            return SetLexerParser.RULE_or_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_test" ):
                listener.enterOr_test(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_test" ):
                listener.exitOr_test(self)




    def or_test(self):

        localctx = SetLexerParser.Or_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_or_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.and_test()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetLexerParser.OR:
                self.state = 139
                self.match(SetLexerParser.OR)
                self.state = 140
                self.and_test()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_testContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.Not_testContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.Not_testContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.AND)
            else:
                return self.getToken(SetLexerParser.AND, i)

        def getRuleIndex(self):
            return SetLexerParser.RULE_and_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_test" ):
                listener.enterAnd_test(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_test" ):
                listener.exitAnd_test(self)




    def and_test(self):

        localctx = SetLexerParser.And_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_and_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.not_test()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SetLexerParser.AND:
                self.state = 147
                self.match(SetLexerParser.AND)
                self.state = 148
                self.not_test()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Not_testContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(SetLexerParser.NOT, 0)

        def not_test(self):
            return self.getTypedRuleContext(SetLexerParser.Not_testContext,0)


        def comparison(self):
            return self.getTypedRuleContext(SetLexerParser.ComparisonContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_not_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_test" ):
                listener.enterNot_test(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_test" ):
                listener.exitNot_test(self)




    def not_test(self):

        localctx = SetLexerParser.Not_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_not_test)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetLexerParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(SetLexerParser.NOT)
                self.state = 155
                self.not_test()
                pass
            elif token in [SetLexerParser.STRING, SetLexerParser.NUMBER, SetLexerParser.FALSE, SetLexerParser.NONE, SetLexerParser.TRUE, SetLexerParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.comparison()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.ExprContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.ExprContext,i)


        def comp_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.Comp_opContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.Comp_opContext,i)


        def getRuleIndex(self):
            return SetLexerParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = SetLexerParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.expr()
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 160
                    self.comp_op()
                    self.state = 161
                    self.expr() 
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comp_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(SetLexerParser.EQUALS, 0)

        def NOT_EQ_2(self):
            return self.getToken(SetLexerParser.NOT_EQ_2, 0)

        def IN(self):
            return self.getToken(SetLexerParser.IN, 0)

        def NOT(self):
            return self.getToken(SetLexerParser.NOT, 0)

        def UNION(self):
            return self.getToken(SetLexerParser.UNION, 0)

        def DIFFERENCE(self):
            return self.getToken(SetLexerParser.DIFFERENCE, 0)

        def INTERSECTION(self):
            return self.getToken(SetLexerParser.INTERSECTION, 0)

        def SYMMETRIC_DIFFERENCE(self):
            return self.getToken(SetLexerParser.SYMMETRIC_DIFFERENCE, 0)

        def getRuleIndex(self):
            return SetLexerParser.RULE_comp_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_op" ):
                listener.enterComp_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_op" ):
                listener.exitComp_op(self)




    def comp_op(self):

        localctx = SetLexerParser.Comp_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comp_op)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetLexerParser.EQUALS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(SetLexerParser.EQUALS)
                pass
            elif token in [SetLexerParser.NOT_EQ_2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(SetLexerParser.NOT_EQ_2)
                pass
            elif token in [SetLexerParser.IN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.match(SetLexerParser.IN)
                pass
            elif token in [SetLexerParser.NOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 171
                self.match(SetLexerParser.NOT)
                self.state = 172
                self.match(SetLexerParser.IN)
                pass
            elif token in [SetLexerParser.UNION]:
                self.enterOuterAlt(localctx, 5)
                self.state = 173
                self.match(SetLexerParser.UNION)
                pass
            elif token in [SetLexerParser.DIFFERENCE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 174
                self.match(SetLexerParser.DIFFERENCE)
                pass
            elif token in [SetLexerParser.INTERSECTION]:
                self.enterOuterAlt(localctx, 7)
                self.state = 175
                self.match(SetLexerParser.INTERSECTION)
                pass
            elif token in [SetLexerParser.SYMMETRIC_DIFFERENCE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 176
                self.match(SetLexerParser.SYMMETRIC_DIFFERENCE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def set_operation(self):
            return self.getTypedRuleContext(SetLexerParser.Set_operationContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SetLexerParser.FunctionCallContext,0)


        def atom(self):
            return self.getTypedRuleContext(SetLexerParser.AtomContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = SetLexerParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.set_operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.atom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_operationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.AtomContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.AtomContext,i)


        def UNION(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.UNION)
            else:
                return self.getToken(SetLexerParser.UNION, i)

        def INTERSECTION(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.INTERSECTION)
            else:
                return self.getToken(SetLexerParser.INTERSECTION, i)

        def DIFFERENCE(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.DIFFERENCE)
            else:
                return self.getToken(SetLexerParser.DIFFERENCE, i)

        def SYMMETRIC_DIFFERENCE(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.SYMMETRIC_DIFFERENCE)
            else:
                return self.getToken(SetLexerParser.SYMMETRIC_DIFFERENCE, i)

        def getRuleIndex(self):
            return SetLexerParser.RULE_set_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_operation" ):
                listener.enterSet_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_operation" ):
                listener.exitSet_operation(self)




    def set_operation(self):

        localctx = SetLexerParser.Set_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_set_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.atom()
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 193
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SetLexerParser.UNION]:
                        self.state = 185
                        self.match(SetLexerParser.UNION)
                        self.state = 186
                        self.atom()
                        pass
                    elif token in [SetLexerParser.INTERSECTION]:
                        self.state = 187
                        self.match(SetLexerParser.INTERSECTION)
                        self.state = 188
                        self.atom()
                        pass
                    elif token in [SetLexerParser.DIFFERENCE]:
                        self.state = 189
                        self.match(SetLexerParser.DIFFERENCE)
                        self.state = 190
                        self.atom()
                        pass
                    elif token in [SetLexerParser.SYMMETRIC_DIFFERENCE]:
                        self.state = 191
                        self.match(SetLexerParser.SYMMETRIC_DIFFERENCE)
                        self.state = 192
                        self.atom()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SetLexerParser.ID, 0)

        def NUMBER(self):
            return self.getToken(SetLexerParser.NUMBER, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.STRING)
            else:
                return self.getToken(SetLexerParser.STRING, i)

        def NONE(self):
            return self.getToken(SetLexerParser.NONE, 0)

        def TRUE(self):
            return self.getToken(SetLexerParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SetLexerParser.FALSE, 0)

        def getRuleIndex(self):
            return SetLexerParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = SetLexerParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_atom)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SetLexerParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(SetLexerParser.ID)
                pass
            elif token in [SetLexerParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(SetLexerParser.NUMBER)
                pass
            elif token in [SetLexerParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 201 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 200
                        self.match(SetLexerParser.STRING)

                    else:
                        raise NoViableAltException(self)
                    self.state = 203 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass
            elif token in [SetLexerParser.NONE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.match(SetLexerParser.NONE)
                pass
            elif token in [SetLexerParser.TRUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 206
                self.match(SetLexerParser.TRUE)
                pass
            elif token in [SetLexerParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 207
                self.match(SetLexerParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.ID)
            else:
                return self.getToken(SetLexerParser.ID, i)

        def OPEN_PAREN(self):
            return self.getToken(SetLexerParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(SetLexerParser.CLOSE_PAREN, 0)

        def DOT(self):
            return self.getToken(SetLexerParser.DOT, 0)

        def arglist(self):
            return self.getTypedRuleContext(SetLexerParser.ArglistContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = SetLexerParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(SetLexerParser.ID)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetLexerParser.DOT:
                self.state = 211
                self.match(SetLexerParser.DOT)
                self.state = 212
                self.match(SetLexerParser.ID)


            self.state = 215
            self.match(SetLexerParser.OPEN_PAREN)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SetLexerParser.STRING) | (1 << SetLexerParser.NUMBER) | (1 << SetLexerParser.FALSE) | (1 << SetLexerParser.NONE) | (1 << SetLexerParser.NOT) | (1 << SetLexerParser.TRUE) | (1 << SetLexerParser.ID))) != 0):
                self.state = 216
                self.arglist()


            self.state = 219
            self.match(SetLexerParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.ExprContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.COMMA)
            else:
                return self.getToken(SetLexerParser.COMMA, i)

        def getRuleIndex(self):
            return SetLexerParser.RULE_exprlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprlist" ):
                listener.enterExprlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprlist" ):
                listener.exitExprlist(self)




    def exprlist(self):

        localctx = SetLexerParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exprlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.expr()
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 222
                    self.match(SetLexerParser.COMMA)
                    self.state = 223
                    self.expr() 
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetLexerParser.COMMA:
                self.state = 229
                self.match(SetLexerParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TestlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.TestContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.TestContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.COMMA)
            else:
                return self.getToken(SetLexerParser.COMMA, i)

        def getRuleIndex(self):
            return SetLexerParser.RULE_testlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTestlist" ):
                listener.enterTestlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTestlist" ):
                listener.exitTestlist(self)




    def testlist(self):

        localctx = SetLexerParser.TestlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_testlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.test()
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 233
                    self.match(SetLexerParser.COMMA)
                    self.state = 234
                    self.test() 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetLexerParser.COMMA:
                self.state = 240
                self.match(SetLexerParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArglistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SetLexerParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(SetLexerParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SetLexerParser.COMMA)
            else:
                return self.getToken(SetLexerParser.COMMA, i)

        def getRuleIndex(self):
            return SetLexerParser.RULE_arglist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArglist" ):
                listener.enterArglist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArglist" ):
                listener.exitArglist(self)




    def arglist(self):

        localctx = SetLexerParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.argument()
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 244
                    self.match(SetLexerParser.COMMA)
                    self.state = 245
                    self.argument() 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SetLexerParser.COMMA:
                self.state = 251
                self.match(SetLexerParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self):
            return self.getTypedRuleContext(SetLexerParser.TestContext,0)


        def getRuleIndex(self):
            return SetLexerParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = SetLexerParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.test()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





