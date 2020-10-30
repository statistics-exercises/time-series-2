import matplotlib.pyplot as plt
import numpy as np

def exponential(lam):
  # Write your function to generate an exponential random variable here

lamd = 2.0 
expectation =     ## Set the true value of the expectation here
indices, average = 200*[0], 200*[0] 
for i in range(200) :
  # Add code to calculate the average from n exponential random variables here and to thus 
  # set the elements of the list called average.  Also write code to set the elements 
  # of the list called indices. 

# This will plot the graph for the data
plt.plot( indices, average, 'b.' )
plt.xlabel("Number of random variables")
plt.ylabel("Sample mean")
plt.plot( [0,200], [expectation,expectation], 'r-')
plt.savefig("average_exponential.png")
