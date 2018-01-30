import numpy as np
from scipy.stats import norm,moment,kurtosis,skew
from matplotlib import pyplot as plt
plt.ion()
#define mean and signma of the normal distribution
mean,sigma=1.5,0.5

p = np.linspace(norm.ppf(10e-7,mean,sigma),norm.ppf((10e5-1)*10e-7,mean,sigma), 1000)
new_norm = norm(mean,sigma)
plt.plot(p, new_norm.pdf(p), 'r-', lw=2, label='normal(1.5,0.5)')
plt.title('probability distribution function')
moments_normal=new_norm.stats(moments='mvsk')
plt.legend()


r=new_norm.rvs(size=1000)
plt.hist(r, normed=True)	
r_mean,r_var,r_skew,r_kur= r.mean(),r.var(),skew(r),kurtosis(r)
print('mean=',r_mean,'  variance=',r_var,'  skewness=',r_skew,'  kurtosis=',r_kur)

