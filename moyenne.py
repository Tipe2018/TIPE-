from numpy import *
from random import *

L=[randrange(0,1000)for k in range (20)]
def moy(L,n):# n nb elm moy glissante
    R=[]
    for i in range (0,len(L)-n,n):
        S=0
        for j in range (i,i+n):
            S+=L[j]
        R.append(S/n)
    return R

print (L)
#print (moy(L,2))
#print (len(L),len (moy(L,2)))

def origine(L):
    orig=L[0]
    for i in range (len(L)):
        L[i]-=orig
    L[0]=0
    return L

print (origine(L))