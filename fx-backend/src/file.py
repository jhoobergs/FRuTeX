import re
import os

from statement import Statement
from expression import Expression
from fx_exception import FXException
from cell_range import CellRange
import constants

class File:
    def __init__(self, path):
        self.path = path
        self.statements = []
        self.attrib = None
        self.expressions = {}
        
        if 'config.fx' != os.path.basename(self.path):
            try:
                self.attrib = constants.attrib_dict[os.path.basename(path)[:-3]]
            except KeyError:
                raise FXException('Invalid file name: ' + os.path.basename(path))            
        
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
            statements.append(Statement(self.attrib,
                                        File.parse_cell_ranges(match[0]),
                                        Expression(match[3] or match[1])))
        
        self.statements = statements
        
    def apply_statements(self, config, cell_dict, statements=None):
        for statement in (statements, self.statements)[statements is None]:
            coordinates = [coordinates for cell_range in statement.cell_ranges for coordinates in cell_range.get_coordinates() if coordinates in self.expressions]
            for coordinate in coordinates:
                self.expressions[cell_dict[coordinate].expressions[statement.attrib].text].discard(coordinates)
           
            result = statement.apply(config, cell_dict, statements is not None)
            
            coordinates = [cs for cell_range in statement.cell_ranges for cs in cell_range.get_coordinates()]
            for coordinate in coordinates:
                self.expressions[cell_dict[coordinate].expressions[statement.attrib].text] = self.expressions.get(cell_dict[coordinate].expressions[statement.attrib].text, set()) | set([coordinate])
                
        return result

    def compact(self):
        exp_to_compact_ranges = {}
        positions_done = {}
        for expression, coordinates in self.expressions.items():
            exp_to_compact_ranges[expression] = set()
            s = exp_to_compact_ranges[expression]
            for row, col in coordinates:
                if positions_done.get((row,col), False):
                    continue

                longest = None
                best_length = 0

                old_ranges = [CellRange((row,row+1),(col,col+1))]
                while(len(old_ranges) > 0):
                    new_ranges = [CellRange((current_range.rows[0] + step2[0], current_range.rows[1] + step2[1]), (current_range.cols[0] + step1[0], current_range.cols[1] + step1[1])) for step2 in [(0,1),(-1,0),(0,0)] for step1 in [(-1,0),(0,1),(0,0)] if step1 != step2 or step1 != (0,0) for current_range in old_ranges]
                    #print([(new_range.rows, new_range.cols) for new_range in new_ranges])
                    new_ranges = list(filter(lambda x: sum([(not coord in coordinates) or positions_done.get(coord, False) for coord in x.get_coordinates()]) == 0, new_ranges))
                    #print([(new_range.rows, new_range.cols) for new_range in new_ranges])
                    largest = max([old.size() for old in old_ranges])
                    if(largest > best_length):
                        longest = list(filter(lambda x: x.size() == largest, old_ranges))[0]
                    if(len(new_ranges) == 0):                        
                        s.add(longest)
                        for pos in longest.get_coordinates():
                            positions_done[pos] = True
                    old_ranges = new_ranges
        return exp_to_compact_ranges
      
    def to_code(self):
        code = ""
        
        for expression, cell_ranges in self.compact().items():
            if not cell_ranges:
                continue
              
            print(cell_ranges)
            cell_ranges = list(cell_ranges)
          
            for cell_range in cell_ranges[:-1]:
                code += cell_range.to_code() + ',\n'
            code += cell_ranges[-1].to_code() + ' = '
            
            code += expression + '\n'
            
        return code
      
    def write_to_file(self):
        with open(self.path, 'w+') as file:
            file.write(self.to_code())
