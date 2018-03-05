import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt

plt.ion()
data=np.loadtxt('data.txt')
density=np.asarray(data[:,0])
w,p=stats.shapiro(density)
wL,pL=stats.shapiro(np.log(density))
plt.subplot(2,1,1)

x = np.linspace(min(density)-2,max(density)+1,100)
mu,sigma=stats.norm.fit(density)
new_norm = stats.norm(mu,sigma)
plt.hist(density,normed=1,label='Density Hist')
plt.plot(x,new_norm.pdf(x),label='Best Normal Fit')
plt.title('Shapiro-Wilk for Gaussianity')
plt.text(-1,0.6,'p value=%f'%(p))
plt.text(-1,0.5,'w value=%f'%(w))
plt.ylabel('Asteroid Density')
plt.legend()


plt.subplot(2,1,2)
muL,sigmaL=stats.norm.fit(np.log(density))
new_normL = stats.norm(muL,sigmaL)
y = np.linspace(min(np.log(density)-1),max(np.log(density)+1),100)
plt.hist(np.log(density),normed=1,label='Log(Density) Hist')
plt.plot(y,new_normL.pdf(y),label='Best Normal fit')
plt.text(-1,1.5,'p value=%f'%(pL))
plt.text(-1,1.3,'w value=%f'%(wL))
plt.ylabel('Log(Density)')
plt.legend()

print('For Density the W value is %f'%(w))
print('For Log of Density the W value is %f'%(wL))
print('As W for log data is more close to 1,the log of the Data is more Guassian')