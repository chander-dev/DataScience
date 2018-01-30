import numpy as np
from scipy.stats import norm,cauchy
from matplotlib import pyplot as plt
plt.ion()

mean,sigma=1.5,0.5

new_norm = norm(mean,sigma)
new_cauchy=cauchy(mean,sigma)

p = np.linspace(norm.ppf(10e-7,mean,sigma),norm.ppf((10e5-1)*10e-7,mean,sigma), 1000)
plt.title('mean=1.5, standard deviation =0.5 for both')
plt.plot(p, new_norm.pdf(p), 'k-', lw=2, label='normal')
plt.plot(p, new_cauchy.pdf(p), 'r-', lw=2, label='cauchy')
plt.legend()