
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
# fichiers de toutes les fonctions de ce programme ainsi que certains réglages
import csv # pour convertir la liste de toutes les valeurs en csv



# Numéro du bus utilisé

busNum = 1

b = SMBus(busNum)


'''Programmation des controles'''
reglages()





'''Réglages'''
DT = 0.01 # pris de la datsheet ???

#nombre pi
PI = np.pi

# conversion radian en degrés (*180/PI)
RAD_TO_DEG = 57.29578



AA = 0.98 #???



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
#tps_acqui=0 # valeur du temps pour chaque mesure
stop=0 #arret de la boucle
boucle_ok=0 #Si le while s'effectue en entier sans problème

tps_out=time.clock() #assurance si jamais le while fait une boucle infinie
#while stop ==0:
#    t1 = time.clock()
#    
#    #Accélération
#    accx,accy,accz=acceleration() 
#
#    Ax.append(accx)
#    Ay.append(accy)
#    Az.append(accz)
#
#
#    #Gyroscope"
#    gyrox, gyroy, gyroz =gyroscope()
#
#    Rx.append(gyrox)
#    Ry.append(gyroy)
#    Rz.append(gyroz) 
#  
#    t2=time.clock()
#    
#    t=t2-t1 #Durée de la boucle
#    temps=temps-t
#    tps_acqui+=t
#    Temps.append(tps_acqui)
#    
#    if tps_out> temps+10: #le temps demandé par l'utilisateur est dépassé (boucle infinie)
#        stop=1 
#
#    if temps<=0:
#        print("Fin de l'acquisition")
#        stop=1
#        boucle_ok=1

#Liste=[Temps,Ax,Ay,Az,Rx,Ry,Rz] #Liste des listes de valeurs

if stop==1 and boucle_ok==1:
    #Conversion de la liste de listes en csv
    conversion(Liste)

t=0
t=clock()
T=[t] #liste des moments où l'acquisition est faite
while t<temps:
    t1=time.clock()
    accx,accy,accz=acceleration() 
    t2=time.clock()
    t=t+t2-t1
    T.append(t)
    print (accx,accy,accz,t)



