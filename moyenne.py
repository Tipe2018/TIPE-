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



#=========================================
from tkinter import *
from math import cos,sin,pi,atan
import time

def animation():
    global alpha,beta,phi
    x=LectureI2CAccelerometre(0x1D,bus)
    if x[1]==0 :
        angle=pi/2
    elif x[1]>0 :
        angle=atan(x[0]/x[1])+pi
    elif x[1]<0 :
        angle=atan(x[0]/x[1])
    P1=150+x[1]/40 
    P2=150+x[0]/40
    can1.delete("un")
    P=[100*cos(angle)+150,100*sin(angle)+150,10*cos(angle+pi/2)+150,10*sin(angle+pi/2)+150,100*cos(angle+pi)+150,100*sin(angle+pi)+150,10*cos(angle+3*pi/2)+150,10*sin(angle+3*pi/2)+150,100*cos(angle)+150,100*sin(angle)+150]
    Pbis=[P[0],P[1],P[2],P[3],P[6],P[7],P[0],P[1]]
    can1.create_polygon(P,fill="white", width=2, outline='black',tag="un")
    can1.create_polygon(Pbis,fill="red", width=2, outline='black',tag="un")    
    fenetre.after(50,animation)
# Creation de la fenetre d'affichage Tkinter
fenetre = Tk()
fenetre.title("Boussole")

can1 = Canvas(fenetre,bg='white', height=300, width=300)
can1.pack(side=LEFT, padx =5, pady =5)
can1.create_oval(25,25,275,275,fill="#EEEEEE", width=2, outline="black")
can1.create_oval(40,40,260,260,fill="#F9F9F9", width=2, outline="black")
for i in range(36) :
    P=[105*cos(2*(i+1)*pi/36)+150,105*sin(2*(i+1)*pi/36)+150,110*cos(2*(i+1)*pi/36)+150,110*sin(2*(i+1)*pi/36)+150]
    can1.create_line(P,width=1)
can1.create_text(150,35,text="N")
can1.create_text(150,270,text="S")
can1.create_text(270,150,text="E")
can1.create_text(35,150,text="O")

animation()
fenetre.mainloop()
