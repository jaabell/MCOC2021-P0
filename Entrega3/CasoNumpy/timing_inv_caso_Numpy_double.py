# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:35:34 2021

@author: matia
"""


from scipy import matmul, rand 
from time import perf_counter 

import matplotlib.pylab as plt 


ListNs=[]
Listdt=[]
ListDts=[]
ListM=[]
ListUsoMemoria=[]
fid = open("caso3.txt","r")
n=0
for line in fid:
    n+=1
    
    ListNs1=[]

    sl = line.split()
   
    N = int(sl[0])
    dt = float(sl[1])
    men= int(sl[2])
    
    Listdt.append(dt)
    ListM.append(men)
    
    if n==10:
        
        ListDts.append(Listdt)
        ListUsoMemoria.append(ListM)
        n=0
        Listdt=[]
        ListM=[]
        
        
        
   
    
fid.close()    

import matplotlib.pylab as plt 
y=ListDts

x=[10,20,50,100,200,500,1000,2000,5000,10000]

labels_x = ["10","20","50","100","200","500","1000","2000","5000","10000"]
Ns = [10,20,50,100,200,500,1000,2000,5000,10000]

labels_y = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
dts = [10**(-4),10**(-3),10**(-2),10**(-1),10**(0),10,60,600]

labels_y2 =["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","12 GB"]
mems1 = [10**(3),10**(4),10**(5),10**(6),10**(7),10**(8),10**(9),12**(10)]




#grafico uso de memoria 
plt.figure(1)

plt.subplot(2,1,1)
plt.title("Rendimiento A@B")
plt.loglog(x,y[0],marker="o")
plt.loglog(x,y[1],marker="o")
plt.loglog(x,y[2],marker="o")
plt.loglog(x,y[3],marker="o")
plt.loglog(x,y[4],marker="o")
plt.loglog(x,y[5],marker="o")
plt.loglog(x,y[6],marker="o")
plt.loglog(x,y[7],marker="o")
plt.loglog(x,y[8],marker="o")
plt.loglog(x,y[9],marker="o")




plt.xticks(Ns,labels_x)
plt.yticks(dts,labels_y)
plt.grid(True)
plt.xticks(visible=False)
plt.ylabel("Tiempo transcurrido (S)")


plt.subplot(2,1,2)
plt.loglog(x,ListUsoMemoria[0],marker="o")
plt.xticks(Ns,labels_x)
plt.yticks(mems1,labels_y2)
plt.grid(True)
plt.xticks(visible=True)
plt.xlabel("Tamaño matriz N")

plt.show()