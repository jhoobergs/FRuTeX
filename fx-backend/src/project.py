import os
import json

from fx_exception import FXException
from file import File
from config import Config
from expression import Expression
from statement import Statement
from cell_range import CellRange

class Project:
    def __init__(self, directory='../testdir'):
        self.directory = directory
        self.files = {}
        self.config = None
        self.data = None
        self.cell_dict = {}

    def parse(self):
        if not 'config.fx' in os.listdir(self.directory):
            raise FXException('Every FRuTeX project needs a config file')
        
        fx_files = [filename for filename in os.listdir(self.directory)
            if os.path.splitext(filename)[1] == '.fx'
            and os.path.basename(filename) != 'config.fx']

        self.config = Config(self.directory + '/config.fx')
        self.config.parse()
    
        files = {}
        for filename in fx_files:
            file = File(self.directory + '/' + filename)
            file.parse()
            files.update({file.attrib: file})
            
        self.files = files
        
        for file in self.files.values():
            file.apply_statements(self.config, self.cell_dict, None)
    
    def generate_json(self):
        data = {"config": {}, "cells": {}}
        num_of_rows = self.config.values["num_rows"]
        num_of_cols = self.config.values["num_cols"]
        default_color = self.config.values["default_color"]
        
        data["config"]["num_of_rows"] = num_of_rows
        data["config"]["num_of_cols"] = num_of_cols
        data["config"]["default_color"] = default_color
        
        data["column_width"] = {str(i): self.config.values["default_width"] for i in range(int(num_of_cols))}
        data["row_height"] = {str(i): self.config.values["default_height"] for i in range(int(num_of_rows))}
        
        for cell in self.cell_dict.values():
            data["cells"][str(cell.row) + ', ' + str(cell.col)] = cell.to_json(self.config, self.cell_dict)
            
        self.data = data
            
        return json.dumps(data)
      
    def compact_all(self):
        for file in self.files.values():
            file.write_to_file()
            
    def update_expression(self, cell_pos, attrib, expression, save=False):
        #cell = self.cell_dict[cell_pos]
        
        new_json = self.files[attrib].apply_statements(self.config, self.cell_dict, [Statement(attrib, [CellRange((cell_pos[0], cell_pos[0] + 1), (cell_pos[1], cell_pos[1] + 1))], Expression(expression))])
        #new_json = cell.update_expression(attrib, Expression(expression), self.config, self.cell_dict)
        new_json = {str(key)[1:-1]: value for key, value in new_json.items()}
      
        if save: self.files[attrib].write_to_file()
      
        self.data["cells"].update(new_json)
        return json.dumps(self.data)
