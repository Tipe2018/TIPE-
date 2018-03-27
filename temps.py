from time import clock
Temps=[]
temps=int(input("temps d'acquisition"))
tps_out=clock()
stop=0
boucle_ok=0
x=0
while stop ==0:
    t1=clock()
    x=x+1
    t2=clock()
    t=t2-t1
    temps=temps-t
    Temps.append(t)
    if tps_out>temps+10:
        stop=1
    if temps<=0:
        print('fin aquisition')
        stop=1
        boucle_ok=1
