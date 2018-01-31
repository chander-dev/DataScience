'''we know that CDF of any valid distribution will range from 0 to 1. Take samples from uniform 
distribution from 0 to 1 and take the inverse cdf(cdf of the required distributiom).'''

import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt
sample=int(1e5) #number of samples to be taken from that distribution
dist=norm     #change the distribution here 

plt.ion()
def get_random_sample(dist,n=1):
	r=np.random.rand(n)
	return dist.ppf(r)
a=get_random_sample(dist,sample)
plt.hist(a,bins=50,normed=True,label='Sampled points')
x_pdf = np.linspace(norm.ppf(10e-5,0,1),norm.ppf((10e2-1)*10e-4,0,1), 1000)
plt.plot(x_pdf, dist.pdf(x_pdf), '--r',label='Actual Guassian')
plt.legend()
plt.show()