'''As cauchy distribution does not have a finite variance, it does not follow the central limit theorem 
this program takes the mean of the samples drawn from a cauchy distribution with 1, 5 and 10 at a time. 
we can clearly see from the graph that the results does not look like a gaussian, hence it does not follow 
central limit theorem'''


import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt

# samples from cho square distribution
np.random.seed(5)
Samples_Drawn = [1,5,10]
fig = plt.figure(figsize=(5,len(Samples_Drawn)*2))
plt.ion()

x = np.random.standard_cauchy((max(Samples_Drawn),10000))

for i in range(len(Samples_Drawn)):
    fig.add_subplot(len(Samples_Drawn),1,i+1)
    plt.subplots_adjust(hspace=1)
    sample_mean = x[:Samples_Drawn[i], :].mean(0)
    plt.hist(sample_mean,bins=50,normed=True)

    plt.title("$Samples = %i$" % Samples_Drawn[i])#, ha='right', va='top')
    plt.xlabel('x')
    plt.ylabel('p(x)')

plt.show()