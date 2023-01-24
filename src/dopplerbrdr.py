import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('U-235 fission.csv')
energy=np.array(data['incident energy'])
cross_section=np.array(data['cross section'])

def RelE(val):
    return abs(val-0.5*k*Temp2)

m=1
M=235

k=8.617*10**-5
Temp2=500
alpha=(M/m)/(k*Temp2)

y=alpha*energy
Er=RelE(energy)
"""------------------------------interpolation------------------------------------"""

Ak=np.zeros(len(x)-1)
Bk=np.zeros(len(x)-1)

for i in range(len(energy)-1):
    Ak[i]=(energy[i+1]*cross_section[i]-energy[i]*cross_section[i+1])/(energy[i+1]-energy[i])
    Bk[i]=(cross_section[i+1]-cross_section[i])/(energy[i+1]-energy[i])
    
"""-----------------------------integration part-----------------------------------"""
"""there will be two loops.one to count the integral and one to count the data points"""

brdr_sigma=np.zeros(len(energy)-1)
for i in range(len(y)-1):
    intergral=0
    for j in range(len(energy)-1):
        delEr=abs(Er[j+1]-Er[j])
        intergral=intergral+np.sqrt(Er[j])*(Ak[j]+Bk[j]*Er[j])*delEr*(np.exp(-alpha*(energy[i]-Er[j])**2)-np.exp(-alpha*(energy[i]+Er[j])**2))
    brdr_sigma[i]=0.5*np.sqrt(alpha/(np.pi*energy[i]))*intergral
    
    
#---------------------------data visualization--------------------------
plt.figure(figsize=(10,6))
plt.plot(energy,cross_section,color='red')
plt.plot(energy[:len(energy)-1],brdr_sigma,color='green')
plt.xscale('log')
plt.yscale('log')
plt.legend(["Temperature--0k",'Temperature--500'])
plt.show()    
