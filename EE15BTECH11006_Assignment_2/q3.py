import numpy as np
from scipy.stats import dweibull
from matplotlib import pyplot as plt
plt.ion()

Weibull = dweibull(2, 0, 6) #k=2, lamda=6
x_axis = np.asarray([i+0.5 for i in range(20)])
y_axis = np.asarray([2.75, 7.80, 11.64, 13.79, 14.20, 13.15, 11.14, 8.72, 6.34, 4.30, 2.73, 1.62, 
	0.91,0.48, 0.24, 0.11, 0.05, 0.02, 0.01, 0.00])*100

y,c=[],0
for i in range(len(y_axis)):
    y = np.concatenate((y,np.linspace(c,c+1,y_axis[i])),axis = 0)
    c+=1
plt.hist(y,bins= 30, normed=True,label='Histogram')

x = np.linspace(0, 20, 10e3)
plt.plot(x, Weibull.pdf(x)*2,'--r',label='k=2,$ \lambda=6$')
plt.xlabel('x')
plt.ylabel('p(x|k,$\lambda)$')
plt.title('Weibull Distribution')
plt.show()