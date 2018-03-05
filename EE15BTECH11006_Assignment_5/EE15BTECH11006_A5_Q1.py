import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from astroML.stats import mean_sigma, median_sigmaG
plt.ion()
A2_list,D_list,W_list=[],[],[]

for i in range(100):
    normal_vals = stats.norm(loc=0, scale=1).rvs(10000)
 
    A2_list.append(stats.anderson(normal_vals)[0])
    D_list.append(stats.anderson(normal_vals)[0])
    W_list.append(stats.shapiro(normal_vals)[0])

# plot a histogram
fig, ax = plt.subplots(3,1,figsize=(12, 8))
fig.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,wspace=0.2, hspace=0.5)
ax[0].hist(A2_list)
ax[0].set_ylabel('Anderson-Darling(A2)')

ax[1].hist(D_list)
ax[1].set_ylabel('Kolmogorov-Smirnov(D)')

ax[2].hist(W_list)
ax[2].set_ylabel('Shapiro-Wilks(W)')