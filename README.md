# Sample mean for exponential random variable

Lets use the fact that you now know how to generate exponential random variables to revise some of the material that was covered in week 4.  In particular I would like you to examine how quickly a sample mean computed from a series of identical exponential random variables converges on the value of the true expectation.  With this in mind I would like you to first.

1. Write a function called `exponential` that takes a parameter called `lam` and that returns an exponential random variable sampled from a distribution with parameter `lam`.
2. Set the value of the variable called `expectation` equal to the true value of the expectation for the random variable that has been sampled in step 3.
3. Call the function called `exponential` using the variable called `lamd` 200 times and compute sample means from 1 sample of the random variable, 2 samples of the random variable, 3 samples of the random variable and so on up until you compute a sample mean from 200 samples of random variable.   You should store the sample means from these samples of different sizes that you calculate in the list called `average`.
4. Set the 200 elements of the array called `indices` to the integers from 1 up to 200.

If you complete the four tasks above the code in the cell on the left should output a graph showing how the sample mean changes as you change the number of random variables from which is computed. 
