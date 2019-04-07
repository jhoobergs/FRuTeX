from fx_exception import FXException

class CellRange:
    def __init__(self, rows, cols):
        if ':' not in rows:
            rows += ':' + str(int(rows) + 1)
            
            
        if ':' not in cols:
            cols += ':' + str(int(cols) + 1)
            
        self.rows = tuple(map(int, rows.split(':')))
        self.cols = tuple(map(int, cols.split(':')))
        
        if not (rows[1] > rows[0] and cols[1] > cols[0]):
            raise FXException('Invalid range: must be ascending')
        
    def get_coordinates(self):
        return [(r, c) for c in range(self.cols[0], self.cols[1])
                       for r in range(self.rows[0], self.rows[1])]
