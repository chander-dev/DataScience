import numpy as np
from scipy import stats
import pandas as pd
df = pd.read_table("h.dat", sep="\s+")
ra=df['RA'].between(50,100)
de=df['DE'].between(0,25)
pmra=df['pmRA'].between(90,130)
pmde=df['pmDE'].between(-60,-10)
eplx=df['e_Plx'].between(0,5)
bv=df['B-V'].between(0,0.2)
hyades=df[ra & de & pmra & pmde & eplx & bv]

hyades_index=hyades.index.values
i=[i for i in df.index if i not in hyades_index]  
non_hyades=df.loc[i]

hyades=np.asarray(hyades)
non_hyades=np.asarray(non_hyades)
t,p = stats.ttest_ind(hyades[:,8],non_hyades[:,8],nan_policy='omit')
 # hece color of the hyades stars differ from the non- hyades
print('p value is=',p)



