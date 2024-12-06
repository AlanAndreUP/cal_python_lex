import ply.lex as lex
import ply.yacc as yacc
import math

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'SENO',
    'COSENO',
    'RAIZ'
)

# añadidos al lexer
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+(\.\d+)?'
t_SENO = r'sin'
t_COSENO = r'cos'
t_RAIZ = r'√'

t_ignore = ' \t'

# Manejar errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Gramática para las expresiones aritméticas
def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = ('+', p[1], p[3]) if p[2] == '+' else ('-', p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    p[0] = ('*', p[1], p[3]) if p[2] == '*' else ('/', p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = float(p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_factor_func(p):
    '''factor : SENO LPAREN expression RPAREN
              | COSENO LPAREN expression RPAREN
              | RAIZ LPAREN expression RPAREN'''
    if p[1] == 'sin':
        p[0] = ('sin', p[3])
    elif p[1] == 'cos':
        p[0] = ('cos', p[3])
    elif p[1] == '√':
        p[0] = ('√', p[3])

# Manejar errores de sintaxis
def p_error(p):
    print("Error de sintaxis en la entrada")

# Construir el parser
parser = yacc.yacc()

def eval_arbol(arbol):
    if isinstance(arbol, (int, float)):
        return arbol

    operador = arbol[0]

    if operador == '+':
        return eval_arbol(arbol[1]) + eval_arbol(arbol[2])
    elif operador == '-':
        return eval_arbol(arbol[1]) - eval_arbol(arbol[2])
    elif operador == '*':
        return eval_arbol(arbol[1]) * eval_arbol(arbol[2])
    elif operador == '/':
        return eval_arbol(arbol[1]) / eval_arbol(arbol[2])
    elif operador == '√':
        return math.sqrt(eval_arbol(arbol[1]))
    elif operador == 'sin':
        return math.sin(math.radians(eval_arbol(arbol[1])))
    elif operador == 'cos':
        return math.cos(math.radians(eval_arbol(arbol[1])))
    else:
        raise ValueError(f"Operador desconocido: {operador}")

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = float(p[1])