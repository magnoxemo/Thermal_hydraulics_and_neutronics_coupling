import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import scipy as sp
from scipy.interpolate import interp1d
from scipy.intergrate import trapz

class material:
	
	def __init__(self,Atomic_mass,density,enrichment,temp,ReactionType):
	
		M=Atomic_mass										#atomic mass of the element 
		density=density									#atomic density
		NA=6.023*10**23									#avogrado constant 
		enrichment=enrichment									#enrichment 
		temp=temp										#temp needs to perform doppler boardening 
		ReactionType=ReactionType								#types of the reaction will happen
		energy,sigma={}							                #cross section dictionary  
		
		
	def CrossSectionLoad(self):
	
		Type_Reaction=len(self.ReactionType)
		path=[]										#path to the cross section file 
		xsection=[]										#cross section data load
		energy={}										#reaction type wise energy 
		sigma={}										#reaction type wise cross section 
		
		for i in range(Type_Reaction):
			
			path.append(1)
			xsection.append(2)
			
		try:	
			for i in range(Type_Reaction):

				path[i]=str(cross section data /)+str(self.M)+str(self.ReactionType[i])+str(.csv)
				xscetion[i]=pd.readcsv(path)
				engergy[str(self.ReactionType[i])]=xsection[i]["Incident energy"]
				sigma[str(self.ReactionType[i])]=xsection[i]["Cross section"]
				
			return energy,sigma
		except:
			raise data_not_found_in_the_bank_Error(str(self.ReactionType[i])," not found ")
	def Dopplerdrbr(self):
	    	energy1=np.array(self.)
	    	cross_section=np.array()

	    	m=1                      							      #projectile mass-----gram atom 
	    	M=self.M                     							      #target mass    -----gram atom
	    	k=8.617*10**-5            							      #boltzman const -----eV 
	    	Temp2=self.temp                   						      #target temp---------Kelvin scale 
	    	Temp1=0
	    	alpha=(M/m)/(k*(Temp2-Temp1))   

	    	"""------------------------------interpolation------------------------------------"""

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
		
			ResonaceEnergy=energy1[i:j]
			Resonacecross=cross_section[i:j]

			return ResonaceEnergy,Resonacecross,i,j

	    	energy,ResonaceSigma,st,ed=ResonaceSplit(energy1,cross_section)
	    	

	    #-------------integration calculation --------------------
	    	E_r=np.zeros(len(energy1))
	   	E_min=np.min(energy)
	    	E_max=np.max(energy)
	    	step=10**6

	    	Er=np.linspace(E_min,E_max,step)
	    	dx=(E_max-E_min)/step

	    #----------------F(x) calculation in the integration loop--------------
	    
	    	def CalFx(x):

			E_r=np.sqrt(Er)*sigma_a(Er)*(np.exp(-alpha*(np.sqrt(x)-np.sqrt(Er))**2)-np.exp(-alpha*(np.sqrt(x)+np.sqrt(Er))**2))

			return E_r
	    	sigma=np.zeros(len(cross_section))

	    	for i in tqdm(range(len(energy))):
			sigma[i]=1/energy[i]*0.5*np.sqrt(alpha/(np.pi))*np.trapz(CalFx(energy[i]),x=Er,dx=dx)
		
		cross_section[st:ed-1]=sigma[:len(energy)-1]
		
		return energy1,cross_section
		
		
	def MacroScopicCross(self):
	
		molar_mass=self.M
		density=self.desnity
		atom_density=(N/molar_mass)*density*10**-24
		enrichment=self.enrichment
		 
		for i in range(Type_Reaction):

			engergy[str(self.ReactionType[i])]=atom_density*enerichment*engergy[str(self.ReactionType[i])]
			sigma[str(self.ReactionType[i])]=atom_density*enerichment*sigma[str(self.ReactionType[i])]
				
		return energy,sigma
	
	def mix(self,material[]):
	
		Items=len(material)
		
		for i in range(Items):
			for k in range()
			material[i]
			
