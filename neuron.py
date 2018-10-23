import math
class neuron:

    def __init__(self, b):
        self.b = b
    
    def output(self, ins):
        
        x = sum(ins) + self.b

        sig = 1 / (1 + math.e ^ (0 - x))

        return sig