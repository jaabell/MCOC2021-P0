# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 08:58:09 2021

@author: matia
"""

from time import perf_counter 
from numpy import zeros, half, single , double , longdouble, eye ,ones,float

from scipy.linalg import inv ,solve ,eigh

def laplaciana(N,dtype):
    A = zeros((N,N),dtype=dtype)
    
    for i in range(N):
        A[i,i]=2
      
        for j in range(max(0,i-2),i):
            if abs(i-j)==1:
                   A[i,i]=-1
                   A[j,i]=-1
                   
                   
              
                 
                 
                  
    return A

ListNs=[2,5,10,15,20,25,50,100,200,500,1000,2000,5000,10000]
#
ListDts=[]
ListUsoMemoria=[]

fid = open("casoB(V),double.txt","w") #vario el nombre dependendiendo del caso para lograr los archivos txt

time=1


while time<=10:
    print(time)
    time+=1
    
    for N in ListNs:    
     
        
        t1 = perf_counter()
            
        a=laplaciana(N,dtype=double) #dependiendo el caso lo cambio para float o double
        b=ones(N)
        t2 = perf_counter()
        #print(A)
        am1= inv(a)
        
        #mul=am1@b  #este solamente lo ocupamos para el caso I
        #mul=solve(a,b, sym_pos=False, lower=False, overwrite_a=False, overwrite_b=False, debug=None, check_finite=True, assume_a='gen', transposed=False)#caso2
        #mu=solve(a, b, sym_pos=False, lower=False, overwrite_a=False, overwrite_b=False, debug=None, check_finite=True, assume_a="sym", transposed=False)#caso4
        #mul=solve(a,b, sym_pos=False, lower=False, overwrite_a=True, overwrite_b=False, debug=None, check_finite=True, assume_a='gen', transposed=False)#Caso5
        #mul=solve(a,b, sym_pos=False, lower=False, overwrite_a=False, overwrite_b=True, debug=None, check_finite=True, assume_a='gen', transposed=False)#caso6
        #mul=solve(a,b, sym_pos=False, lower=False, overwrite_a=True, overwrite_b=True, debug=None, check_finite=True, assume_a='gen', transposed=False)#caso7

        #mu=eigh(a, b=None, lower=True, eigvals_only=False, overwrite_a=False, overwrite_b=False, turbo=True, eigvals=None, type=1, check_finite=True, subset_by_index=None, subset_by_value=None, driver=None) 
        #mu=eigh(a, b=None, lower=True, eigvals_only=False, overwrite_a=False, overwrite_b=False, turbo=True, eigvals=None, type=1, check_finite=True, subset_by_index=None, subset_by_value=None, driver=None) 
        mu=eigh(a, b=None, lower=True, eigvals_only=False, overwrite_a=False, overwrite_b=True, turbo=True, eigvals=None, type=1, check_finite=True, subset_by_index=None, subset_by_value=None, driver="evx") 

        t3 = perf_counter()
        
        dt_ensamblaje = t2-t1
        
        dt_inversion = t3-t2
        
        bytes_total= a.nbytes + am1.nbytes
        
        #print(f"Uso memoria:{bytes_total}s ")
        
       # print(f"Tiempo ensamblaje: {dt_ensamblaje}s")
        
        #print(f"Tiempo inversion: {dt_inversion}s")

         
         
        UsoMemoriaTeorico=4*N*N
        UsoMemoriaNumpy=a.nbytes
          
         
        UsoMemoriaTotal=bytes_total
             
        
        dt = dt_inversion
        ListDts.append(dt)
        ListUsoMemoria.append(UsoMemoriaTotal)
        # print( UsoMemoriaTotal)
        print(f"Tiempo transcurrido ={dt} s")
        #print(f"N={N} dt={dt} s men= (UsoMemoriaTotal) bytes")
        fid.write(f"{N} {dt} {UsoMemoriaTotal}\n")
     
    
     
            
fid.close()
