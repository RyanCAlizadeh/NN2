import math
import random
class neuron:

    def __init__(self, bias, numIn, w_initialization):
        
        inputWeights = [0] * numIn
        for i in range(len(inputWeights)):
            inputWeights[i] = random.uniform(w_initialization[0], w_initialization[1])
        self.inputWeights = inputWeights
        self.bias = bias
        self.activation = 0
        self.numIn = numIn

    
    def activate(self, inputValues):
        
        if len(inputValues) != self.numIn:
            print("Error: number of weights does not match number of inputs")
            return None

        sum = 0

        for i in range(len(inputValues)):
            sum += inputValues[i] * self.inputWeights[i]

        sum += self.bias

        sig = 1 / (1 + math.e ** (0 - sum))

        self.activation = sig


def sigmoid(x):
    return 1 / (1 + math.e ** (0 - sum))
def sigmoid_(x):
    return sigmoid(x) * ( 1 - sigmoid(x) )
