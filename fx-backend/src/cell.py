import constants
import frutex_parser

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.expressions = {}
        self.evaluated_expressions = {}
        
    def apply_expression(self, attrib, expression):
        self.expressions[attrib] = expression
        self.evaluated_expressions[attrib] = None
        
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
        