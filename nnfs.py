import sys
import numpy as np
# import matplotlib

# current version  
print("Python : ", sys.version)
print("Numpy  : ", np.__version__)
# print("Matplotlib : ", matplotlib.__version__)

# Single Neuron
inputs = [1, 2, 3, 2.5] # considering last layer with single output connected
weights = [0.2, 0.8, 0.5, 1.0] 
bias = 2

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output)

# 3 Layered Neuron
inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, 0.5, 1.0]
weights2 = [0.5, 0.91, 0.26, 0.5] 
weights3 = [0.26, 0.27, 0.17, 0.87] 

# Input : Weight's Matrix
for i in inputs:
  for j in weights1:
    print(f'{i}*{j}')

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [
         inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + bias1,
         inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + bias2,
         inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + bias3   
        ] 
print(output)

# now let's make it little more dynamic 
weights = [
            [0.2, 0.8, 0.5, 1.0],
            [0.5, 0.91, 0.26, 0.5],
            [0.26, 0.27, 0.17, 0.87]
          ]
        
biases = [2, 3, 0.5]

op = []
for i, w in zip(input, weights):
  op.append(i * w)
