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
assert fp.eval(c, "content", None, None).value == 5 


c.expressions["content"] = Expression("""
  if (7 < 5)
    5
  else
    7
""")
assert fp.eval(c, "content", None, None).value == 7


c.expressions["content"] = Expression("""
  if (7 != 5)
    4
  else
    5
""")
assert fp.eval(c, "content", None, None).value == 4

c.expressions["content"] = Expression("""
  if (7 != 7.0)
    4
  else
    5
""")
assert fp.eval(c, "content", None, None).value == 5

c.expressions["content"] = Expression("""
  -5 ++ 4
""")
assert fp.eval(c, "content", None, None).value == -1

c.expressions["content"] = Expression("""
  3**4
""")
assert fp.eval(c, "content", None, None).value == 3**4

c.expressions["content"] = Expression("""
  if (7 > 5)
    5
  else
    7
""")

assert fp.eval(c, "content", None, None).value == 5 
c.expressions["content"] = Expression("""
  if (7 < 5)
    5
  else
    7
""")
assert fp.eval(c, "content", None, None).value == 7

c.expressions["content"] = Expression("""
 max(1,2,3)
""")
assert fp.eval(c, "content", None, None).value == 3

c.expressions["content"] = Expression("""
  if (min(7, 5, 6) < 5)
    5
  else
    7
""")
assert fp.eval(c, "content", None, None).value == 7

c.expressions["content"] = Expression("""
  if (5 * 6 == 1)
    4 + 67
  else
    3 // 2
""")
assert fp.eval(c, "content", None, None).value == 1

c.expressions["content"] = Expression("""
  if (5 * 6 == 1)
    4 + 67
  elif (7 == 7)
    85
  else
    3 // 2
""")
assert fp.eval(c, "content", None, None).value == 85

c.expressions["content"] = Expression("""
  if (5 * 6 == 1 or 6 == 6)
    4 + 67
  elif (7 == 7)
    85
  else
    3 // 2
""")
assert fp.eval(c, "content", None, None).value == 71

c.expressions["content"] = Expression("""
  if (false)
    4 + 67
  elif (true)
    85
  else
    3 // 2
""")
assert fp.eval(c, "content", None, None).value == 85

c.expressions["content"] = Expression("""
  if (not true)
    4 + 67
  elif (not false)
    85
  else
    3 // 2
""")
assert fp.eval(c, "content", None, None).value == 85

c.expressions["content"] = Expression("""
  4 + 5 * 6
""")
assert fp.eval(c, "content", None, None).value == 34

c.expressions["content"] = Expression("""
  (4 + 5) * 6
""")
assert fp.eval(c, "content", None, None).value == 54

c.expressions["content"] = Expression("""
  if((4 + 5) * 6 == 54)
    1
  else
    0
""")
assert fp.eval(c, "content", None, None).value == 1

c.expressions["content"] = Expression("""
  if(54 == 6 * (4 + 5))
    1
  else
    0
""")
assert fp.eval(c, "content", None, None).value == 1

c.expressions["content"] = Expression("""
  if(54 == 6 * (4 + 5))
    "Blue"
  else
    "Red"
""")
assert fp.eval(c, "content", None, None).value == "Blue"