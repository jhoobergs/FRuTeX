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