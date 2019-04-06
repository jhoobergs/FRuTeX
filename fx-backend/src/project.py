import os
import json

from fx_exception import FXException
from file import File
from config import Config

class Project:
    def __init__(self, directory='../testdir'):
        self.directory = directory
        self.files = []
        self.config = None
        self.cell_dict = {}

    def parse(self):
        if not 'config.fx' in os.listdir(self.directory):
            raise FXException('Every FRuTeX project needs a config file')
        
        fx_files = [filename for filename in os.listdir(self.directory)
            if os.path.splitext(filename)[1] == '.fx'
            and os.path.basename(filename) != 'config.fx']

        self.config = Config(self.directory + '/config.fx')
        self.config.parse()
    
        files = []
        for filename in fx_files:
            file = File(self.directory + '/' + filename)
            file.parse()
            files.append(file)
            
        self.files = files
        
        for file in self.files:
            file.apply_statements(self.cell_dict)
    
    def generate_json(self):
        data = {"cells": {}}
        
        for cell in self.cell_dict.values():
            data["cells"][str(cell.row) + ', ' + str(cell.col)] = cell.to_json(self.config)
            
        return json.dumps(data)
        