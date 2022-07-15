import math
import numpy
from array import array

import pandas as pd
import matplotlib.pyplot as plt

def alaka(num):
    h=1
    while 1==1:
        if 2**h>=num:
            break
        else:
            h+=1
    return h

i=1
xd=[]
contador=0
suma=0
sumais=0
print("Para parar de añadir numeros presiona Q")

while 1==1:
    x=(input("Ingresa el valor " + str(i) +" "))
    if x=='q':
        break
    else:
        xd.append(int(x))
    i+=1
a =max(xd)-min(xd)
b =(1 + 3.322 * math.log(len(xd),10))
iC = round(a/b)
k = int(alaka(len(xd)))
inter=[]
mini = min(xd)
mini2 = min(xd)
listNums=[]
frecuencia=[]
puntoMedio=[]
freRel=[]
freAcum=[]
efeEquis=[]
cuadrado=[]
#print("el intervalo de clases es: " + str(iC) + " y k: " + str(k))

for i in range(k):
    inter.append(str(mini) + '-' + str(mini+iC))
    mini +=iC
    mini+=1
print(inter)

for i in range(k):
    listNums.append([])

for i in range(k):
    for j in range(iC+1):
        listNums[i].append(mini2)

        mini2+=1


for i in range(len(listNums)):
    for nume in xd:
        if nume in listNums[i]:
            contador+=1
    listNums[i].append(contador)
    contador=0
for i in range(k):
    frecuencia.append(listNums[i][-1])

for i in range(k):
    puntoMedio.append((listNums[i][0]+listNums[i][-2])/2)

for i in range(k):
    freRel.append(listNums[i][-1]/len(xd))

for i in range(k):
    suma = suma + listNums[i][-1]
    freAcum.append(suma)

for i in range(k):
    efeEquis.append(puntoMedio[i]*frecuencia[i])

for i in range(k):
    cuadrado.append(puntoMedio[i]*puntoMedio[i])


temporal = pd.DataFrame({'Intervalo': inter, 'Frecuencia' : frecuencia, 'Punto medio' : puntoMedio,
                         'Frecuencia relativa' : freRel, 'Frecuencia Acumulada' : freAcum,
                         'X*F' : efeEquis, 'X cuadrada' : cuadrado})

print(temporal)
for i in efeEquis:
    sumais+=i
media = sumais/len(xd)
equisde=pd.DataFrame({'Datos':xd})

indice=frecuencia.index(max(frecuencia))
mediana = listNums[indice][0]+(((len(xd))/(2)-freAcum[indice-1])/(frecuencia[indice]))*(listNums[indice][-2]-listNums[indice][0])

moda1 =listNums[indice][0]
print(moda1)
moda2 =((frecuencia[indice]-frecuencia[indice-1])/((frecuencia[indice]-frecuencia[indice-1])+(frecuencia[indice]-frecuencia[indice+1])))
print(moda2)
moda3 =(listNums[indice][-2]-listNums[indice][0])
print(moda3)

moda =moda1+moda2*moda3

print("LI: "+ str(listNums[indice][0]))
print("La media es:     " + str(media) + " La mediana es: " + str(mediana) +
      " La moda es : " + str(moda))
input()