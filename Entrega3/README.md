Entrega 4

Comentario:
La variabilidad del tiempo es bastante similar entre procedimientos con el mismo método de ejecución, el cual cambia considerablemente cuando pasamos de ocupar solve a o utilizar eight debido a que con este ultimo al momento de utilizar una matriz grande (N=10000) toma un tiempo considerablemente mayor al que se logra resolviéndolo con la línea de comando SOlVE.
Con respecto al algoritmo que gana en promedio se puede decir que es mucho más eficiente la línea de comando SOLVE debido a que esta para el máximo tamaño que se utilizo de matriz (N=10000) toma un tiempo promedio de ejecución que ronda entre los 20 a 30 segundos, lo cual se aleja mucho de los tiempos dados para este mismo tamaño de matriz para la línea de comando eight ya que esta misma para los mismos tamaños de matriz utilizados esta rondando en un tiempo promedio entre 105 y 120 segundos.
El tiempo que se demora la ejecución se puede apreciar que dependerá del tamaño de la matriz que se quiera ejecutar , entre mas grande la matriz mas tiempo se demorara y como se puede apreciar en los gráficos esta razón no es lineal y después del tamaño de matriz 5000 cualquier proceso independiente del método que se utilice se demorara mucho mas que si se calcularan matrices de tamaño 500 hacia abajo
Con respecto a esta superioridad se debe a que el computador utiliza mejor el proceso de la línea de comando solve a eight pudiendo utilizar todos los procesadores de una forma mas optima y eficiente lo cual se refleja en los tiempos de ejecución.
gráficos de rendimiento para cada caso:
Casos float :
A.I)
![image](https://user-images.githubusercontent.com/62267612/130303489-0de95500-bebb-4398-9e20-fbab05a8bb98.png)

  
A.II) 
![image](https://user-images.githubusercontent.com/62267612/130303493-b952d728-4def-4ba4-8113-25029e0f973c.png)

 
A.III)
![image](https://user-images.githubusercontent.com/62267612/130303501-4183a631-2508-4f9f-9b63-2cbbaa7d1219.png)

 

A.IV)
![image](https://user-images.githubusercontent.com/62267612/130303504-3455eeee-e126-4a1b-9103-079b92a1d711.png)

 
A.V)
![image](https://user-images.githubusercontent.com/62267612/130303509-4b44d5bd-e017-4f14-b65a-2ab526c5a5ce.png)

 


A.VI)
![image](https://user-images.githubusercontent.com/62267612/130303513-45a9164a-8c5d-4427-98e2-e8540aadd85e.png)

  
A.Vii
![image](https://user-images.githubusercontent.com/62267612/130303518-06c9ad58-2530-4546-aadb-db9777e6ad46.png)

  
B.I) 
![image](https://user-images.githubusercontent.com/62267612/130303521-52bab012-be72-4d23-ba0b-8fc319bc4f10.png)

 

B.II)
![image](https://user-images.githubusercontent.com/62267612/130303524-0fbb4894-1f9a-4a18-be36-c0e6ff12ea47.png)

 

B.III)
 ![image](https://user-images.githubusercontent.com/62267612/130303530-31012ecf-ed3c-4529-976a-8c0de5548c62.png)

B.IV)
![image](https://user-images.githubusercontent.com/62267612/130303534-7a0471fc-90fc-42d3-be6b-7f2242948f6f.png)

B.V)
![image](https://user-images.githubusercontent.com/62267612/130303544-1c7bec5b-a071-4338-992c-e0c428456c76.png)

 
Casos double :
A.I)
![image](https://user-images.githubusercontent.com/62267612/130303554-3c8ae0cc-746b-4d78-a447-0e5bd434e4c8.png)

 
A.II)
![image](https://user-images.githubusercontent.com/62267612/130303558-cca55a29-1e46-4905-8283-6a1623fc5dc6.png)

 

A.III)
![image](https://user-images.githubusercontent.com/62267612/130303560-3be8f98d-c43d-4a8a-905e-809d08f7f7d5.png)

 
A.IV)
  ![image](https://user-images.githubusercontent.com/62267612/130303568-8921182c-4fbb-47e0-b8d5-f8af362f5267.png)

A.V)
 
![image](https://user-images.githubusercontent.com/62267612/130303570-95a834d2-6f53-4aef-b6cc-116db7a15bc4.png)



A.VI)
 
![image](https://user-images.githubusercontent.com/62267612/130303575-13dc6a2b-cde8-4169-951c-2037d4078c01.png)

A.VII)
![image](https://user-images.githubusercontent.com/62267612/130303585-029c2d0a-ac39-4248-b1ea-f7ac6499e03a.png)

  
B.I)
![image](https://user-images.githubusercontent.com/62267612/130303592-7ab90de6-0c05-4778-8d1e-91cfc30978b0.png)

 
B.II)
![image](https://user-images.githubusercontent.com/62267612/130303594-34fe1974-0ccc-4b11-b423-ff2b56fdcff4.png)

 
B.III)
![image](https://user-images.githubusercontent.com/62267612/130303600-b426942f-d143-4019-a15c-455341b2720f.png)

 
B.IV)
  ![image](https://user-images.githubusercontent.com/62267612/130303604-78e322dd-206b-46f1-943b-9ecf8a3b359e.png)

B.V)


2)Comparación promedio de 10 corridas para cada caso ( float-double)

I)Comparación promedio 10 corridas para float

 

II)Comparación promedio 10 corridas para double

![image](https://user-images.githubusercontent.com/62267612/130303619-283002a1-22dd-470b-8527-6911b063bc49.png)

 


3)
Comparación de rendimientos promedio de desempeño de solve v/s eigh (para caso float y double)

I)Desempeño solve v/s eigh (float)
![image](https://user-images.githubusercontent.com/62267612/130303650-c5d9aef5-75bf-4ebc-8e48-0035d9255ebb.png)

 

I)Desempeño solve v/s eigh (double)
 


![image](https://user-images.githubusercontent.com/62267612/130303652-00556b49-1dab-4187-bcdd-3e98db88b99c.png)


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







