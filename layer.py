import math
from neuron import neuron
class layer:
    def __init__(self, size, numIn):
        w_initialization = [0 - math.sqrt(1 / numIn), math.sqrt(1 / numIn)]
        neurons = []
        for i in range(size):
            neurons.append(neuron(0.0001, numIn, w_initialization))

        self.neurons = neurons
        self.size = size
        self. numIn = numIn
    
    def activate(self, inputValues):
        if len(inputValues) != self.numIn:
            print("Error: Number of inputs does not match layer input parametres")
            return None

        for neuronIndex in range(len(self.neurons)):
            self.neurons[neuronIndex].activate(inputValues)