from content import Content
from fx_exception import FXException

class Float (Content):
    def __init__(self, value):
        super().__init__(float(value))
        
    def __gt__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + type(other))
            
        return self.value > other.value

    def __ge__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + type(other))
            
        return self.value >= other.value
    
    def __lt__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + type(other))
            
        return self.value < other.value
    
    def __le__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + type(other))
            
        return self.value <= other.value
    
    def __eq__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + type(other))
            
        return self.value == other.value
    
    def __ne__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Float to " + type(other))
            
        return self.value != other.value
    
    def __repr__(self):
        return "Float(" + str(self.value) + ')'

class Integer (Content):
    def __init__(self, value):
        super().__init__(int(value))

        
    def __gt__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + type(other))
            
        return self.value > other.value

    def __ge__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + type(other))
            
        return self.value >= other.value
    
    def __lt__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + type(other))
            
        return self.value < other.value
    
    def __le__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + type(other))
            
        return self.value <= other.value
    
    def __eq__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + type(other))
            
        return self.value == other.value
    
    def __ne__(self, other):
        if not isinstance(other, (Integer, Float)):
            raise FXException("Can't compare Integer to " + type(other))
            
        return self.value != other.value
    
    
    def __repr__(self):
        return "Integer(" + str(self.value) + ')'
        