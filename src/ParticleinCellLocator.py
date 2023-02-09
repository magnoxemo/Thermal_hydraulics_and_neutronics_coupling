center=[( 0 , 0 ),( 4 , 0 ),( 8 , 0 ),( -4 , 0 ),( -8 , 0 ),( 4, 4),( 4 , 8 ),( 8 , 4 ),( -4, 4),
( -4 , 8 ),( -8 , 4 ),( -8 , -4 ),( -4, 4),( -4 , -8 ),( -8 , -4 ),( 0, 4),( 0 , 8 ),( 0, -4),( 0 , -8 ),
( 4, -4),( 4 , -8 ),( -4, -4),( 8, -4)
]

x_centers=np.zeros(len(center))
y_centers=np.zeros(len(center))

for k in range(len(center)):
    x_centers[k],y_centers[k]=center[k]

    
def ParticleinCellLocator(x,y):

    for i in range(len(x_centers)):
        flag=0
        if np.sqrt((x-x_centers[i])**2+(y-y_centers[i])**2 )<=1:
            print("fuel_id --",i+1)
            flag=1
            return i
            break
    if flag==0:
        print("neutron is in moderator ")
h=ParticleinCellLocator(2,10)
