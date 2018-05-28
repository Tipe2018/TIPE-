from numpy import *
from random import *

L=[randrange(0,1000)for k in range (1001)]
def moy(L,n):# n nb elm moy glissante
    R=[]
    for i in range (0,len(L)-n,n):
        S=0
        for j in range (i,i+n):
            S+=L[j]
        R.append(S/n)
    return R

print (L)
print (moy(L,10))
print (len(L),len (moy(L,10)))
