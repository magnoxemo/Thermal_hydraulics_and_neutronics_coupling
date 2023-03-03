import numpy as np

def ParticleLocFind(pos):
	
	x=pos[0]
	y=pos[1]
	z=pos[2]
	if np.sqrt(x**2+y**2+z**2)>geometry.diam:
			return 0
	elif:
		for i in geometry.object:
	
		if Val(x,y,z,i.param)<=0:
			return i.id
		else:
			return i.Moderator_id
			
def ParticleMover(R0,Omega0):

""" as Omega0 will be a veactor in 3D it's better to treat it as an array of size 3

  				r[0]=x i
  				r[1]=y j 
  				r[2]=z k 
  				
    and here x=u ,y=v, z= w so omega0= u i+ v j + w k and the new updated distance will be 
    
    				r=r0+r'*omega'
    				r=-ln(meu)/total_sigma
    				
 """	
 	ID=ParticleLocFind(R0)
 	Sigma_T=material.GetTotalCross(ID)
 	
 	l=-np.ln(np.random.rand())/sigma_T
 	u=Omega0[0]
 	v=Omega0[1]
 	w=Omega0[2]
 	
	meu=np.random.rand()
	omega_=np.zeros(3)
	
	omega_[0]=(-(u*w*np.cos(phi0)/s)-v/s)*np.sqrt(1-meu**2)
	omega_[1]=(-(v*w*cos(phi0)+u/s)*np.sqrt(1-meu**2)+v*meu)
	omega_[2]=(s*(np.sqrt(1-meu**2)*np.cos(phi0)+w*meu))
	
	r=r0+l*omega_
	
	return r
