import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import scipy
import scipy.stats
plt.ion()

data=np.loadtxt('data.txt')
x,y,sigma_y=np.asarray(data[:,0],dtype='float32'),np.asarray(data[:,1],dtype='float32'),np.asarray(data[:,2],dtype='float32')

def linear(x, m, i):
 	return m*x +i 
def quad(x,a,b,c):
	return a*x**2 + b*x + c
def cube(x,a,b,c,d):
	return a*x**3 + b*x**2 + c*x+d


xp=np.linspace(0,1,100)
m,i=curve_fit(linear,x,y,sigma= sigma_y)[0]

plt.plot(x,y,'o',label='data')
plt.plot(xp,linear(xp,m,i),'--b',label='m=%5.3f b= %5.3f'%( m,i))

a,b,c=curve_fit(quad,x,y,sigma= sigma_y)[0]
plt.plot(xp,quad(xp,a,b,c),'--k',label='a=%5.3f b=%5.3f c=%5.3f'%(a,b,c))

p,q,r,s=curve_fit(cube,x,y,sigma= sigma_y)[0]
plt.plot(xp,cube(xp,p,q,r,s),'--r',label='p=%5.3f q=%5.3f r=%5.3f s=%5.3f'%(p,q,r,s))

plt.title('Curve Fitting')
plt.xlabel('X')
plt.ylabel("Y")
plt.legend()


# linear model:
y_linear = linear(x,m,i)
y_quad = quad(x,a,b,c)
y_cube = cube(x,p,q,r,s)

'''
resid_linear = y - y_linear
resid_quad = y - y_quad
resid_cube = y - y_cube

sse_linear = sum(resid_linear**2)
sse_quad = sum(resid_quad**2)
sse_cube = sum(resid_cube**2)
'''
# *******Chi2**********
Chi2_linear=np.sum(((y-y_linear)/sigma_y)**2)
Chi2_quad=np.sum(((y-y_quad)/sigma_y)**2)
Chi2_cube=np.sum(((y-y_cube)/sigma_y)**2)
# print('Linear Chi2=%f Quadratic Chi2=%f Cubic Chi2=%f'%(Chi2_linear,Chi2_quad,Chi2_cube))

Chi2_linear_likelihood= scipy.stats.chi2(len(x)-2).pdf(Chi2_linear)
Chi2_quad_likelihood= scipy.stats.chi2(len(x)-3).pdf(Chi2_quad)
Chi2_cube_likelihood= scipy.stats.chi2(len(x)-4).pdf(Chi2_cube)
print('Linear Chi2_likelihood=%f Quadratic Chi2_likelihood=%f Cubic Chi2_likelihood=%f'%(Chi2_linear_likelihood,Chi2_quad_likelihood,Chi2_cube_likelihood))

p_quad_linearH=1-scipy.stats.chi2.cdf(Chi2_linear-Chi2_quad,df=1)
p_cube_linearH=1-scipy.stats.chi2.cdf(Chi2_linear-Chi2_cube,df=2)
print('Linear as Hypothesis--->Quadratic P value=%f Cubic P value =%f'%(p_quad_linearH,p_cube_linearH))

# p_linear=1-scipy.stats.chi2.cdf(Chi2_linear,df=(len(x)-2))
# p_quad=1-scipy.stats.chi2.cdf(Chi2_quad,df=(len(x)-3))
# p_cube=1-scipy.stats.chi2.cdf(Chi2_cube,df=(len(x)-4))
# # print("********* P values ********")
# print('Linear p=%f Quadratic p=%f Cubic p=%f'%(p_linear,p_quad,p_cube))

lmax_linear= -np.sum(scipy.stats.norm.logpdf(y,loc=y_linear,scale=sigma_y))
lmax_quad= -np.sum(scipy.stats.norm.logpdf(y,loc=y_quad,scale=sigma_y))
lmax_cube= -np.sum(scipy.stats.norm.logpdf(y,loc=y_cube,scale=sigma_y))


AIC_linear= 2*2-2*lmax_linear
AIC_quad= 2*3-2*lmax_quad
AIC_cube= 2*4-2*lmax_cube

delta_AIC_Linear_Quad=AIC_quad - AIC_linear
delta_AIC_Linear_Cube= AIC_cube - AIC_linear
# print("********AIC********")
print('Linear AIC=%f Quadratic AIC=%f Cubic AIC=%f'%(AIC_linear,AIC_quad,AIC_cube))
print('AIC_quad - AIC minimum=',delta_AIC_Linear_Quad,'AIC_Cube- AIC minimum=',delta_AIC_Linear_Cube)

n=len(x)
BIC_linear=-2*lmax_linear + 2*np.log(n)
BIC_quad=-2*lmax_quad + 3*np.log(n)
BIC_cube=-2*lmax_cube + 4*np.log(n)

delta_BIC_Linear_Quad=BIC_quad - BIC_linear
delta_BIC_Linear_Cube= BIC_cube - BIC_linear
# print('*******BIC*********')
print('Linear BIC=%f Quadratic BIC=%f Cubic BIC=%f'%(BIC_linear,BIC_quad,BIC_cube))
print('BIC_quad - BIC minimum=',delta_BIC_Linear_Quad,'BIC_Cube- BIC minimum=',delta_BIC_Linear_Cube)


#taking linear to be NULL hypothoesis 



''' 
y_hat = model.predict(X)
resid = y - y_hat
sse = sum(resid**2)
k= # of variables
AIC= 2k - 2ln(sse)
k = number of variables
n = number of observations
BIC = -2*ln(sse) + k*ln(n)'''	