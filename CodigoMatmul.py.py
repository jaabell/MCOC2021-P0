from scipy import matmul, rand 
from time import perf_counter 
from numpy import zeros, float16, float32, float64
import matplotlib.pylab as plt 


ListNs=[10]
ListDts=[]
ListUsoMemoria=[]

fid = open("rendimeiento.txt","w")

a=1

while a<=len(ListNs):
    print(a)
    a+=1
    
    for N in ListNs:    
     
         A = zeros((N,N),dtype=float32 )+1
         B = zeros((N,N),dtype=float32 )+2
         
         
         UsoMemoriaTeorico=4*N*N
         UsoMemoriaNumpy=A.nbytes
          
         
         t1 = perf_counter()
         
         C = A@B
         
         t2 = perf_counter()
             
         UsoMemoriaTotal=A.nbytes + B.nbytes + C.nbytes     
         dt = t2 - t1
         ListDts.append(dt)
         ListUsoMemoria.append(UsoMemoriaTotal)
        # print( UsoMemoriaTotal)
         print(f"Tiempo transcurrido ={dt} s")
         #print(f"N={N} dt={dt} s men= (UsoMemoriaTotal) bytes")
         fid.write(f"{N} {dt} {UsoMemoriaTotal}\n")
     
    
     
            
fid.close()
#plt.figure(1)
#plt.subplot(2,1,1)
#plt.plot(ListNs,ListDts)
#plt.subplot(2,1,1)
#plt.plot(ListNs,ListUsoMemoria)
#plt.show()