from keras.datasets import mnist
from network import network
from neuron import neuron
from layer import layer
import math
# Load Data
(xtrain, ytrain), (xtest, ytest) = mnist.load_data()

# Format data as simple python lists
xformat = []
for i in xtrain:
    xformat.append(i.flatten().tolist())
xtrain = xformat
ytrain = ytrain.tolist()

def sigmoid(x):
    return 1 / (1 + math.e ** (0 - x))
            
def sigmoid_(x):
    return sigmoid(x) * ( 1 - sigmoid(x) )


# Initialize Network instance
"""
numLayers =     input("Number of Layers:      ")
numIn =         input("Number of inputs:      ")
hidLaySize =    input("Size of Hidden Layers: ")
outLaySize =    input("Size of output Layer:  ")
rate =    float(input("Learning Rate:         "))
net = network(numLayers, numIn, hidLaySize, outLaySize, rate)
"""

net = network(3, 784, 16, 10, 0.1)
net_updates = network(3, 784, 16, 10, 0.1)

for image_index in range(len(xtrain) - 1):
    yhat = [0] * 10
    yhat[ytrain[image_index]] = 1
    net.activate(xtrain[image_index])
    for layer in range(len(net.layers) - 1, 0, -1):
        newYhat = [0] * len(net.layers[layer - 1].neurons)
        for neuron_index in range(len(net.layers[layer].neurons) - 1):
            
            for weight in range(len(net.layers[layer].neurons[neuron_index].inputWeights) - 1):
                net.layers[layer - 1]
                net.layers[layer - 1].neurons[weight]
                net.layers[layer]
                net.layers[layer].neurons[neuron_index]
                yhat[neuron_index]

                del_w = 0.1 * net.layers[layer - 1].neurons[weight].activation * sigmoid_(net.layers[layer].neurons[neuron_index].sum) * (yhat[neuron_index] - net.layers[layer].neurons[neuron_index].activation )
                del_a = 0.1 * net.layers[layer].neurons[neuron_index].inputWeights[weight] * sigmoid_(net.layers[layer].neurons[neuron_index].sum) * (yhat[neuron_index] - net.layers[layer].neurons[neuron_index].activation )
                net.layers[layer].neurons[neuron_index].inputWeights[weight] += del_w
                newYhat[weight] += del_a



# -----------------------------------------------
# ------------------ARCHIVE----------------------
# -----------------------------------------------



"""

# This is some garbage code i made for like genetic algorithms or whatever, i thought i would try it but its super complicated
# For now i will leave the code.
# I might archive this soon

nets = []

for i in range(10):
    nets.append(network(3, 784, 16, 10, rate))

# nets contain 10 unique networks. we will run them each on 10 training cases

prev = 0
next = 10


while next <= len(xtrain):
    costs = []
    for net in nets:
        totsum = 0
        for i in range(prev, next):
            geuss = net.activate(xtrain[i])

            yans = [0] * 10
            yans[ytrain[i]] = 1
            cost = 0

            for j in range(len(yans)):
                cost += abs(geuss[j] - yans[j])
            cost = cost ** 2
            totsum += cost

        # end of individual net 10 tests
        costs.append(totsum / 10)
    # end of cycle through nets

    for i in range(len(costs)):
        print(i, costs[i])

    firsec = [0, 1]
    copcost = costs.copy()
    costs.sort()
    for i in [0, 1]:
        for j in range(len(copcost)):
            if copcost[j] == costs[i]:
                firsec[i] = j

    print("Net:", firsec[0], "came first  with cost:  ", costs[0])
    print("Net:", firsec[1], "came second with cost:  ", costs[1])
    # end of game, top contestents move onto next game

    newNets = []
    for i in firsec:
        newNets.append(nets[i])

        for j in range(4):
            newNet = network(3, 784, 16, 10, rate)
            newNet.n, newNet.w = nets[i].mutate()
            newNets.append(newNet)
    print(nets)
    nets = newNets.copy()
    print(newNets)

    next += 10
    prev += 10
"""