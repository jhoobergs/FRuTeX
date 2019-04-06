import os
from fx_exception import FXException

def parse_config_file(path):
    

def parse_values(path):
    with open(path, 'r') as file:
        text = file.readlines()
        
    

    
    
    
"""-------------------------------------------------------------------------"""     
"""                                                                         """     
"""-------------------------------------------------------------------------"""    
    
def parse_file(path):
    basename, ext = os.path.splitext(filename)
    
    if ext != '.fx':
        return
    
    if basename == 'values':
        parse_values(filename)

def parse_project(directory):
    fx_files = [filename for filename in os.listdir(directory)
                    if os.path.splitext(filename)[1] == '.fx']
    
    if not 'config.fx' in fx_files:
        raise FXException('Every FRuTeX project needs a config file')

    parse_config_file(directory + '/config.fx')
