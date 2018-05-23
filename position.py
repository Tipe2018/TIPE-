<<<<<<< HEAD

'Intégrations des valeurs pour obtenir la position'
import numpy as np
#Pour le graphe 3D
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as pl
import random as r

def position (Lx,Ly,Lz,fin,n): 
#L liste des accélérations,de t=0 à t=fin, n=taille de L
    vitesseX=[]
    vitesseY=[]
    vitesseZ=[]
    
    positionX=[]
    positionY=[]
    positionZ=[]
    
    'méthode des trapèzes'
    tau=fin/n # tau=(b-a)/n avec a=0, b=fin
    
    for k in range (1,n):
        vx=tau*(Lx[k-1]+Lx[k])/2 # vitesse suivant x
        vitesseX.append(vx)
        
        vy=tau*(Ly[k-1]+Ly[k])/2 # vitesse suivant y
        vitesseY.append(vy)
        
        vz=tau*(Lz[k-1]+Lz[k])/2 # vitesse suivant z
        vitesseZ.append(vz)
    
    for i in range (1,n-2):
        px=tau*(vitesseX[i]+vitesseX[i+1])/2
        positionX.append(px)
        
        py=tau*(vitesseY[i]+vitesseY[i+1])/2
        positionY.append(py)
        
        pz=tau*(vitesseZ[i]+vitesseZ[i+1])/2
        positionZ.append(pz)
    print (positionX)


    #Graphe de la position du ballon'
    fig=pl.figure()
    ax = fig.gca(projection='3d')
    ax.plot(positionX, positionY, positionZ)
    pl.show()

=======

'Intégrations des valeurs pour obtenir la position'
import numpy as np
#Pour le graphe 3D
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as pl

def position (Lx,Ly,Lz,fin,n): 
#L liste des accélérations,de t=0 à t=fin, n=taille de L
    vitesseX=[]
    vitesseY=[]
    vitesseZ=[]
    
    positionX=[]
    positionY=[]
    positionZ=[]
    
    'méthode des trapèzes'
    tau=fin/n # tau=(b-a)/n avec a=0, b=fin
    
    for k in range (n-1):
        vx=tau*(Lx[k]+Lx[k+1])/2 # vitesse suivant x
        vitesseX.append(vx)
        
        vy=tau*(Ly[k]+Ly[k+1])/2 # vitesse suivant x
        vitesseY.append(vy)
        
        vz=tau*(Lz[k]+Lz[k+1])/2 # vitesse suivant x
        vitesseZ.append(vz)
    
    for i in range (n-2):
        px=tau*(vitesseX[i]+vitesseX[i+1])/2
        positionX.append(px)
        
        py=tau*(vitesseY[i]+vitesseY[i+1])/2
        positionY.append(py)
        
        pz=tau*(vitesseZ[i]+vitesseZ[i+1])/2
        positionZ.append(pz)
    return positionX, positionY, positionZ
    
           
    #Graphe de la position du ballon'
    fig=pl.figure()
    ax = fig.gca(projection='3d')
    ax.plot(positionX, positionY, positionZ)
    pl.show()
>>>>>>> dd1f5ead37177fcd831be51157c9326bbc1aeec1
