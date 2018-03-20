'''============= Intégration des valeurs de la centrale inertielle ========='''
'''========================pour avoir la position==========================='''

import numpy as np

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
        
         