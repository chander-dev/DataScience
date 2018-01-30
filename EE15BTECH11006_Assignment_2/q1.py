
import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt

# samples from cho square distribution
np.random.seed(5)
Samples_Drawn = [1,5,10]
fig = plt.figure(figsize=(5,len(Samples_Drawn)*2))
plt.ion()
DOF=3

x = np.random.chisquare(DOF,(max(Samples_Drawn), 10000))
for i in range(len(Samples_Drawn)):
    fig.add_subplot(len(Samples_Drawn),1,i+1)
    plt.subplots_adjust(hspace=1)
    sample_mean = x[:Samples_Drawn[i], :].mean(0)
    plt.hist(sample_mean,bins=50,normed=True)

# plot the expected gaussian pdf
    sigma = np.sqrt(2.0*DOF/Samples_Drawn[i])
    dist = norm(DOF, sigma)
    x_pdf = np.linspace(norm.ppf(10e-7,DOF,sigma),norm.ppf((10e5-1)*10e-7,DOF,sigma), 1000)
    plt.plot(x_pdf, dist.pdf(x_pdf), '--r')

    plt.title("$Samples = %i$" % Samples_Drawn[i])#, ha='right', va='top')
    plt.xlabel('x')
    plt.ylabel('p(x)')

plt.show()