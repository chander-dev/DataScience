import numpy as np
from matplotlib import pyplot as plt
plt.ion()

f=open('q2.txt','r')
lines=f.readlines()
x,y,sigma_y=[],[],[]
for i in lines:
    x.append(i.split(' ')[1])
    y.append(i.split(' ')[2])
    sigma_y.append(i.split(' ')[3])
f.close()

x,y,sigma_y=np.asarray(x,dtype='float32'),np.asarray(y,dtype='float32'),np.asarray(sigma_y,dtype='float32')

#creating matrices
A=np.column_stack((np.ones(x.shape[0]),x))
A=np.asarray(A,dtype='float32')
C=np.diag(sigma_y)**2	
Y=y

#x=([A(T).C(-1).A](-1))[A(T).C(-1).Y]
b,m = np.matmul(np.linalg.inv(np.matmul(np.matmul(A.T,np.linalg.inv(C)),A)),np.matmul(np.matmul(A.T,np.linalg.inv(C)),Y))
print('slope=',m,'intercept=',b)

y_pred = m*x+b
plt.xlabel('x')
plt.ylabel('y')
plt.title('Estimated Line')
plt.errorbar(x,y,yerr=sigma_y,fmt='o',label='error')
plt.plot(x,y_pred,'-k',label='Best fit')
plt.legend()
