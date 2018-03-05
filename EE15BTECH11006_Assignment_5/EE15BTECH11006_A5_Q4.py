import numpy as np 
from matplotlib import pyplot as plt
from scipy.stats import norm
from sklearn.mixture import GMM
plt.ion()


data=np.log10(np.loadtxt('t90.txt'))
X=data.reshape(-1,1)

N = np.arange(1, 20) #componets in GMM
models=[(GMM(n_components=i, n_iter=1000,covariance_type='full')).fit(X) for i in N]
AIC = [m.aic(X) for m in models]
BIC = [m.bic(X) for m in models]

best = np.argmin(BIC)
Gmm_best = models[best]

print "Best fit converged:", Gmm_best.converged_
print "BIC: n_components =  %i" % N[best]

# plot AIC/BIC
plt.plot(N, AIC, '-k', label='AIC')
plt.plot(N, BIC, '-r', label='BIC')
plt.title("Best n_components=%d"%(N[best]))
plt.xlabel('N components')
plt.ylabel('AIC/BIC')
plt.legend()
plt.show()