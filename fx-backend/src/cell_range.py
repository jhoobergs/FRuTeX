from fx_exception import FXException

class CellRange:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
                
        if type(rows) is not tuple:
            if rows is not None:
                if (':' not in rows):
                    rows += ':' + str(int(rows) + 1)
                self.rows = tuple(map(int, rows.split(':')))
                    
            if cols is not None:
                if (':' not in cols):
                    cols += ':' + str(int(cols) + 1)
                self.cols = tuple(map(int, cols.split(':')))
              
        
    def get_coordinates(self):
        if self.rows is None:
            return [(None, i) for i in range(self.cols[0], self.cols[1])]
          
        if self.cols is None:
            return [(i, None) for i in range(self.rows[0], self.rows[1])]
      
        return [(r, c) for c in range(self.cols[0], self.cols[1])
                       for r in range(self.rows[0], self.rows[1])]

    def size(self):
        if None in (self.rows, self.cols):
            return 0
          
        return (self.cols[1] - self.cols[0]) * (self.rows[1] - self.rows[0])
      
    def to_code(self):
        return ('R' + str(self.rows[0]) + (':' + str(self.rows[1])) * (self.rows[1] > self.rows[0] + 1) + ' ') * (self.rows is not None) + \
               ('C' + str(self.cols[0]) + (':' + str(self.cols[1])) * (self.cols[1] > self.cols[0] + 1)) * (self.cols is not None)
      