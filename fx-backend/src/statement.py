from cell import Cell
from expression import Expression

class Statement:
    def __init__(self, attrib, cell_ranges, expression):
        self.attrib = attrib
        self.cell_ranges = cell_ranges
        self.expression = expression
        
    def apply(self, config, cell_dict, update=False):
        for cell_range in self.cell_ranges:
            for r, c in cell_range.get_coordinates():
                if (r, c) not in cell_dict:
                    cell_dict[(r, c)] = Cell(r, c)

                if not update:
                    cell_dict[(r, c)].apply_expression(self.attrib, Expression(self.expression.text))
                else:
                    return cell_dict[(r, c)].update_expression(self.attrib, self.expression, config, cell_dict)
        
        