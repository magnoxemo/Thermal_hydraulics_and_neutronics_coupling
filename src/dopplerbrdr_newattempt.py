import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import time 

data=pd.read_csv('/home/shochcho/Downloads/Doppler code/U-235 fission.csv')
energy=np.array(data['incident energy'])
cross_section=np.array(data['cross section'])

def RelE(val):
    return abs(val-0.5*k*Temp2)

m=1
M=235

k=8.617*10**-5
Temp2=5000
alpha=(M/m)/(k*Temp2)


from scipy.interpolate import interp1d

sigma_a=interp1d(energy,cross_section)

def ResonaceSplit(energy,cross_section):
    LowRE=10**-.8
    HighRE=10**5
    for i in range(len(energy)):
        if energy[i]>LowRE:
            break
    for j in range(i,len(energy)):
        if energy[j]>HighRE:
            break
    
    ResonaceEnergy=energy[i:j]
    Resonacecross=cross_section[i:j]

    return ResonaceEnergy,Resonacecross
ResonaceE,ResonaceSigma=ResonaceSplit(energy,cross_section)

loopCount=len(ResonaceE)-1
brdr_sigma=np.zeros(loopCount)
start_time=time.time()

for i in tqdm(range(loopCount)):
	
    integral=0

    for j in range(loopCount):
		
        delEr=abs(ResE_R[j+1]-ResE_R[j])/10
        innerintgrl=0
	
        for k in range(10):
		
            step_Er = ResE_R[j]+k*delEr
            innerintgrl=innerintgrl+(sigma_a(step_Er))*delEr   

        integral=integral+np.sqrt(ResE_R[j])*innerintgrl*(np.exp(-alpha*(energy[i]-ResE_R[j])**2)-np.exp(-alpha*(energy[i]+ResE_R[j])**2))
    brdr_sigma[i]=0.5*np.sqrt(alpha/(np.pi*ResonaceE[i]**2))*integral
   

end_time=time.time()
elapsed_time =end_time-start_time
print('Execution time:', elapsed_time, 'seconds')

plt.figure(10,6)
plt.plot(ResonaceE,ResonaceSigma,color='pink')
plt.plot(ResonaceE[:(loopCount)],brdr_sigma,color="green")
plt.xscale('log')
plt.yscale('log')
plt.show()
