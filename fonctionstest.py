# -*- coding: latin-1 -*-
import csv 
def conversion(l): # convertit liste en csv

    file=open("valeurs.csv",'w',)
    
    ecriture=csv.writer(file,dialect='excel',delimiter=';')
    ecriture.writerow(['Temps', 'AccX','AccY','AccZ','RotX','RotY','RotZ'])
    for i in range (len (l[0])-1):
        ecriture.writerow([l[0][i],l[1][i],l[2][i],l[3][i],l[4][i],l[5][i],l[6][i]]) 
    file.close()


def moy(L,n,t):# n nb elm moy glissante
    R=[]
    for i in range (0,len(L)-n,n):
        S=0
        for j in range (i,i+n):
            if t==1:
                S+=L[j] #car on ne doit pas appliquer le coeff au temps
            if t==0:
                S+=L[j]*10 # car mesuré en accélération (g)
        R.append(S/n)
    return R

def filtrage(L,a): 
    #Centrale précise au cm, donc toutes décimales après 0.01 sont rendues nulles
    for i in range (len(L)):
        if a==1: #Accélération sur x
            L[i]=round(L[i],2)+512
        if a==2: #Accélération sur y
            L[i]=round(L[i],2)+768
        if a==3: #Accélération sur y
            L[i]=round(L[i],2)+15104
    return L
