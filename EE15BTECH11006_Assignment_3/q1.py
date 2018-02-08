from astroML.resample import bootstrap
import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt
plt.ion()
N=1000

samples = np.random.normal(0,1,N)
median_BS = bootstrap(samples,10000,np.median,kwargs=dict(axis=1))
standard_dev=np.std(median_BS)
std=np.sqrt(np.pi/(2*N))
print('deviation of bootstrap sammples',standard_dev)

x = np.linspace(-0.5,0.5,1000)
mu = np.mean(median_BS)
sigma = np.std(median_BS)
pdf = norm(0, std).pdf(x)#theorically expected gaussian 
pdf1 = norm(mu, sigma).pdf(x) #samples based gaussian 
plt.hist(median_BS,bins=30,normed=True,label='Histogram') #histogram of Bootstrap samples
plt.plot(x,pdf,'-k',label='sample calculated plot')	
plt.plot(x,pdf1,'-r',label='Theoritical Plot')
plt.legend()