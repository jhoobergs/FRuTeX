
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.expressions = {}
        
    def apply_expression(self, attrib, expression):
        self.expressions[attrib] = expression
        