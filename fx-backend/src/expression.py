
class Expression:
    def __init__(self, text):
        self.text = text
        
    def __str__(self):
        return "Expression(\n" + self.text + ")"
      
    def __bool__(self):
        return bool(self.text)
    