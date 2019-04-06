import re

from statement import Statement
from expression import Expression
from fx_exception import FXException
from cell_range import CellRange

class File:
    def __init__(self, path):
        self.path = path
        self.statements = None
        
    @staticmethod
    def parse_cell_ranges(text):
        text = ''.join(text.split())
        
        cell_ranges = []
        cell_ranges_str = text.split(',')
        for cell_range_str in cell_ranges_str:
            matches = re.findall(r"([rcRC][0-9]+(:[0-9]+)?)", cell_range_str)
            matches = {s[0][0].upper(): s[0][1:] for s in matches}
            
            if len(matches) == 0:
                raise FXException("Invalid syntax")
                
            if len(matches) == 1:
                raise FXException("Infinite ranges not yet implemented")
                
            cell_ranges.append(CellRange(matches.get('R'), matches.get('C')))
            
            return cell_ranges
        
    def parse(self):
        with open(self.path, 'r') as file:
            text = file.read()
            
        statements = []
        matches = re.findall(r"^([^(\|=)]*)=((\s*\|((\s\s*..*(\n|))*))|([^\n\|]*))",
                             text,
                             re.MULTILINE)
        
        for match in matches:
            statements.append(Statement(File.parse_cell_ranges(match[0]),
                                        Expression(match[3] or match[1])))
        
        self.statements = statements
        
            
        
        