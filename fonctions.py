# -*- coding: latin-1 -*-
# Numéro du bus utilisé
from smbus import SMBus
busNum = 1
b = SMBus(busNum)

''' D'après la datasheet du LSM303D: Registres des MSB et LSB:'''

" - du magnétomètre " 
#Suivant x
MAG_X_LSB = 0x08
MAG_X_MSB = 0x09

# suivant y
MAG_Y_LSB = 0x0A
MAG_Y_MSB = 0x0B

#Suivant z
MAG_Z_LSB = 0x0C 
MAG_Z_MSB = 0x0D

" - de l'accélération "

#Suivant x
ACC_X_LSB = 0x28 
ACC_X_MSB = 0x29

#Suivnt y
ACC_Y_LSB = 0x2A 
ACC_Y_MSB = 0x2B

#Suivant z
ACC_Z_LSB = 0x2C 
ACC_Z_MSB = 0x2D

" - de la température "

TEMP_MSB = 0x05

TEMP_LSB = 0x06


"Registres de lecture du gyroscope"

# Sur x

LGD_GYRO_X_LSB = 0x28

LGD_GYRO_X_MSB = 0x29

#Sur y

LGD_GYRO_Y_LSB = 0x2A

LGD_GYRO_Y_MSB = 0x2B

#Sur z

LGD_GYRO_Z_LSB = 0x2C

LGD_GYRO_Z_MSB = 0x2D


''' Registres du LSM303D '''
LSM = 0x1d #I2C Adresse du LSM303D
LSM_WHOAMI_ID = 0b1001001 #Device self-id
LSM_WHOAMI_ADDRESS = 0x0F

''' Registres du L3GD20H '''
LGD = 0x6b #Device I2C slave address
LGD_WHOAMI_ADDRESS = 0x0F
LGD_WHOAMI_ID = 0b11010111 #Device self-id

'''Combinaison du bit fort/ faible''' 
def combiner (msb,lsb):

    # les valeurs prises sont des valeurs de référence

    combinaison = 256*msb + lsb

    if combinaison >= 32768:

        return combinaison - 65536

    else:

        return combinaison





def detection ():

    LSM303D=False

    L3GD20H=False

    if b.read_byte_data(LSM, LSM_WHOAMI_ADDRESS) == LSM_WHOAMI_ID:

        LSM303D = True 

        return print ('LSM303D détecté.')

    else:

        print ('LSM303D non détecté sur le bus '+str(busNum)+'.')

    if b.read_byte_data(LGD, LGD_WHOAMI_ADDRESS) == LGD_WHOAMI_ID:

        L3GD20H= True        

        return print ('L3GD20H détecté.')

    else:

        return print ('No L3GD20H detected on bus on I2C bus '+str(busNum)+'.')

        

    if LSM303D== True and L3GD20H==True:

        return print ('Tous les éléments sont détectés')


'''==========Programmation des controles=================='''

'''Adresse des registres de controle (d'après la datasheet du LSM303D)'''

"Paramètres généraux"
CTRL_0 = 0x1F 

"Active l'accéléromètre"
CTRL_1 = 0x20 #configures data 

"Auto-test de l'accéléromètre"
CTRL_2 = 0x21 # anti-aliasing accel filter

"Interruption" 
CTRL_3 = 0x22 
CTRL_4 = 0x23 

"Active le capteur de température"
CTRL_5 = 0x24 

"Sélection de la résolution du magnétomètre, data rate config"
CTRL_6 = 0x25 

"Active le magnétomètre et ajuste le mode"
CTRL_7 = 0x26 

"Activation du gyroscope"

LGD_CTRL_1 = 0x20 

LGD_CTRL_2 = 0x21 #can set a high-pass filter for gyro

LGD_CTRL_3 = 0x22

LGD_CTRL_4 = 0x23

LGD_CTRL_5 = 0x24

LGD_CTRL_6 = 0x25

LGD_TEMP = 0x26


def reglages ():
    #Activation de l'accéléromètre et activation des axes x,y,z"
    b.write_byte_data(LSM, CTRL_1, 0b1100111)
    #échantillonnage des relevés à 100H

    

    #Réglage de la plage d'accéléromètre/ de mesure"
    b.write_byte_data(LSM, CTRL_2, 0b0000000) 
    #Tous les réglages sont par défaut
    # set +/- 2g (g: constante gravitationelle)

    

    #Réglage de la résolution du magnétomètre + désactivation du thermomètre"
    b.write_byte_data(LSM, CTRL_5, 0b01100100)
    # 6.25hz ODR ???

    

    #Réglage de la plage de calcul du magnétomètre"
    b.write_byte_data(LSM, CTRL_6, 0b00100000)
    

    b.write_byte_data(LSM, CTRL_7, 0x00)
    # Magnétmètre plus sur mode économie

    #Allume le gyroscope et le paramètre en mode normal"
    b.write_byte_data(LGD, LGD_CTRL_1, 0x0F)

    

    #set 2000 dps full scale ???
    b.write_byte_data(LGD, LGD_CTRL_4, 0b00110000) 

def acceleration():
    #Calcul de l'accélération"
    accx = combiner(b.read_byte_data(LSM, ACC_X_MSB), b.read_byte_data(LSM, ACC_X_LSB))
    accy = combiner(b.read_byte_data(LSM, ACC_Y_MSB), b.read_byte_data(LSM, ACC_Y_LSB))
    accz = combiner(b.read_byte_data(LSM, ACC_Z_MSB), b.read_byte_data(LSM, ACC_Z_LSB))
    
    #Coeff appliqués ???
    accx = accx * 0.061 * 0.001
    accy = accy * 0.061 * 0.001
    accz = accz * 0.061 * 0.001 - 0.1

    return accx,accy,accz

def gyroscope():
    gyrox = combiner(b.read_byte_data(LGD, LGD_GYRO_X_MSB), b.read_byte_data(LGD, LGD_GYRO_X_LSB))
    gyroy = combiner(b.read_byte_data(LGD, LGD_GYRO_Y_MSB), b.read_byte_data(LGD, LGD_GYRO_Y_LSB))
    gyroz = combiner(b.read_byte_data(LGD, LGD_GYRO_Z_MSB), b.read_byte_data(LGD, LGD_GYRO_Z_LSB))

    return gyrox, gyroy, gyroz

def conversion(liste): # convertit en csv
    file=open("valeurs.csv",'w',newline='')
    ecriture=csv.writer(file,dialect='excel',delimiter=';')
    ecriture.writerows([liste]) 
    file.close()