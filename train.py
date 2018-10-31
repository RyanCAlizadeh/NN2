from keras.datasets import mnist
from network import network
from neuron import neuron
(xtrain, ytrain), (xtest, ytest) = mnist.load_data()

xformat = []
for i in xtrain:
    xformat.append(i.flatten().tolist())
yformat = ytrain.tolist()

nets = []

"""
hidLaySize = int(input("Size of layer " + str(i) + ": "))
outLaySize = int(input("Size of ouput layer: "))
"""


for i in range(10):
nets.append(network(3, 784, 16, 9))

# nets contain 10 unique networks. we will run them each on 10 training cases
prev = 0
next = 10
sum = 0
totSum = 0


for net in nets:
    for i in range(prev, next):
        geuss = net.activate(xtrain[i])
        cost = 1 - geuss[ytrain[i]]
        for conf in geuss:
            cost += conf
        cost -= geuss[ytrain[i]]
        cost = cost ** 2
    totSum += cost
    

    next += 10
    prev += 10