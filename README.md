Entrega 5:

El codigo de ensamblaje que se utilizo para lograr la matriz laplaciana fue el siguiente:

def laplaciana(N,dtype):
    A = zeros((N,N),dtype=dtype)
    
    for i in range(N):
        A[i,i]=2
      
        for j in range(max(0,i-2),i):
            if abs(i-j)==1:
                   A[i,i]=-1
                   A[j,i]=-1               
    return A

El cual fue el escogido debido a que por un motivo quizas de actualizaciones de librerias o algo que no logre entender era el unico que me funcionaba para poder lograr tanto la matriz llena como la dispersa, otros codigos me funcionaban en una matriz pero en la otra no asi que para temas practicos de comparacion utilice esta para ver las reales diferencias que existen entre estas dos matrices y asi ver el tiempo de ejecucion de cada una de estas.

A continuación se mostraran los graficos obtenidos para el rendimiento de MATMUL tanto para matrices dispersas como llenas 

Matriz llena:


![image](https://user-images.githubusercontent.com/62267612/131164424-3266ed58-97f9-4dbd-8ebc-a5b2b8747f21.png)

Matriz dispersa:


![image](https://user-images.githubusercontent.com/62267612/131164461-4700d7fc-eb4a-4b42-b4e8-6ce9dd92fb5a.png)


A raiz de los resultados obtenidos se puede apreciar que con las matrices dispersas ahorramos mucha eficiencia debido a que esta no considera los valores de 0 lo cual hace que el tiempo de resolucion de la multiplicacion sea mucho mas optimizada y por ende mucho mas rapida a diferencia de lo que ocurre con la matriz llena la cual considera los valores de ceros y lo cual hace que el tiempo de resolución del problema sea mucho pero mucho mas alto.
Debido a lo mencionado anteriormente podemos ver que por un lado el tiempo con las matrices dispersas es considerablemente mas bajo por lo cual nos da margen para poder aumentar el Tamaño del N de las matrices que creamos lo cual fue logrado pero solamente hasta cierto punto debido a que despues de un cierto N (N=30.000 en mi caso) el problema no es con el tiempo de ejecucion sino con la memoria que llega al limite en mi computador debido a que se esta trabajando con matrices demasiado elevadas, a continuacion adjuntare una foto del error por memoria y la capacidad a la cual llega el computador.

![image](https://user-images.githubusercontent.com/62267612/131166339-1788ac36-f97d-463f-a7bd-05e15645e778.png)











Entrega 4

Comentario: La variabilidad del tiempo es bastante similar entre procedimientos con el mismo método de ejecución, el cual cambia considerablemente cuando pasamos de ocupar solve a o utilizar eight debido a que con este ultimo al momento de utilizar una matriz grande (N=10000) toma un tiempo considerablemente mayor al que se logra resolviéndolo con la línea de comando SOlVE.

Con respecto al algoritmo que gana en promedio se puede decir que es mucho más eficiente la línea de comando SOLVE debido a que esta para el máximo tamaño que se utilizo de matriz (N=10000) toma un tiempo promedio de ejecución que ronda entre los 20 a 30 segundos, lo cual se aleja mucho de los tiempos dados para este mismo tamaño de matriz para la línea de comando eight ya que esta misma para los mismos tamaños de matriz utilizados esta rondando en un tiempo promedio entre 105 y 120 segundos.

El tiempo que se demora la ejecución se puede apreciar que dependerá del tamaño de la matriz que se quiera ejecutar , entre mas grande la matriz mas tiempo se demorara y como se puede apreciar en los gráficos esta razón no es lineal y después del tamaño de matriz 5000 cualquier proceso independiente del método que se utilice se demorara mucho mas que si se calcularan matrices de tamaño 500 hacia abajo.

Con respecto a esta superioridad se debe a que el computador utiliza mejor el proceso de la línea de comando solve a eight pudiendo utilizar todos los procesadores de una forma mas optima y eficiente lo cual se refleja en los tiempos de ejecución. gráficos de rendimiento para cada caso: Casos float : A.I) image

gráficos de rendimiento para cada caso:
Casos float :


A.I)
![image](https://user-images.githubusercontent.com/62267612/130304763-c6c3f564-d955-47be-bce7-b40db0cd21f8.png)

  
A.II) 
![image](https://user-images.githubusercontent.com/62267612/130304764-207b99f7-cbf9-41c5-af0f-ceb97bfa1a8d.png)

 
A.III)
![image](https://user-images.githubusercontent.com/62267612/130304781-d8be126f-54af-42b8-b5af-175fc395a647.png)

 

A.IV)
![image](https://user-images.githubusercontent.com/62267612/130304787-4516da3e-4709-4b10-9156-1c0fe1a4f1f5.png)

 
A.V)
 
![image](https://user-images.githubusercontent.com/62267612/130304790-5bdfdba3-5a6d-4255-8ccd-3898d0ba9339.png)


A.VI)
![image](https://user-images.githubusercontent.com/62267612/130304794-0e82ae5b-3e8e-465b-be79-06ad46d6e30e.png)

  
A.Vii
![image](https://user-images.githubusercontent.com/62267612/130304797-44e6edea-ff65-4c9e-8502-d2f07eb553b1.png)

  
B.I) 
 ![image](https://user-images.githubusercontent.com/62267612/130304801-b1460c08-ef70-4a1a-a16f-8e5fd1d703ae.png)


B.II)
 ![image](https://user-images.githubusercontent.com/62267612/130304802-c0fcdb73-0eb6-4604-8bed-360d911e918d.png)


B.III)
![image](https://user-images.githubusercontent.com/62267612/130304807-6856398a-a071-4898-8e42-a03548c33ef0.png)

 
B.IV)
![image](https://user-images.githubusercontent.com/62267612/130304812-d936b8a0-eac1-4dbe-a380-76b450dae6d3.png)

 
B.V)
![image](https://user-images.githubusercontent.com/62267612/130304816-45b21225-f31c-4113-aafe-dcfbdbc7788c.png)


Casos double :
A.I)

![image](https://user-images.githubusercontent.com/62267612/130304821-14a07d80-28d1-49d2-9ab6-2833b0812361.png)

 
A.II)
 ![image](https://user-images.githubusercontent.com/62267612/130304826-f9bc0ebe-dd75-4062-a9da-720c75b8ee2b.png)


A.III)
![image](https://user-images.githubusercontent.com/62267612/130304829-e28b120f-1b73-4e05-b397-50464404c8f8.png)

 
A.IV)

![image](https://user-images.githubusercontent.com/62267612/130304836-c56ba428-4e90-4b53-bd60-2eb8539fd603.png)

  
A.V)
 
![image](https://user-images.githubusercontent.com/62267612/130304841-411960ff-54cf-48ad-950c-3faed0e86753.png)



A.VI)
![image](https://user-images.githubusercontent.com/62267612/130304844-2ff67f9d-5b61-4a07-811f-b36b506f3e15.png)

 

A.VII)
  ![image](https://user-images.githubusercontent.com/62267612/130304848-c7db6175-839f-4b0f-bc60-30bf6f83b646.png)

B.I)
 ![image](https://user-images.githubusercontent.com/62267612/130304852-f7cf64de-7028-4a33-b431-30813a806ba5.png)

B.II)
![image](https://user-images.githubusercontent.com/62267612/130304858-928f91ef-3e3c-477a-874b-9b14ce5bee01.png)

 
B.III)
![image](https://user-images.githubusercontent.com/62267612/130304864-d8fdf74d-f86e-492d-90f4-64f4c3e7f25d.png)

 
B.IV)
![image](https://user-images.githubusercontent.com/62267612/130304866-dcdaa54b-4019-4693-b7ac-c0e45b87c141.png)

  

B.V)
  
![image](https://user-images.githubusercontent.com/62267612/130304869-1635fee1-bced-41ce-885c-dc5b3bf5bf14.png)


2)Comparación promedio de 10 corridas para cada caso ( float-double)

I)Comparación promedio 10 corridas para float
![image](https://user-images.githubusercontent.com/62267612/130304874-7f28bdd0-dd81-46ab-ac15-dade63e5e612.png)


 


II)Comparación promedio 10 corridas para double

![image](https://user-images.githubusercontent.com/62267612/130304878-4dd8ce60-37d2-46c2-9886-b2cb334a89dd.png)

 


3)
Comparación de rendimientos promedio de desempeño de solve v/s eigh (para caso float y double)

I)Desempeño solve v/s eigh (float)
![image](https://user-images.githubusercontent.com/62267612/130304879-db673be8-9356-4257-a208-05b96ca3ea57.png)

 


II)Desempeño solve v/s eigh (double)
 
![image](https://user-images.githubusercontent.com/62267612/130304880-5cb880bb-d0c2-4bb6-aca3-a5d12e7fff59.png)


#Entrega 3

Memeoria y eficiencia cada caso :

Procedimiento con numpy.linalg 

caso 1 (half) :
 ![image](https://user-images.githubusercontent.com/62267612/129962945-e38c4d1e-2492-498d-a72b-f7ef10b3b2b7.png)




caso 2 (single ) :


![caso2](https://user-images.githubusercontent.com/62267612/129965084-346cf44d-f50a-40c0-b417-7679cd1a1164.png)


caso 3 (double ) :![caso3](https://user-images.githubusercontent.com/62267612/129965118-78171aca-6122-4d1f-b18b-9dec57bf7f25.png)


caso 4 (longdouble ) :
![image](https://user-images.githubusercontent.com/62267612/129963235-15a9e58d-7bc8-4545-9f03-5324da2d4c1b.png)

 

Procedimiento con scipy.linalg (overwrite_a=False)


caso 5 (half) :![caso5](https://user-images.githubusercontent.com/62267612/129965147-f1bbcac0-4751-4bc2-b10c-400bdc30da2b.png)


caso 6 (single ) :![caso6](https://user-images.githubusercontent.com/62267612/129965208-7bd8790e-b6f5-457e-ac98-490e308b5399.png)

caso 7 (double ) :![caso7](https://user-images.githubusercontent.com/62267612/129965224-2b0d8afd-9df1-40da-b804-cf7c8523a6b2.png)


caso 8 (longdouble):![caso8](https://user-images.githubusercontent.com/62267612/129965262-a78bc7d7-3303-427e-aa10-1d04c733d4ee.png)


Procedimiento con scipy.linalg (overwrite_a=True)


caso 9(half) :![caso9](https://user-images.githubusercontent.com/62267612/129965269-a8423fca-ee7d-448b-8293-48921c49de09.png)



caso 10 (single ) :![caso10](https://user-images.githubusercontent.com/62267612/129965280-b0a23cf6-ff48-4450-a206-7bcdd219ba3e.png)

caso 11 (double ) :![caso11](https://user-images.githubusercontent.com/62267612/129965287-57eb53f4-d33e-412c-bd99-0f3f46216150.png)


caso 12 (longdouble):![caso12](https://user-images.githubusercontent.com/62267612/129965339-e25240f0-9dd9-4463-8c50-da831753deb6.png)


PREGUNTAS:

¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta. 

#half 1 byte
#single 2 bytes
#double 4 bytes
#long double 8 bytes



¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso?

incide en el aspecto en que se ejecutara el programa, este implica que los procesadores funcionen simultaneamente al mismo tiempo lo que hace que resuelva varios calculos grandes de manera simultanea para que se acelere el proceso.

A continuacion se puede apreciar que al funcionar el programa con las 10 corridas seguidas el procesador esta funcionando al maximo de su capacidad y como se puede apreciar en la imagen esta realizando mas de 270 procesos los cuales los esta realizando mediante el paralelismo y capacidad del computador al mismo tiempo.

![image](https://user-images.githubusercontent.com/62267612/129967345-7b1a762b-4ae2-4f51-8bbf-1b3c3a005488.png)




#Entrega 2 (preguntas):




![Figure 2021-08-05 203342](https://user-images.githubusercontent.com/62267612/128441956-ece48267-172a-4725-89dc-667d455045b5.png)


¿Cómo difiere del gráfico del profesor/ayudante?

Difiere con respecto al inicio del procedimiento de python lo cual se puede dar debido a que mi procesador puede que sea de una velocidad mas baja por lo cual tiene menos procesadores para dedicarle a este proceso


¿A qué se pueden deber las diferencias en cada corrida?

a los distintos procesos que en si el computador esta haciendo entre si , pueden haber mil factores , desde el apretar una tecla , ocupar otras funciones o hasta incluso un correo o algun mensaje de alguna aplicación, depende de la cantidad de procesos que este ejecutando el computador en el instante en que ejecuta el programa.

El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?

debido a que el proceso que hace siempre tiene un punto de inicio y uno de fin , por ende siempre llegara donde mismo gastando la misma capacidad de memoria siempre , el tiempo varia dependiendo del camino que se tome y de los procesos que esta ejecutando la maquina.Se demorara mucho mas tiempo si se esta jugando por ejemplo a que si el compputador esta solo ejecutando la accion especifica.

¿Qué versión de python está usando?
3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]

¿Qué versión de numpy está usando?

1.20.1

Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 
si:
![image](https://user-images.githubusercontent.com/62267612/128537666-a5fbc2e1-2da6-43cb-a04b-6a200cde6cdc.png)










# MCOC2021-P0

# Mi computador principal

* Tipo: Notebook
* Año adquisición: 2020

System Information

------------------
      Time of this report: 8/5/2021, 20:43:13
             Machine name: LAPTOP-DKSFM6BM
               Machine Id: {4508A5A5-DD57-4464-9501-3D16CCCC1B7B}
         Operating System: Windows 10 Home 64-bit (10.0, Build 19043) (19041.vb_release.191206-1406)
                 Language: Spanish (Regional Setting: Spanish)
      System Manufacturer: HP
             System Model: OMEN Laptop 15-ek0xxx
                     BIOS: F.05 (type: UEFI)
                Processor: Intel(R) Core(TM) i5-10300H CPU @ 2.50GHz (8 CPUs), ~2.5GHz
                   Memory: 12288MB RAM
      Available OS Memory: 12128MB RAM
                Page File: 15005MB used, 12929MB available
              Windows Dir: C:\windows
          DirectX Version: DirectX 12
      DX Setup Parameters: Not found
         User DPI Setting: 120 DPI (125 percent)
       System DPI Setting: 96 DPI (100 percent)
          DWM DPI Scaling: Disabled
                 Miracast: Available, with HDCP
Microsoft Graphics Hybrid: Not Supported
 DirectX Database Version: 1.2.4
           DxDiag Version: 10.00.19041.0928 64bit Unicode







