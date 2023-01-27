import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


#----------------------importing data file & constant defining ----------------------
data=pd.read_csv('U-235 fission.csv')
energy=np.array(data['incident energy'])
cross_section=np.array(data['cross section'])

def RelE(val):
    return abs(val-0.5*k*Temp2)

m=1                     #projectile mass
M=235                   #target mass

k=8.617*10**-5          #boltzman const
Temp2=500               #target temp
alpha=(M/m)/(k*Temp2)   

y=alpha*energy
Er=RelE(energy)         #relative energy calculation


"""------------------------------interpolation------------------------------------"""

Ak=np.zeros(len(x)-1)       #constant term in linear interpolation 
Bk=np.zeros(len(x)-1)       #term which is propotional to E



# calculation loop for interpolation 
for i in range(len(energy)-1):
    Ak[i]=(energy[i+1]*cross_section[i]-energy[i]*cross_section[i+1])/(energy[i+1]-energy[i])
    Bk[i]=(cross_section[i+1]-cross_section[i])/(energy[i+1]-energy[i])


    
"""-----------------------------integration part-----------------------------------"""
"""there will be three loops.one to count the integral and one to count the data points another one to carry out the inner inetgral"""





"""this function will take E parameter and return the coressponding index value of the 
linear intepolator's coefficient 
				
				Ak[i]----> the constant term
				Bk[i]----> the relative term 
first there will be a linear search in the energy[] list then return the index of that range in energy  """

def indexFinder(E):

	flag=0
	for k in range(len(energy)-1):
		if energy[k]<E and energy[k+1]>E:
			flag=1
			return k
			break
	if flag==0:
		return k
			 
			 
brdr_sigma=np.zeros(len(energy)-1)
for i in range(len(y)-1):

    intergral=0
    
    for j in range(len(energy)-1):
    
        delEr=abs(Er[j+1]-Er[j])/1000
        innerintgrl=0
        
        #inner inet
        for j in range(1000):
        
        	step_Er=Er[j]+k*delEr
        	m=indexFinder(step_Er)
        	innerintgrl=innerintgrl+(Ak[m]+B[m]*step_Er)*delEr
        
        #interpolation's problem fixation--- done        
        intergral=intergral+np.sqrt(Er[j])*innerintgrl*(np.exp(-alpha*(energy[i]-Er[j])**2)-np.exp(-alpha*(energy[i]+Er[j])**2))
        
    brdr_sigma[i]=0.5*np.sqrt(alpha/(np.pi*energy[i]))*intergral
    
    
    
#---------------------------data visualization--------------------------
plt.figure(figsize=(10,6))
plt.plot(energy,cross_section,color='red')
plt.plot(energy[:len(energy)-1],brdr_sigma,color='green')
plt.xscale('log')
plt.yscale('log')
plt.legend(["Temperature--0k",'Temperature--500'])
plt.show()    


"""this code is based on the sigma1 karnel algorithm 
ref paper https://www.tandfonline.com/doi/abs/10.13182/NSE76-1 """
