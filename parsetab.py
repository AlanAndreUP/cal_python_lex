
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COSENO DIVIDE LPAREN MINUS NUMBER PLUS RAIZ RPAREN SENO TIMESexpression : expression PLUS term\n                  | expression MINUS termexpression : termterm : term TIMES factor\n            | term DIVIDE factorterm : factorfactor : NUMBERfactor : LPAREN expression RPARENfactor : SENO LPAREN expression RPAREN\n              | COSENO LPAREN expression RPAREN\n              | RAIZ LPAREN expression RPAREN'
    
_lr_action_items = {'NUMBER':([0,5,9,10,11,12,14,15,16,],[4,4,4,4,4,4,4,4,4,]),'LPAREN':([0,5,6,7,8,9,10,11,12,14,15,16,],[5,5,14,15,16,5,5,5,5,5,5,5,]),'SENO':([0,5,9,10,11,12,14,15,16,],[6,6,6,6,6,6,6,6,6,]),'COSENO':([0,5,9,10,11,12,14,15,16,],[7,7,7,7,7,7,7,7,7,]),'RAIZ':([0,5,9,10,11,12,14,15,16,],[8,8,8,8,8,8,8,8,8,]),'$end':([1,2,3,4,17,18,19,20,21,25,26,27,],[0,-3,-6,-7,-1,-2,-4,-5,-8,-9,-10,-11,]),'PLUS':([1,2,3,4,13,17,18,19,20,21,22,23,24,25,26,27,],[9,-3,-6,-7,9,-1,-2,-4,-5,-8,9,9,9,-9,-10,-11,]),'MINUS':([1,2,3,4,13,17,18,19,20,21,22,23,24,25,26,27,],[10,-3,-6,-7,10,-1,-2,-4,-5,-8,10,10,10,-9,-10,-11,]),'RPAREN':([2,3,4,13,17,18,19,20,21,22,23,24,25,26,27,],[-3,-6,-7,21,-1,-2,-4,-5,-8,25,26,27,-9,-10,-11,]),'TIMES':([2,3,4,17,18,19,20,21,25,26,27,],[11,-6,-7,11,11,-4,-5,-8,-9,-10,-11,]),'DIVIDE':([2,3,4,17,18,19,20,21,25,26,27,],[12,-6,-7,12,12,-4,-5,-8,-9,-10,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,5,14,15,16,],[1,13,22,23,24,]),'term':([0,5,9,10,14,15,16,],[2,2,17,18,2,2,2,]),'factor':([0,5,9,10,11,12,14,15,16,],[3,3,3,3,19,20,3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression','parser_calculadora.py',42),
  ('expression -> expression MINUS term','expression',3,'p_expression','parser_calculadora.py',43),
  ('expression -> term','expression',1,'p_expression_term','parser_calculadora.py',47),
  ('term -> term TIMES factor','term',3,'p_term','parser_calculadora.py',51),
  ('term -> term DIVIDE factor','term',3,'p_term','parser_calculadora.py',52),
  ('term -> factor','term',1,'p_term_factor','parser_calculadora.py',56),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser_calculadora.py',60),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parser_calculadora.py',64),
  ('factor -> SENO LPAREN expression RPAREN','factor',4,'p_factor_func','parser_calculadora.py',68),
  ('factor -> COSENO LPAREN expression RPAREN','factor',4,'p_factor_func','parser_calculadora.py',69),
  ('factor -> RAIZ LPAREN expression RPAREN','factor',4,'p_factor_func','parser_calculadora.py',70),
]
