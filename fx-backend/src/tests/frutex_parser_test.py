import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from frutex_parser import FrutexParser
from project import Project
from cell import Cell

fp = FrutexParser()
c = Cell(0,0)
c.expressions["content"] = """
  if (7 > 5)
    5
  else
    7
"""
assert fp.eval(c, "content", None).value == 5 


c.expressions["content"] = """
  if (7 < 5)
    5
  else
    7
"""
assert fp.eval(c, "content", None).value == 7


c.expressions["content"] = """
  if (7 != 5)
    4
  else
    5
"""
assert fp.eval(c, "content", None).value == 4

c.expressions["content"] = """
  if (7 != 7.0)
    4
  else
    5
"""
assert fp.eval(c, "content", None).value == 5

c.expressions["content"] = """
  -5 ++ 4
"""
assert fp.eval(c, "content", None).value == -1

c.expressions["content"] = """
  3**4
"""
assert fp.eval(c, "content", None).value == 3**4
