# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 21:57:22 2021

@author: matia
"""


from time import perf_counter 
from numpy import zeros, half, single , double , longdouble, eye ,ones,float
import scipy.sparse as sparse 
from scipy.linalg import inv ,solve ,eigh
from scipy import matmul

def laplaciana(N,dtype):
    A = zeros((N,N),dtype=dtype)
    
    for i in range(N):
        A[i,i]=2
      
        for j in range(max(0,i-2),i):
            if abs(i-j)==1:
                   A[i,i]=-1
                   A[j,i]=-1               
    return A

ListNs=[2,5,10,15,20,25,50,100,200,500,1000,2000,5000,10000,15000]
#
ListDtsInversion=[]
ListDtsEnsamblaje=[]

fid = open("MatrizLlena,double(inv).txt","w") #vario el nombre dependendiendo del caso para lograr los archivos txt
time=1
while time<=10:
    print(time)
    time+=1
    
    for N in ListNs:    
     
        
        t1 = perf_counter()
            
        a=laplaciana(N,dtype=double) #dependiendo el caso lo cambio para float o double
       # b=ones(N)
        #A=sparse.csr_matrix(a)
        #B=sparse.csr_matrix(b)
       
        t2 = perf_counter()
        #print(A)
        
        am1= inv(a)
        
        #mul=solve(am1,b) #este solamente lo ocupamos para caso matriz llena
        
    
        t3 = perf_counter()
        
        dt_ensamblaje = t2-t1
        
        dt_inversion = t3-t2
        
        #bytes_total= a.nbytes + am1.nbytes
        
        #print(f"Uso memoria:{bytes_total}s ")
        
       # print(f"Tiempo ensamblaje: {dt_ensamblaje}s")
        
        #print(f"Tiempo inversion: {dt_inversion}s")

         
         
        #UsoMemoriaTeorico=4*N*N
        #UsoMemoriaNumpy=a.nbytes
          
         
        #UsoMemoriaTotal=bytes_total
             
        
        ListDtsEnsamblaje.append(dt_ensamblaje)
        ListDtsInversion.append(dt_inversion)
       # ListUsoMemoria.append(UsoMemoriaTotal)
        # print( UsoMemoriaTotal)
       
        print(f"N={N} dt_ensamblaje={dt_ensamblaje} dt_inversion={dt_inversion} ")
        fid.write(f"{N} {dt_ensamblaje} {dt_inversion}\n ")
     
    
     
            
fid.close()