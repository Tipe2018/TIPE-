
import csv

file=open("test.csv",'w',newline='')
ecriture=csv.writer(file,dialect='excel',delimiter=';')
ecriture.writerows([["test","essaie"],[23,45,5]]) # valeurs de test 

file.close()

# test ok il faut creer des couples pour les valeurs [valeur,temps]
#puis les ajouter a tour de role dans la liste principal et ecrire le csv avec cette liste 
