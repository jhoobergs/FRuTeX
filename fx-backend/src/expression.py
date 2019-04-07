
class Expression:
    def __init__(self, text):
        self.text = text
        self.dependents = set()
        
    def __str__(self):
        return "Expression(\n" + self.text + ")"
      
    def add_dependent(self, dependent):
        self.dependents.add(dependent)
    