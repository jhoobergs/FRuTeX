from lark import Lark, Tree
from fx_exception import FXException
from functools import reduce

functions = {
    "min": lambda args : MinExpression(args),
    "max": lambda args: MaxExpression(args)
}

def tree_to_repr(tree):
    print(tree)
   
    if type(tree) != Tree:
        return tree

    if(tree.data == "integer"):
        return Integer(tree.children[0].value)
    elif(tree.data == "float"):
        return Float(tree.children[0].value)
    elif(tree.data == "var"):
        return VarExpression(tree.children[0].value)
    elif(tree.data == "if_exp"):
        return IfExpression([tree_to_repr(c) for c in tree.children])
    elif(tree.data == "comp_exp"):
        return CompareExpression(tree_to_repr(tree.children[0]), tree.children[1], tree_to_repr(tree.children[2]))
    elif tree.data in ["add_exp", "term_exp"] :
        return ArithExpression(list(map(tree_to_repr, tree.children)))
    elif tree.data == "factor":
        return UnaryExpression(tree.children[0].value, tree_to_repr(tree.children[1]))
    elif tree.data == "pow_exp":
        return PowerExpression(tree_to_repr(tree.children[0]), tree_to_repr(tree.children[1]))
    elif tree.data == "funccall":
        return functions[tree.children[0].value](list(map(tree_to_repr, tree.children[1].children)))

class ConstExpression:
    def __init__(self, value):
        self.value = value

    def eval(self, cell, attrib, cell_dict):
        return self
        
class Boolean (ConstExpression):
    def __init__(self, value):
        super().__init__(bool(value))
    
    def is_true(self):
        return self.value

    def __repr__(self):
        return "Boolean: " + str(self.value)


class Float (ConstExpression):
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


class Integer (ConstExpression):
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
    self.parser = Lark(r"""
        ?expr: if_exp
            | value
            | comp_exp
            | add_exp
        ?if_exp: "if" "(" expr ")" expr ["else" expr] 
        ?comp_exp: expr _comp_op expr
        ?add_exp: term_exp (_add_op term_exp)*
        ?term_exp: factor (_mult_op factor)*
        ?factor: _factor_op factor | pow_exp
        ?pow_exp: value ["**" factor]
        ?value: float
        | integer
        | "(" expr ")"
        | "true" -> true
        | "false" -> false
        | NAME "(" [arguments] ")" -> funccall
        | NAME -> var
        | string
        
        string : ESCAPED_STRING
        integer: INT
        float: DECIMAL

        arguments: expr ("," expr)*

        !_comp_op: ">"|"<"|">="|"<="|"=="|"!="
        !_mult_op: "*"|"/"|"//"|"%"
        !_factor_op: "+"|"-"
        !_add_op: "+"|"-"
        NAME: /[a-zA-Z_][\w:]*/

        %import common.DECIMAL
        %import common.INT
        %import common.ESCAPED_STRING
        %import common.SIGNED_NUMBER
        %import common.WS
        %ignore WS

        """, start='expr')

  def parse(self, code):
    replaced = code.text.replace("\n  ", '\n')
    return self.parser.parse(replaced)
  
  def eval(self, cell, attrib, cell_dict):
    parsed_expression = self.parse(cell.expressions[attrib])
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
    super().__init__(args)

  def eval(self, cell, attrib, cell_dict): 
    return self.func()(self.args)
  
  def func(self):
    pass

class MinExpression(ArgsFuncExpression):
  def __init__(self, args):
    super().__init__(args)
  def func(self):
    return min

class MaxExpression(ArgsFuncExpression):
  def __init__(self, args):
    super().__init__(args)
  def func(self):
    return max