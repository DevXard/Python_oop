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
        self.start = start
        self.initial = start
        self.res = start

    def __repr__(self):
        return f"Serial Generator start = {self.start} next = {self.start + 1}"

    def generate(self):
        if self.start == self.initial:
            self.initial -=1
            return self.start
        else:
            self.start += 1
            return self.start
        
    def reset(self):
        
        self.start = self.res
        self.initial = self.res