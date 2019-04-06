
class Cell:
    def __init__(self, row, col, content=None, color=None):
        self.row = row
        self.col = col
        self.content = content
        self.color = color
        
    def assign_content(self, content):
        self.content = content
        
    def assign_color(self, color):
        self.color = color
        