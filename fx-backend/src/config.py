from file import File
import constants

class Config (File):
    def __init__(self, path, statements):
        self.defaults = constants.default_config

    def get_default(self, attrib):
        return self.defaults[constants.attrib_to_default_dict[attrib]]
