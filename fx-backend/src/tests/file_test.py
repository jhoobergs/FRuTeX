import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from file import File

f = File("content.fx")
f.expressions = {
  "5": [(0,0),(1,0), (2,0)],
  "4": [(3,0),(4,0), (3,1),(4,1)]
}
print([["Range " + str((l.rows, l.cols)) for l in items] for items in f.compact().values()])