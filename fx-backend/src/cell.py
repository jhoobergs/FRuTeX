
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.expression = None
        
    def apply_expression(self, expression):
        self.expression = expression
        