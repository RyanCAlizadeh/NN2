from neuron import neuron
from layer import layer
import random
import math
class network:

    def __init__(self, numLayers, numIn, hidLaySize, outLaySize, rate):
        layers = []
        layers.append(layer(hidLaySize, numIn))
        for lay in range(1, numLayers-1):
            layers.append(layer(hidLaySize, hidLaySize))
        layers.append(layer(outLaySize, hidLaySize))

        self.layers     = layers
        self.numLayers  = numLayers
        self.numIn      = numIn
        self.hidLaySize = hidLaySize
        self.outLaySize = outLaySize
        self.rate       = rate

    def activate(self, data):
        if len(data) != self.numIn:
            print("Error: Data size inconsistent with Network input size")
            return None

        self.layers[0].activate(data)

        for i in range(1, self.numLayers):
            data = []
            for neu in self.layers[i - 1].neurons:
                data.append(neu.activation)
            self.layers[i].activate(data)
        
        output = []
        for i in self.layers[self.numLayers - 1].neurons:
            output.append(i.activation)
        self.out = output
        return output

    def cost(self, data, yhat):
        y = self.activate(data)
        sum = 0
        for i in range(len(y)):
            sum += 0.5 * ( ( yhat[i] - y[i] ) ** 2)
        sum /= len(y)
        return sum





# -----------------------------------------------
# ------------------ARCHIVE----------------------
# -----------------------------------------------
        

"""
# Unnecessary for new weighting setup

        # Independantly declare weight between n[0] and inputs

        w.append([])
        for i in range(len(n[0])):# Independantly declare weight between n[0] and inputs
            w[0].append([])
            for j in range(numIn):
                w[0][i].append(random.random() * random.choice([-1, 1]) * (1/math.sqrt(numIn)))

        for i in range(len(n)):     # i is a layer index of n
            if i != 0:              # we have already done n[0]
                w.append([])
                for j in range(len(n[i])):      # j is a neuron
                    w[i].append([])
                    for k in n[i-1]:
                        w[i][j].append(random.random() * random.choice([-1, 1]) * (1/math.sqrt(len(n[i-1]))))

        # w is now declared, all weights have been initialized with random values from -1/d to 1/d
        # Access weight between neuron n[L][i1] and n[L - 1][i2]:
        # w[L][i1][i2]

        # Now declare learning rate (scale of mutation)
"""

        

"""
# unnecessary for backprop

    def mutate(self):
        n = self.n.copy()
        w = self.w.copy()

        for layer in n:
            for neuro in layer:
                neuro.b += random.choice([1, -1]) * random.random() * self.rate
        for layer in w:
            for inNeu in layer:
                for weights in inNeu:
                    weights += random.choice([1, -1]) * random.random() * self.rate
        return n, w
"""
