from content import Content

class Boolean (Content):
    def __init__(self, value):
        super().__init__(bool(value))
    
    def is_true(self):
        return self.value

    def __repr__(self):
        return "Boolean: " + str(self.value)

        