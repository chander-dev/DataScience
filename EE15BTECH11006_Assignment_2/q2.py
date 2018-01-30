import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import spearmanr,kendalltau,pearsonr	
plt.ion()
DataFileIn = open("data.dat", "r")
DataList = DataFileIn.readlines()
DataFileIn.close()
luminosity,red_shift=[],[]
for i in DataList:
    luminosity.append(float(i.split(' ')[0]))
    red_shift.append(float((i.split()[1]).split('\n')[0]))

plt.loglog(red_shift,luminosity,'or',)
plt.title('loglog plot for luminosity vs red shift')
plt.ylabel('luminosity')
plt.xlabel('red_shift')
plt.show()
pearson_rho,pearson_pValue=pearsonr(luminosity,red_shift)
spearman_rho,spearman_pValue=spearmanr(luminosity,red_shift)
kendalltau_rho,kendalltau_pValue=kendalltau(luminosity,red_shift)
print('Spearman---| correlation=',spearman_rho,'p value=',spearman_pValue)
print('Pearson---| correlation=',pearson_rho,'p value=',pearson_pValue)
print('Kendall-tau---|  correlation=',kendalltau_rho,'p value=',kendalltau_pValue)