import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt 
from numpy import sqrt


data = pd.read_csv("/home/walid_ahammed/Downloads/U-235 fission.csv")

energy = np.array(data['Incident energy'])
cross_section = np.array(data['cross section'])

k = 0.8617*10**-4
mass_projectile = 1
mass_target = 235
temp_1 = 0
temp_2 = 298
alpha = (mass_target/mass_projectile)/(k*(temp_2-temp_1))

sigma = interp1d(energy, cross_section)


def GetIntegral_Value(E, E_rmax):
    energy = E
    interval = 1000
    E_realtive = np.arange(0, E_rmax, interval)
    dE_r = E_rmax/interval

    sum = 0

    for i in E_realtive:
        try:
            sum = sum+sqrt(i)*sigma(i)*(np.exp(-alpha*(sqrt(energy)-sqrt(i))
                                                    ** 2)-np.exp(-alpha*(np.exp(energy)+np.exp(i))**2))*dE_r
        except:
            pass

    return sum


def getMaxEnegybasedInputEnergy(E, mass_projectile, mass_target, temp_2, k):
    E_rMax = 0.5*mass_projectile * \
        (sqrt(2*E/mass_projectile)+sqrt(k*temp_2/mass_target))**2
    return E_rMax

x=[]
def FinalCal():
    sigmaPrime = []
    j=0
    for i in range(len(energy)):
        if energy[i]>10**-2 and energy[j]<10**6:
            x.append(energy[i])
            sigmaPrime.append((1/sqrt(energy[i]))* 0.5*sqrt(alpha/np.pi*energy[i])*GetIntegral_Value(
                energy[i], getMaxEnegybasedInputEnergy(energy[i], mass_projectile, mass_target, temp_2, k)))
            j=j+1

    return sigmaPrime
sigmaPrime=FinalCal()

plt.figure(figsize=(10,6))
plt.plot(energy,cross_section)
plt.plot(x,sigmaPrime)
plt.xscale('log')
plt.yscale('log')