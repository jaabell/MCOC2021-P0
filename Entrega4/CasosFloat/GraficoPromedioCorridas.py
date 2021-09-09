# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 17:52:09 2021

@author: matia
"""

from scipy import matmul, rand 
from time import perf_counter 

import matplotlib.pylab as plt 

def promediolist(x):
    ListNs=[]
    Listdt=[]
    ListDts=[]
    ListM=[]
    ListProm=[]
    ListUsoMemoria=[]
    o=open(x,"r")
    n=0
    for line in o:
        n+=1
        
        ListNs1=[]
    
        sl = line.split()
       
        N = int(sl[0])
        dt = float(sl[1])
        men= int(sl[2])
        
        Listdt.append(dt)
        ListM.append(men)
        
        if n==14:
            
            ListDts.append(Listdt)
            ListUsoMemoria.append(ListM)
            n=0
            Listdt=[]
            ListM=[]
            
    y=ListDts    
    a=0

    while a<=13:
        v=0
        suma=0
        for x in y:
            suma+=x[a]
            v+=1
            if v==len(y):
                dd=suma/v
                ListProm.append(dd)
                
                v=0
                a+=1
  
        
   
    return ListProm


       
    
A1=promediolist("casoI,float.txt")    
          
A2=promediolist("casoII,float.txt") 
             
#A3=promediolist("casoIII,float.txt")    
       
A4=promediolist("casoIV,float.txt") 
      
A5=promediolist("casoV,float.txt")    
A6=promediolist("casoVI,float.txt")    
A7=promediolist("casoVII,float.txt")    

B1=promediolist("casoB(I),float.txt")    
B2=promediolist("casoB(II),float.txt")    
B3=promediolist("casoB(III),float.txt")    
B4=promediolist("casoB(IV),float.txt")    
B5=promediolist("casoB(V),float.txt")  

            

        


       
       

x=[2,5,10,15,20,25,50,100,200,500,1000,2000,5000,10000]

labels_x = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
Ns = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

labels_y = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
dts = [10**(-4),10**(-3),10**(-2),10**(-1),10**(0),10,60,600]

labels_y2 =["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","12 GB"]
mems1 = [10**(3),10**(4),10**(5),10**(6),10**(7),10**(8),10**(9),12**(10)]
s=0

#grafico uso de memoria 
plt.figure(1)

plt.subplot(2,1,1)
plt.title("Rendimiento A@B")
plt.loglog(x,A1,marker="o")
plt.loglog(x,A2,marker="o")

plt.loglog(x,A4,marker="o")
plt.loglog(x,A5,marker="o")
plt.loglog(x,A6,marker="o")
plt.loglog(x,A7,marker="o")
plt.loglog(x,B1,marker="o")
plt.loglog(x,B2,marker="o")
plt.loglog(x,B3,marker="o")
plt.loglog(x,B4,marker="o")
plt.loglog(x,B5,marker="o")



plt.xticks(Ns,labels_x)
plt.yticks(dts,labels_y)
plt.grid(True)
plt.xticks(visible=True)
plt.ylabel("Promedio Tiempo transcurrido (S)")

plt.xticks(visible=True)
plt.xlabel("Tamaño matriz N")

plt.show()


