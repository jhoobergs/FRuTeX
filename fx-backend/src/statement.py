from fx_exception import FXException
from cell import Cell

class Statement:
    def __init__(self, cell_ranges, expression):
        self.cell_ranges = cell_ranges
        self.expression = expression
        
    def apply(self, cell_dict):
        for cell_range in self.cell_ranges:
            for r, c in cell_range.get_coordinates():
                cell_dict.get((r, c), Cell(r, c)).apply_expression(self.expression)
        
        