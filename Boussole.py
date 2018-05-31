from Tkinter import *
from math import cos,sin,pi,atan
import time
from smbus import SMBus

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
    
def convert(NbSigne):#conversion du nombre signe
    if NbSigne<32768 :
        return NbSigne
    else :
        return (-(65536-NbSigne))

def LectureI2CAccelerometre(addr,bus):
    x1 = bus.read_byte_data(addr,0x08)
    x2 = bus.read_byte_data(addr,0x09)
    y1 = bus.read_byte_data(addr,0x0A)
    y2 = bus.read_byte_data(addr,0x0B)
    z1 = bus.read_byte_data(addr,0x0C)
    z2 = bus.read_byte_data(addr,0x0D)
    x=x1+x2*256
    x=convert(x)
    y=y1+y2*256
    y=convert(y)
    z=z1+z2*256
    z=convert(z)
    return [x,y,z]

# Initialisation des angles
alpha,beta,phi=0,0,0

# Initialisation du capteur
bus=SMBus(1)
bus.write_byte_data(0x1D,0x24,0x08)          #configuration du registre CTRL1
bus.write_byte_data(0x1D,0x25,0x00)
bus.write_byte_data(0x1D,0x26,0x04)

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
