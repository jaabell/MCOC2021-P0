# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 22:08:25 2021

@author: matia
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 17:44:04 2021
@author: matia
"""


from scipy import matmul, rand 
from time import perf_counter 

import matplotlib.pylab as plt 


ListNs=[]
ListDtEnsamblaje=[]
ListDtInversion=[]


ListM=[]
ListUsoMemoria=[]
fid = open("MatrizDispersa,double(inv).txt","r")
n=0
l1=[]
l2=[]
l3=[]

for line in fid:
    n+=1
    sl = line.split()
    #print(sl)
    N=float(sl[0])
    tE=float(sl[1])
    tI=float(sl[2])
    
    l1.append(N)
    l2.append(tE)
    l3.append(tI)
    
    
    if n==15:
        n=0
        ListNs.append(l1)
        ListDtEnsamblaje.append(l2)
        ListDtInversion.append(l3)
        l1=[]
        l2=[]
        l3=[]
        
        
   
    
fid.close()    


y=ListDtEnsamblaje
yy=ListDtInversion

x=[2,5,10,15,20,25,50,100,200,500,1000,2000,5000,10000,15000]
#
labels_x = [2,5,10,15,20,25,50,100,200,500,1000,2000,5000,10000,15000]
Ns = [2,5,10,15,20,25,50,100,200,500,1000,2000,5000,10000,15000]
labels_y = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
dts = [10**(-4),10**(-3),10**(-2),10**(-1),10**(0),10,60,600]

labels_y2 =["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","12 GB"]
mems1 = [10**(3),10**(4),10**(5),10**(6),10**(7),10**(8),10**(9),12**(10)]

max1=0
max2=0

for s in y:
    ss=max(s)
    if ss>=max1:
        max1=ss
for s in yy:
    ss=max(s)
    if ss>=max2:
        max2=ss
                
        
fx=0.00001       
fx2=fx*fx
fx3=fx2*fx
#grafico ensamblaje
plt.figure(1)

plt.subplot(2,1,1)
plt.title("Rendimiento A@B")
plt.loglog(x,y[0],marker="o", color='k')
plt.loglog(x,y[1],marker="o", color='k')
plt.loglog(x,y[2],marker="o", color='k')
plt.loglog(x,y[3],marker="o", color='k')
plt.loglog(x,y[4],marker="o", color='k')
plt.loglog(x,y[5],marker="o", color='k')
plt.loglog(x,y[6],marker="o", color='k')
plt.loglog(x,y[7],marker="o", color='k')
plt.loglog(x,y[8],marker="o", color='k')

plt.loglog([2,30000],[max1,max1],marker=' ', color='b', linestyle='--', label = "Constante")
plt.loglog([2,30000],[fx,max1],marker=' ', color='orange', linestyle='--', label = "O(N)")
plt.loglog([500,30000],[fx,max1],marker=' ', color='g', linestyle='--', label = "O(N^2)")
plt.loglog([2000,30000],[fx,max1],marker=' ', color='r', linestyle='--', label = "O(N^3)")
plt.loglog([2000 ,30000],[fx,max1],marker=' ', color='m', linestyle='--', label = "O(N^4)")

#plt.legend(loc="upper left")



plt.plot((5))



plt.xticks(Ns,labels_x)
plt.yticks(dts,labels_y)
plt.grid(True)
plt.xticks(visible=False)
plt.ylabel("Tiempo ensamblado(S)")

#grafico inversion
plt.subplot(2,1,2)
plt.loglog(x,yy[0],marker="o",color='k')
plt.loglog(x,yy[1],marker="o",color='k')
plt.loglog(x,yy[2],marker="o",color='k')
plt.loglog(x,yy[3],marker="o",color='k')
plt.loglog(x,yy[4],marker="o",color='k')
plt.loglog(x,yy[5],marker="o",color='k')
plt.loglog(x,yy[6],marker="o",color='k')
plt.loglog(x,yy[7],marker="o",color='k')
plt.loglog(x,yy[8],marker="o",color='k')
plt.loglog(x,yy[9],marker="o",color='k')


plt.loglog([2,30000],[max2,max2],marker=' ', color='b', linestyle='--', label = "Constante")
plt.loglog([2,30000],[fx,max2],marker=' ', color='orange', linestyle='--', label = "O(N)")
plt.loglog([200,30000],[fx,max2],marker=' ', color='g', linestyle='--', label = "O(N^2)")
plt.loglog([1000,30000],[fx,max2],marker=' ', color='r', linestyle='--', label = "O(N^3)")
plt.loglog([2000 ,30000],[fx,max2],marker=' ', color='m', linestyle='--', label = "O(N^4)")
plt.legend(loc="upper left")


plt.xticks(Ns,labels_x,rotation=45)
plt.yticks(dts,labels_y)
plt.grid(True)
plt.ylabel("Tiempo transcurrido (S)")
plt.xticks(visible=True)
plt.xlabel("Tamaño matriz N")

plt.show()