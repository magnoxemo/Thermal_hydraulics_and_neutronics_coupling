import numpy as np 
import matplotlib.pyplot as plt 

def CoreVisualize(center,radius):

    figure, axes = plt.subplots()
    axes.set_facecolor('xkcd:green')
    axes.set_facecolor((.0, 0, .9))
    plt.xlim(-10,10)
    plt.ylim(-10,10)
  
    center=center
    radius=radius

    for i in center:
        axes.add_artist( plt.Circle(i,radius,color='red',fill=True ))
        axes.add_artist( plt.Circle(i,radius+0.1,color='green',fill=False ))
        axes.add_artist( plt.Circle(i,radius+0.2,color='black',fill=False ))

    plt.title( 'CORE_arrangement' )
    plt.figure(figsize=(12,8))
    plt.show()

center=[( 0 , 0 ),( 4 , 0 ),( 8 , 0 ),( -4 , 0 ),( -8 , 0 ),( 4, 4),( 4 , 8 ),( 8 , 4 ),( -4, 4),
( -4 , 8 ),( -8 , 4 ),( -8 , -4 ),( -4, 4),( -4 , -8 ),( -8 , -4 ),( 0, 4),( 0 , 8 ),( 0, -4),( 0 , -8 ),
( 4, -4),( 4 , -8 ),( -4, -4),( 8, -4)
]

CoreVisualize(center,radius=1)
