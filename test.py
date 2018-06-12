from fonctionstest import *
from random import *

L=[random() for k in range(1000)]


print(L)
filtrage(L)
print(L)

R=moy(L,250)
print(R)