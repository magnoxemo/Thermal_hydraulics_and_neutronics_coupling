import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import time 


#----------------------importing data file & constant defining ----------------------

data=pd.read_csv('/home/shochcho/Downloads/Cm-246 absorption.csv')
energy1=np.array(data['incident energy'])
cross_section=np.array(data['cross_section'])

m=1                       #projectile mass
M=246                     #target mass

k=8.617*10**-5            #boltzman const
Temp2=50000               #target temp
alpha=(M/m)/(k*Temp2)   

"""------------------------------interpolation------------------------------------"""

from scipy.interpolate import interp1d

sigma_a=interp1d(energy1,cross_section)

#-----------resonance regionsplit----------

def ResonaceSplit(energy,cross_section):
    LowRE=10**-1
    HighRE=10**4
    for i in (range(len(energy))):
        if energy[i]>LowRE:
            break
    for j in range(i,len(energy)):
        if energy[j]>HighRE:
            break
    
    ResonaceEnergy=energy[i:j]
    Resonacecross=cross_section[i:j]
    print(i,j)

    return ResonaceEnergy,Resonacecross
energy,ResonaceSigma=ResonaceSplit(energy1,cross_section)

#-------------integration calculation --------------------
E_r=np.zeros(len(energy1))
E_min=np.min(energy)
E_max=np.max(energy)
step=10**5

Er=np.linspace(E_min,E_max,step)
dx=(E_max-E_min)/step

#----------------F(x) calculation in the integration loop--------------
def CalFx(x):

    E_r=np.sqrt(Er)*sigma_a(Er)*(np.exp(-alpha*(np.sqrt(x)-np.sqrt(Er))**2)-np.exp(-alpha*(np.sqrt(x)+np.sqrt(Er))**2))

    return E_r
sigma=np.zeros(len(cross_section))

for i in tqdm(range(len(energy))):
    sigma[i]=1/energy[i]*0.5*np.sqrt(alpha/(np.pi))*np.trapz(CalFx(energy[i]),x=Er,dx=dx)
   

#---------------------------data visualization--------------------------
plt.figure(figsize=(10,6))
plt.scatter(energy,ResonaceSigma,color='red')
plt.plot(energy,sigma[:len(energy)],color='green')
plt.xscale('log')
plt.yscale('log')
plt.legend(["--0","--50000 K"])
plt.show()


"""this code is based on the sigma1 karnel algorithm 
ref paper https://www.tandfonline.com/doi/abs/10.13182/NSE76-1 """
