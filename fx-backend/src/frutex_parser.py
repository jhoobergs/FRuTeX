from lark import Lark
from lark.indenter import Indenter
from number_type import *
from boolean_type import *

def tree_to_repr(tree):
    #print(tree)
    if(tree.data == "number"):
      if(tree.children[0].type == "DEC_NUMBER"):
        return Integer(tree.children[0].value)
      elif(tree.children[0].type == "FLOAT_NUMBER"):
        return Float(tree.children[0].value)
    elif(tree.data == "var"):
        return VarExpression(tree.children[0].value)
    elif(tree.data == "compound_stmt"):
      if(tree.children[0].data == "if_stmt"):
        return IfExpression([tree_to_repr(c) for c in tree.children[0].children])
    elif(tree.data == "comparison"):
        return CompareExpression(tree_to_repr(tree.children[0]), tree.children[1].value, tree_to_repr(tree.children[2]))
    elif(tree.data == "file_input"):
        return tree_to_repr(tree.children[0]) # TODO ? assumes only 1 main statement
    elif(tree.data == "suite"):
        return SuiteExpression([tree_to_repr(c) for c in tree.children])

class FrutexIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 2

class FrutexParser():
  def __init__(self):
    kwargs = dict(rel_to=__file__, postlex=FrutexIndenter(), start='file_input')
    self.parser = Lark.open('../assets/frutex.lark', parser='lalr', **kwargs)

  def parse(self, code):
    replaced = code.replace("\n  ", '\n')
    return self.parser.parse(replaced)
  
  def eval(self, cell, attrib, cell_dict):
    parsed_expression = self.parse(cell.expressions[attrib])
    repr = tree_to_repr(parsed_expression)
    print(repr)
    return repr.eval()

class FrutexExpression():
  def eval(self):
    raise Exception("Eval not implemented")
  
  def __repr__(self):
    return "FrutexExpression"

class CompoundExpression(FrutexExpression):
  def __init__(self, children):
    self.children = children
  
  def __repr__(self):
    return "CompoundExpression: " + " ".join([c.__repr__() for c in self.children])

class SuiteExpression(CompoundExpression):
  def __init__(self, children):
    super().__init__(children)
  
  def eval(self):
    return [c.eval() for c in self.children][-1]

class IfExpression(CompoundExpression):
  def __init__(self, children):
    super().__init__(children)
  
  def eval(self): # TODO: elifs
    conditionEval = self.children[0].eval()
    if(conditionEval.is_true()):
      return self.children[1].eval()
    else:
      return self.children[2].eval()

class VarExpression(FrutexExpression):
  def __init__(self, name):
    self.name = name
  
  def eval(self): # TODO
    pass
  
  def __repr__(self):
    return "VarExpression: " + self.name

comparators = {
  ">": lambda a,b: a > b,
  "<": lambda a,b: a < b,
  ">=": lambda a,b: a >= b,
  "<=": lambda a,b: a <= b,
  "==": lambda a,b: a == b,
  "!=": lambda a,b: a != b
}
class CompareExpression(FrutexExpression):
  def __init__(self, a, comparator, b):
    self.a = a
    self.comparator = comparator
    self.b = b
  
  def eval(self):
    return Boolean(comparators[self.comparator](self.a, self.b))

  def __repr__(self):
    return "CompareExpression: " + self.a.__repr__() + " " + self.comparator + " " + self.b.__repr__()
