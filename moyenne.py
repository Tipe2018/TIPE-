from numpy import *
from random import *

L=[randrange(0,1000)for k in range (20)]
def moy(L,n):# n nb elm moy glissante
    R=[]
    for i in range (0,len(L)-n,n):
        S=0
        for j in range (i,i+n):
            S+=L[j]*10 # car altimu calcul en g accélération
        R.append(S/n)
    return R

#print (L)
#print (moy(L,2))
#print (len(L),len (moy(L,2)))

def origine(L):
    orig=L[0]
    for i in range (len(L)):
        L[i]-=orig
    L[0]=0
    return L

#print (origine(L))

L=[randrange(0,1000)for k in range (20)]
def filtrage(L): 
    #Centrale précise au cm, donc toutes décimales après 0.01 sont rendues nulles
    for i in range (len(L)-1):
        L[i]=round(L[i],2)
    return L
#print (L)
#print (filtrage(L))

print (round(4.0826,3))