
from time import perf_counter 
from numpy import zeros, half, single , double , longdouble, eye 
import matplotlib.pylab as plt 


from laplaciana import laplaciana 
from scipy.linalg import inv 

ListNs=[10,20,50,100,200,500,1000,2000,5000,10000]
ListDts=[]
ListUsoMemoria=[]

fid = open("caso12.txt","w")

a=1

while a<=len(ListNs):
    print(a)
    a+=1
    
    for N in ListNs:    
     
        
        t1 = perf_counter()
            
        A=laplaciana(N,dtype=longdouble)
        t2 = perf_counter()
        #print(A)
        am1= inv(A, overwrite_a=True, check_finite=True)
        
        t3 = perf_counter()
        
        dt_ensamblaje = t2-t1
        
        dt_inversion = t3-t2
        
        bytes_total= A.nbytes + am1.nbytes
        
        #print(f"Uso memoria:{bytes_total}s ")
        
       # print(f"Tiempo ensamblaje: {dt_ensamblaje}s")
        
        #print(f"Tiempo inversion: {dt_inversion}s")

         
         
        UsoMemoriaTeorico=4*N*N
        UsoMemoriaNumpy=A.nbytes
          
         
        UsoMemoriaTotal=bytes_total
             
        
        dt = dt_inversion
        ListDts.append(dt)
        ListUsoMemoria.append(UsoMemoriaTotal)
        # print( UsoMemoriaTotal)
        print(f"Tiempo transcurrido ={dt} s")
        #print(f"N={N} dt={dt} s men= (UsoMemoriaTotal) bytes")
        fid.write(f"{N} {dt} {UsoMemoriaTotal}\n")
     
    
     
            
fid.close()