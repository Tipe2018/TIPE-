# -*- coding: latin-1 -*-
'Intégrations des valeurs pour obtenir la position'

import numpy as np
#Pour le graphe 3D
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as pl
import random as r
import csv  


def origine(L): #pour mettre la première valeur a l'origine
    orig=L[0] 
    for i in range (len(L)):
        L[i]-=orig
    L[0]=0
    return L

file=open('valeurs.csv','r')
file.readline() #lis la 1e ligne( celle des textes)
Lx,Ly,Lz,T=[],[],[],[]
fichier=csv.reader(file, delimiter=';')
for ligne in fichier:
    Lx.append(eval(ligne[1]))
    Ly.append(eval(ligne[2]))
    Lz.append(eval(ligne[3]))
    T.append(eval(ligne[0]))

def position (Lx,Ly,Lz,fin,n): 
#L liste des accélérations,de t=0 à t=fin, n=taille de L
    vitesseX=[]
    vitesseY=[]
    vitesseZ=[]
    
    positionX=[]
    positionY=[]
    positionZ=[]
    
    #méthode des trapèzes
    tau=float(fin)/n # tau=(b-a)/n avec a=0, b=fin
    
    for k in range (0,n-1):
        vx=tau*(Lx[k]+Lx[k+1])/2 # vitesse suivant x
        vitesseX.append(vx)
        
        vy=tau*(Ly[k]+Ly[k+1])/2 # vitesse suivant y
        vitesseY.append(vy)
        
        vz=tau*(Lz[k]+Lz[k+1])/2 # vitesse suivant z
        vitesseZ.append(vz)
    
    for i in range (0,n-2):
        px=tau*(vitesseX[i]+vitesseX[i+1])/2
        positionX.append(px)
        
        py=tau*(vitesseY[i]+vitesseY[i+1])/2
        positionY.append(py)
        
        pz=tau*(vitesseZ[i]+vitesseZ[i+1])/2
        positionZ.append(pz)
    
    #mise à l'origine des listes
    positionX_orig=origine(positionX)
    positionY_orig=origine(positionY)
    positionZ_orig=origine(positionZ)

    #Graphe de la position du ballon'
    fig=pl.figure()
    ax = fig.gca(projection='3d')
    ax.plot(positionX_orig, positionY_orig, positionZ_orig)
    ax.plot([0],[0],[0],'rx')
    
    pl.xlabel('axe des x')
    pl.ylabel('axe des y')
    
    pl.show()
    pl.close()
    pl.plot(T,Lx,'*')
    pl.plot(T,Ly,'*')
    pl.plot(T,Lz,'*')
    pl.legend(['Lx','Ly','Lz'])
    pl.show()
position (Lx,Ly,Lz,T[-1],len(T))
print (len(Lx))
print (len(Ly))
print (len(Lz))
print (len(T))




##Test:
#t=np.linspace (0,5,20)
#Lx=[r.randrange(0,20,1) for i in range (20)]
#Ly=[r.randrange(0,20,1) for i in range (20)]
#Lz=[r.randrange(0,20,1) for i in range (20)]
#position(Lx,Ly,Lz,t[len(t)-1],20)