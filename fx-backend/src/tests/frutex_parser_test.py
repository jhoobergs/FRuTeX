import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from frutex_parser import FrutexParser
from project import Project
from cell import Cell
from expression import Expression

fp = FrutexParser()
c = Cell(0,0)
c.expressions["content"] = Expression("""
  if (7 > 5)
    5
  else
    7
""")
assert fp.eval(c.expressions["content"].text).value == 5 


c.expressions["content"] = Expression("""
  if (7 < 5)
    5
  else
    7
""")
assert fp.eval(c.expressions["content"].text).value == 7


c.expressions["content"] = Expression("""
  if (7 != 5)
    4
  else
    5
""")
assert fp.eval(c.expressions["content"].text).value == 4

c.expressions["content"] = Expression("""
  if (7 != 7.0)
    4
  else
    5
""")
assert fp.eval(c.expressions["content"].text).value == 5

c.expressions["content"] = Expression("""
  -5 ++ 4
""")
assert fp.eval(c.expressions["content"].text).value == -1

c.expressions["content"] = Expression("""
  3**4
""")
assert fp.eval(c.expressions["content"].text).value == 3**4

c.expressions["content"] = Expression("""
  if (1 == 2)
    5
  else
    if (1 == 3)
      6
    elif (2 == 2)
      7
    else
      8
""")
assert fp.eval(c.expressions["content"].text).value == 7

