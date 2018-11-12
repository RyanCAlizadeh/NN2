from keras.datasets import mnist
from network import network
from neuron import neuron
(xtrain, ytrain), (xtest, ytest) = mnist.load_data()

xformat = []
for i in xtrain:
    xformat.append(i.flatten().tolist())
ytrain = ytrain.tolist()

nets = []

"""
hidLaySize = int(input("Size of layer " + str(i) + ": "))
outLaySize = int(input("Size of ouput layer: "))
"""


for i in range(10):
    nets.append(network(3, 784, 16, 10))

# nets contain 10 unique networks. we will run them each on 10 training cases

prev = 0
next = 10


costs = []
for net in nets:
    totsum = 0
    for i in range(prev, next):
        geuss = net.activate(xtrain[i])
        
        print(geuss)
        print("break")
        print(ytrain[i])

        yans = [0] * 10
        yans[ytrain[i]] = 1
        cost = 0
        print(yans)

        for j in range(len(yans)):
            cost += abs(geuss[j] - yans[j])
            print(geuss[j], yans[j])
        print("cost?", cost)
        cost = cost ** 2
        totsum += cost
        print("cost:", cost)
        
    # end of individual net 10 tests
    print(prev-next)
    costs.append(totsum / 10)
# end of cycle through nets
next += 10
prev += 10

flab = 0
slab = 0
first = None
secon = None
min1 = 82
min2 = 82
for i in range(len(costs) - 1):
    if costs[i] <= min1:
        secon = first
        first = nets[i]
        slab = flab
        flab = i
print("Net:", flab, "came first  with cost:", costs[flab])
print("Net:", slab, "came second with cost:", costs[slab])
# end of game, top contestents move onto next game
for i in costs:
    print(i)