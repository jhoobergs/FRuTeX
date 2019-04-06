from content import Content

class Float (Content):
    def __init__(self, value):
        super().__init__(float(value))
    
    def __repr__(self):
        return "Float: " + str(self.value)

class Integer (Content):
    def __init__(self, value):
        super().__init__(int(value))

    def __gt__(self, a):
        if(not isinstance(a, (Integer, Float))):
            print("WRONG CODE") # TODO throw right error
        return self.value > a.value
    
    def __repr__(self):
        return "Integer: " + str(self.value)
        