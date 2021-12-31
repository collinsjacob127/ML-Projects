# Neural Network class definition
# Jacob Collins
# 31 December 2021
import numpy as np

# Class def
class Network:
    # Class initializer
    # Initializes the weights
    # @param array structure - number of nodes for each layer (0 - input, max - output)
    def __init__(self, structure):
        # Process structure and initialize weights
        # self.weights - list of each weight matrix in sequential order.
        self.weights = list()
        for i in range(len(structure)-1):
            self.weights.append(0.02*np.random.random((structure[i],structure[i+1]))-0.01)



    # Forward propagation
    # Runs input through the network and gives output
    def forward_prop(self, input):
        # Connect input to first hidden layer and output
        pass
    # Backpropagation
    # Compares output to correct response and adjusts weights accordingly
    def back_prop(self, output, correct):
        # Check alignment of output and correct
        pass

    # Iterative Learning
    # Automatically runs through batches and trains the network;
    # Saves output to text file
    # @param iterations - number of iterations to run through
    # @param inputs - list of inputs for running through
    # @param corrects - list of correct responses for comparison
    def iterative_learning(self, iterations, inputs, corrects):
        pass

net = Network([5, 4, 3, 2])

