import constants
import frutex_parser

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.expressions = {}
        self.evaluated_expressions = {}
        self.dependents = {}
        self.dependent_of = {}
        
    def add_dependent(self, dep_cell, dep_attrib, this_attrib):
        self.dependents[this_attrib] = self.dependents.get(this_attrib, set()) | set([(dep_cell, dep_attrib)])
        dep_cell.dependent_of[dep_attrib] = dep_cell.dependent_of.get(dep_attrib, set()) | set([(self, this_attrib)])
        
    def apply_expression(self, attrib, expression):
        self.expressions[attrib] = expression
        self.evaluated_expressions[attrib] = None
        for c, a in self.dependent_of.get(attrib, set()):
          c.dependents.get(a, set()).discard((self, attrib))
          
    def refresh(self, attrib, config, cell_dict):
        self.evaluated_expressions[attrib] = None
        d = {(self.row, self.col): self.to_json(config, cell_dict)}
        
        for c, a in self.dependents.get(attrib, set()):
            d.update(c.refresh(a, config, cell_dict))
            
        return d
          
    def update_expression(self, attrib, expression, config, cell_dict):
        self.apply_expression(attrib, expression)
        return self.refresh(attrib, config, cell_dict)
        
    def get_expression_text(self, attrib, config, cell_dict):
        result = self.get_expression_result(attrib, config, cell_dict)
        
        if result is None:
          return config.get_default(attrib)
        
        else:
          return str(result.value)
          
    def get_expression_result(self, attrib, config, cell_dict):
        e = self.evaluated_expressions.get(attrib)
        if e is not None:
            return e
        else:
            expr_result = frutex_parser.FrutexParser().eval(self, attrib, config, cell_dict)
            self.evaluated_expressions[attrib] = expr_result
            
            return expr_result
        
    def to_json(self, config, cell_dict):
        json = {}
        
        for attrib in constants.attrib_dict.values():
            json[attrib] = self.get_expression_text(attrib, config, cell_dict)
            
        return json
        