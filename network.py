from neuron import neuron
import random
from keras.datasets import mnist
import math

class network:

    def __init__(self, numLayers, numIn, hidLaySize, outLaySize, rate):
        laySizes = []
        for i in range(numLayers - 1):
            laySizes.append(hidLaySize)
        laySizes.append(outLaySize)
        counter = 0

        w = []
        n = []

        for i in laySizes:
            n.append([])
            for j in range(i):
                n[counter].append(neuron(0.0001))
            counter += 1

        # n is now declared, neurons have all been initialized.
        # L = layer
        # i = index in layer
        # Access specific neuron at n[L][i]

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

        self.rate = rate
        self.n = n
        self.w = w
    
    def activate(self, data):
        if len(data) * len(data[0]) != len(self.w[0][0]):
            print("Error, data size not compatible with initialized network. Returning \"none\"")
            return None

        ins = []
        for i in data:
            for j in i:
                ins.append(j)
        sunm = 0
        out = []

        for layer in range(len(self.w)):
            out = []
            for j in range(len(self.w[layer])):
                sum = 0
                for k in range(len(self.w[layer][j])):
                    sum += ins[k] * self.w[layer][j][k]
                sum += self.n[layer][j].b
                sum = 1 / (1 + math.e ** (0 - sum))
                out.append(round(sum, 4))
            ins = out
        return out

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