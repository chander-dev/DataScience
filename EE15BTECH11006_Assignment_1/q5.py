path='exoplanet.eu_catalog.csv'
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import *
import pandas as pd 

df = pd.read_csv(path) #reading the datafile 
e=df['eccentricity'] 
e=e.dropna() #removing all NaN
a=np.array([i for i in e if i!=0]) #0 input is not valid in the boxcox function so drop it
ans,k=boxcox(a)

#plotting the results
fig=plt.figure()
ax1=fig.add_subplot(211)
ax2=fig.add_subplot(212)
ax1.set_title('Eccentricity data')
ax2.set_title('BoxCox Gaussianizing')
ax1.hist(a,normed=True)
ax2.hist(ans,normed=True,bins=15)
plt.tight_layout()
plt.show()	
