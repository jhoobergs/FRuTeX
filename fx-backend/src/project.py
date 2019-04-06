import os

from fx_exception import FXException
from file import File

class Project:
    def __init__(self, directory='../testdir'):
        self.directory = directory
        self.files = None
        
    def parse(self):
        fx_files = [filename for filename in os.listdir(self.directory)
            if os.path.splitext(filename)[1] == '.fx']

        if not 'config.fx' in fx_files:
            raise FXException('Every FRuTeX project needs a config file')
    
        files = []
        for filename in fx_files:
            file = File(self.directory + '/' + filename)
            file.parse()
            files.append(file)
            
        self.files = files
            