# Calculate the weighted mean lifetime and uncertainty of the mean.
import numpy as np 
a=np.asarray([[0.8920,0.00044], [0.881,0.009], [0.8913,0.00032], [0.9837,0.00048], [0.8958,0.00045]]) 
x=a[:,0]
n=a[:,1]
num,denum=0,0
for i in range(len(a)):
	num+=x[i]/(n[i]**2)
	denum+=1/n[i]**2
weighted_mean=num/denum
error=1.0/denum
print('weighted mean=',weighted_mean)
print('error=',error)