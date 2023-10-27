"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """"Makes a new serial, with a start"""
        self.start = start 
        self.beginning = start

    def generate(self):
        """Return next serial"""
        if self.start == self.start:
            beginning = self.start
            self.start = self.start +1
            return beginning
        else:
            self.start = self.start +1
            return (self.start)
        
    def reset(self):
        """Resetst the value to the original start"""
        self.start = self.beginning

        

