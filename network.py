from neuron import neuron
import random
from keras.datasets import mnist
import math

class network:

    def __init__(self, numLayers, numIn):
        laySizes = []
        for i in range(numLayers - 1):
            laySizes.append(int(input("Size of layer " + str(i) + ": ")))
        laySizes.append(int(input("Size of output layer: ")))
        counter = 0

        w = []
        n = []

        for i in laySizes:
            n.append([])
            for j in range(i):
                n[counter].append(neuron(-75))
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
                w[0][i].append(random.random() * 10)

        for i in range(len(n)):     # i is a layer index of n
            if i != 0:              # we have already done n[0]
                w.append([])
                for j in range(len(n[i])):      # j is a neuron
                    w[i].append([])
                    for k in n[i-1]:
                        w[i][j].append(random.random() * 10)

        # w is now declared, all weights have been initialized with random values
        # Access weight between neuron n[L][i1] and n[L - 1][i2]:
        # w[L][i1][i2]

        self.n = n
        self.w = w
    
    def activate(self, data):
        if len(data) != len(self.w[0][0]):
            print("Error, data size not compatible with initialized network. Returning \"none\"")
            return None

        ins = data
        sunm = 0
        out = []

        for i in range(len(self.w)):
            out = []
            for j in range(len(self.w[i])):
                sum = 0
                for k in range(len(self.w[i][j])):
                    sum += ins[k] * self.w[i][j][k]
                sum += self.n[i][j].b
                sum = 1 / (1 + math.e ** (0 - sum))
                out.append(sum)
            ins = out
        
        return out