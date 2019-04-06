from lark import Lark, Tree
from lark.indenter import Indenter
from fx_exception import FXException
from functools import reduce

def tree_to_repr(tree):
    print(tree)
   
    if type(tree) != Tree:
        return tree

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
        return CompareExpression(tree_to_repr(tree.children[0]), tree.children[1], tree_to_repr(tree.children[2]))
    elif tree.data == "arith_expr":
        return ArithExpression(list(map(tree_to_repr, tree.children)))
    elif tree.data == "term":
        return tree_to_repr(tree.children[0])
    elif(tree.data == "file_input"):
        return tree_to_repr(tree.children[0]) # TODO ? assumes only 1 main statement
    elif(tree.data == "suite"):
        return SuiteExpression([tree_to_repr(c) for c in tree.children])
    elif tree.data == "factor":
        return UnaryExpression(tree.children[0], tree_to_repr(tree.children[1]))
    elif tree.data == "power":
        return PowerExpression(tree_to_repr(tree.children[0]), tree_to_repr(tree.children[1]))

class FrutexIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 2
    
class Content:
    def __init__(self, value):
        self.value = value

    def eval(self, cell, attrib, cell_dict):
        return self
        
class Boolean (Content):
    def __init__(self, value):
        super().__init__(bool(value))
    
    def is_true(self):
        return self.value

    def __repr__(self):
        return "Boolean: " + str(self.value)


class Float (Content):
    def __init__(self, value):
        super().__init__(float(value))
        
    def __gt__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + str(type(other)))
            
        return Boolean(self.value > other.value)

    def __ge__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + str(type(other)))
            
        return Boolean(self.value >= other.value)
    
    def __lt__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + str(type(other)))
            
        return Boolean(self.value < other.value)
    
    def __le__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + str(type(other)))
            
        return Boolean(self.value <= other.value)
    
    def __eq__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + str(type(other)))
            
        return Boolean(self.value == other.value)
    
    def __ne__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + str(type(other)))
            
        return Boolean(self.value != other.value)
    
    def __pos__(self):
        return Float(+self.value)
    
    def __neg__(self):
        return Float(-self.value)
    
    def __add__(self, other):
        if isinstance(other, (Integer, Float)):
            return Float(self.value + other.value)
        
        else:
            raise FXException("Can't add Float to " + str(type(other)))
            
    def __sub__(self, other):
        if isinstance(other, (Integer, Float)):
            return Float(self.value - other.value)
        
        else:
            raise FXException("Can't subtract " + str(type(other)) + " from Float")
            
    def __mul__(self, other):
        if isinstance(other, (Integer, Float)):
            return Float(self.value * other.value)
        
        else:
            raise FXException("Can't multiply Float with " + str(type(other)))
            
    def __floordiv__(self, other):
        if isinstance(other, (Integer, Float)):
            return Float(self.value // other.value)
        
        else:
            raise FXException("Can't floor divide Float by " + str(type(other)))
            
    def __truediv__(self, other):
        if isinstance(other, (Integer, Float)):
            return Float(self.value / other.value)
        
        else:
            raise FXException("Can't divide Float by " + str(type(other)))
            
    def __mod__(self, other):
        if isinstance(other, (Integer, Float)):
            return Float(self.value % other.value)
        
        else:
            raise FXException("Can't calculate the modulo of a Float with a " + str(type(other)))
            
    def __pow__(self, other):
        if self.value < 0:
            if isinstance(other, Integer):
                return Float(self.value ** other.value)
            
            else:
                raise FXException("Can't raise a (negative) Float to the power of a " + str(type(other)))
                
        else:
            if isinstance(other, (Float, Integer)):
                return Float(self.value ** other.value)
            
            else:
                raise FXException("Can't raise a Float to the power of a " + str(type(other)))
            
    def __repr__(self):
        return "Float(" + str(self.value) + ')'


class Integer (Content):
    def __init__(self, value):
        super().__init__(int(value))

        
    def __gt__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + str(type(other)))
            
        return Boolean(self.value > other.value)

    def __ge__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + str(type(other)))
            
        return Boolean(self.value >= other.value)
    
    def __lt__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + str(type(other)))
            
        return Boolean(self.value < other.value)
    
    def __le__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + str(type(other)))
            
        return Boolean(self.value <= other.value)
    
    def __eq__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + str(type(other)))
            
        return Boolean(self.value == other.value)
    
    def __ne__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + str(type(other)))
            
        return Boolean(self.value != other.value)
    
    def __pos__(self):
        return Integer(+self.value)
    
    def __neg__(self):
        return Integer(-self.value)
    
    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value + other.value)
        
        elif isinstance(other, Float):
            return Float(self.value + other.value)
        
        else:
            raise FXException("Can't add Integer to " + str(type(other)))
            
    def __sub__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value - other.value)
                
        elif isinstance(other, Float):
            return Float(self.value - other.value)
        
        else:
            raise FXException("Can't subtract " + str(type(other)) + " from Integer")
            
    def __mul__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value * other.value)
        
        elif isinstance(other, Float):
            return Float(self.value * other.value)
        
        else:
            raise FXException("Can't multiply Integer with " + str(type(other)))
            
    def __floordiv__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value // other.value)
        
        elif isinstance(other, Float):
            return Float(self.value // other.value)
        
        else:
            raise FXException("Can't floor divide Integer by " + str(type(other)))
            
    def __truediv__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value / other.value)
        
        elif isinstance(other, Float):
            return Float(self.value / other.value)
        
        else:
            raise FXException("Can't divide Integer by " + str(type(other)))
            
    def __mod__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value % other.value)
        
        elif isinstance(other, Float):
            return Float(self.value % other.value)
        
        else:
            raise FXException("Can't calculate the modulo of a Integer with a " + str(type(other)))
            
    def __pow__(self, other):
        if self.value < 0:
            if isinstance(other, Integer):
                return Float(self.value ** other.value)
            
            else:
                raise FXException("Can't raise a (negative) Integer to the power of a " + str(type(other)))
                
        else:
            if isinstance(other, Float):
                return Float(self.value ** other.value)
            
            elif isinstance(other, Integer):
                return Integer(self.value ** other.value)
            
            else:
                raise FXException("Can't raise a Integer to the power of a " + str(type(other)))
                
    def __repr__(self):
        return "Integer(" + str(self.value) + ')'
        

class FrutexParser():
  def __init__(self):
    kwargs = dict(rel_to=__file__, postlex=FrutexIndenter(), start='file_input')
    self.parser = Lark.open('../assets/frutex.lark', parser='lalr', **kwargs)

  def parse(self, code):
    replaced = code.replace("\n  ", '\n')
    return self.parser.parse(replaced)
  
  def eval(self, cell, attrib, cell_dict):
    parsed_expression = self.parse(cell.expressions[attrib].text)
    repr = tree_to_repr(parsed_expression)
    print(repr)
    return repr.eval(cell, attrib, cell_dict)

class FrutexExpression():
  def eval(self, cell, attrib, cell_dict):
    raise Exception("Eval not implemented")
  
  def __repr__(self):
    return "FrutexExpression"

class CompoundExpression(FrutexExpression):
  def __init__(self, children):
    self.children = children
  
  def __repr__(self):
    return "CompoundExpression: " + " ".join([repr(c) for c in self.children])

class SuiteExpression(CompoundExpression):
  def __init__(self, children):
    super().__init__(children)
  
  def eval(self, cell, attrib, cell_dict):
    return [c.eval(cell, attrib, cell_dict) for c in self.children][-1]

class IfExpression(CompoundExpression):
  def __init__(self, children):
    super().__init__(children)
    
  def __repr__(self):
    return "IfExpression: " + " ".join([repr(c) for c in self.children])
  
  def eval_condition(self, lst, cell, attrib, cell_dict):
    if not lst:
        raise FXException("If statements need an else clause")
      
    if len(lst) == 1:
      return lst[0].eval(cell, attrib, cell_dict)
      
    else:
      if lst[0].eval(cell, attrib, cell_dict).is_true():
          return lst[1].eval(cell, attrib, cell_dict)
      else:
          return self.eval_condition(lst[2:], cell, attrib, cell_dict)
    
  def eval(self, cell, attrib, cell_dict):
    return self.eval_condition(self.children, cell, attrib, cell_dict)

class VarExpression(FrutexExpression):
  def __init__(self, name):
    self.name = name
  
  def eval(self, cell, attrib, cell_dict): # TODO
    if(self.name == "R"):
      return Integer(cell.row)
    elif(self.name == "C"):
      return Integer(cell.column)
    else:
      raise FXException("Unknown variable: " + self.name)
    ranges = File.parse_cell_ranges(name)
    if(len(ranges) > 1):
      raise FXException("Only 1 range can be specified as variable")
    coordinates = ranges[0].get_coordinates()
    if(len(coordinates) != 1):
      raise FXException("Only 1 cell can be specified as variable")
       
  
  def __repr__(self):
    return "VarExpression: " + self.name

comparators = {
  ">": lambda a, b: a > b,
  "<": lambda a, b: a < b,
  ">=": lambda a, b: a >= b,
  "<=": lambda a, b: a <= b,
  "==": lambda a, b: a == b,
  "!=": lambda a, b: a != b
}

operators = {
  "+": lambda a, b: a + b,
  "-": lambda a, b: a - b,
  "*": lambda a, b: a * b,
  "/": lambda a, b: a / b,
  "//": lambda a, b: a // b,
  "%": lambda a, b: a % b,
}

class CompareExpression(FrutexExpression):
  def __init__(self, a, comparator, b):
    self.a = a
    self.comparator = comparator
    self.b = b
  
  def eval(self, cell, attrib, cell_dict):
    return comparators[self.comparator](self.a.eval(cell, attrib, cell_dict), self.b.eval(cell, attrib, cell_dict))

  def __repr__(self):
    return "CompareExpression: " + repr(self.a) + " " + self.comparator + " " + repr(self.b)

class ArithExpression (FrutexExpression):
  def __init__(self, children):
    self.children = children
        
  def eval(self, cell, attrib, cell_dict):
    head, *tail = self.children
    tail = [(tail[i], tail[i + 1]) for i in range(0, len(tail), 2)]
    return reduce(lambda state, op_elem: operators[op_elem[0]](state, op_elem[1].eval(cell, attrib, cell_dict)), tail, head.eval(cell, attrib, cell_dict))
     
  def __repr__(self):
    return "ArithExpression: " + " ".join(map(repr, self.children))

class UnaryExpression (FrutexExpression):
    def __init__(self, op, elem):
        self.op = op
        self.elem = elem
        
    def eval(self, cell, attrib, cell_dict):
        if self.op == '-':
            return -self.elem
        elif self.op == '+':
            return +self.elem
        else:
            raise FXException()

class PowerExpression (FrutexExpression):
    def __init__(self, elem1, elem2):
        self.elem1 = elem1
        self.elem2 = elem2
        
    def eval(self, cell, attrib, cell_dict):
        return self.elem1.eval(cell, attrib, cell_dict) ** self.elem2.eval(cell, attrib, cell_dict)

class FuncExpression(FrutexExpression):
  def __init__(self, args):
    self.args = args

class ArgsFuncExpression(FuncExpression):
  def __init__(self, args):
    super()._init__(args)

  def eval(self, cell, attrib, cell_dict): 
    return func(self.args)
  
  def func():
    pass

class MinExpression(FuncExpression):
  def __init__(self, args):
    super()._init__(args)
  def func():
    return min

class MaxExpression(FuncExpression):
  def __init__(self, args):
    super()._init__(args)
  def func():
    return max