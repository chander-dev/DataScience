import scipy
significance_Higgs =scipy.stats.norm.isf(1.7e-9)
print('significance in terms of no of sigmas HIGGS ',significance_Higgs)
#which is matching with the value given in tha paper

significance_Ligo =scipy.stats.norm.isf(2e-7)
print('significance in terms of no of sigmas LIGO',significance_Ligo)

#goodness of fir according to the best parameters taken from mentioned paper
p_value=1-scipy.stats.chi2(67).cdf(65.2)
print('GOF using the best-fit',p_value)
