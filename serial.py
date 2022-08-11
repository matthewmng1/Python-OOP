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

    def __init__(self, start=0):
        """Makes the generator. Starts at whatever number is passed in or defaults to 0"""
        self.start = self.next = start

    def generate(self):
        """ adds one every time self.generate() is executed"""
        self.next +=1
        return self.next

    def reset(self):
        """ resets generator back to what it originally started at """
        self.next = self.start
        return self.start
