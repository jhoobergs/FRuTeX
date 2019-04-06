from file import File
import constants

class Config (File):
    def __init__(self, path):
        super().__init__(path)
        
        self.values = constants.default_config

    def get_default(self, attrib):
        return self.values[constants.attrib_to_default_dict[attrib]]

    def parse(self):
        with open(self.path, 'r') as file:
            lines = file.readlines()
            
        for line in lines:
            key, value = line.split('=')
            key = key.strip()
            value = value.strip()
            
            self.values[key] = value
