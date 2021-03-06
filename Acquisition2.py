# -*- coding: latin-1 -*-
#Driver for the LSM303D accelerometer and magnetometercompass




 #tst


#First follow the procedure to enable I2C on R-Pi.



#1. Add the lines ic2-bcm2708 and i2c-dev to the file etcmodules



#2. Comment out the line blacklist ic2-bcm2708 (with a #) in the file etcmodprobe.draspi-blacklist.conf



#3. Install I2C utility (including smbus) with the command apt-get install python-smbus i2c-tools



#4. Connect the I2C device and detect it using the command i2cdetect -y 1.  It should show up as 1D or 1E (here the variable LSM is set to 1D).







#Driver by Fayetteville Free Library Robotics Group







import time
import math
from smbus import SMBus
import numpy as np
from fonctions import * 
#from fonctionstest import *
# fichiers de toutes les fonctions de ce programme ainsi que certains réglages
import csv # pour convertir la liste de toutes les valeurs en csv



# Numéro du bus utilisé

busNum = 1

b = SMBus(busNum)

'''détection  du capteur'''
detection()

'''Programmation des controles'''
reglages()





'''Réglages'''
DT = 0.01 # pris de la datsheet

#nombre pi
PI = np.pi

# conversion radian en degrés (*180/PI)
RAD_TO_DEG = 57.29578



AA = 0.98 



'''Initialisation des angles'''

#Sur x
gyrox_angle = 0.0
#Sur y
gyroy_angle = 0.0
#Sur z
gyroz_angle = 0.0

'''Création des listes '''
Ax=[] # accélération sur x
Ay=[] #sur y
Az=[] # sur z

Rx=[]#Rotation sur x
Ry=[]
Rz=[]

Temps=[] #Liste du temps de l'acquisition d'une valeur

#Entrée de l'utilisateur
temps=int(input("Temps d'acquisition en secondes"))



t=time.clock()
T=[t] #liste des moments où l'acquisition est faite
i=0
temps_boucle=time.clock()
while T[i]<temps:
    
    #Acquisition de l'accélération
    accx,accy,accz=acceleration() 
    #Acquisition du gyroscope
    gyrox, gyroy, gyroz =gyroscope()
    t=time.clock()-t
    T.append(T[i]+t)
    i+=1
    print (T[i-1])
    Ax.append(accx)
    Ay.append(accy)
    Az.append(accz)
    Rx.append(gyrox)
    Ry.append(gyroy)
    Rz.append(gyroz)
    time.sleep(0.001) # prend 4 mesures par secondes
temps_boucle-=time.clock()
print ('Fin acquisition + mise en csv')
print ('temps boucle'+str(temps_boucle))

Axf=filtrage(Ax,1)
Ayf=filtrage(Ay,2)
Azf=filtrage(Az,3)

#moyenne des valeurs pour minimiser le bruit:
n=250
Ax_moy=moy(Axf,n,0)
Ay_moy=moy(Ayf,n,0)
Az_moy=moy(Azf,n,0)
Rx_moy=moy(Rx,n,0)
Ry_moy=moy(Ry,n,0)
Rz_moy=moy(Rz,n,0)
T_moy=moy(T,n,1)

#filtrage des valeurs dont la variation est inf au cm


Liste=[T,Axf,Ayf,Azf,Rx,Ry,Rz] #Liste des listes de valeurs
conversion(Liste)           #Conversion de la liste de listes en csv
print ('Fichier converti')
