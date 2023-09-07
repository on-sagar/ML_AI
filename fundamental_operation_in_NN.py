
'''DEMONSTRATING THE FUNDAMENTAL CONCEPT OF A NEURAL NETWORK'''

##A neural netwroks takes a certain input then multiplies those
##inputs by certains weights,sums up a bias and produces an output.
##This output maybe the final or within one of many hidden layers
##so, the fundamental operation going on within a neural network is just
##the following calculation

inputs=[1.9,3.5,4.9]
weights=[3,4,5]
bias=0.8

output=inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[1]
print(output)