import constants

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.expressions = {}
        
    def apply_expression(self, attrib, expression):
        self.expressions[attrib] = expression
        
    def get_expression_text(self, attrib, config):
        if attrib in self.expressions:
            return self.expressions[attrib].text
        
        else:
            return config.get_default(attrib)
        
    def to_json(self, config):
        json = {}
        
        for attrib in constants.attrib_dict.values():
            json[attrib] = str(eval(self.get_expression_text(attrib, config).strip()))
            
        return json
        