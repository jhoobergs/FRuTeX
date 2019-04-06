import os
import re
from fx_exception import FXException 
from statement import Statement
from expression_parser import make_tree

def parse_file(path):
    with open(path, 'r') as file:
        text = file.readlines()
        
    statements = []
    matches = re.findall(r"^([^(\|=)]*)=((\s*\|((\s\s*..*(\n|))*))|([^\n\|]*))",
                         text,
                         re.MULTILINE)
    
    for match in matches:
        statements.append(Statement(match[0],
                                    make_tree(match[3] or match[1])))
        

def parse_project(directory):
    fx_files = [directory + '/' + filename for filename in os.listdir(directory)
                    if os.path.splitext(filename)[1] == '.fx']
    
    if not 'config.fx' in fx_files:
        raise FXException('Every FRuTeX project needs a config file')

    for path in fx_files:
        parse_file(path)
