# -*- coding: utf-8 -*-
"""Codificacion Huffman

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WS6gcuCifup4cwkPvfcv6xyL32kITlkw
"""

pip install binarytree --upgrade

class ExtendedNode:

    def __init__(self,value=None,probability=None, left=None, right=None):
        self.value=value
        self.probability=probability
        self.left = left    # Left child
        self.right = right  # Right child

import pandas as pd
from binarytree import Node
import numpy as np


df=pd.read_csv('./Alfabeto_Probabilidades.csv') # Se importa la tabla de probabilidad
df.sort_values(["Probability"],axis=0, ascending=False,inplace=True,na_position='first') #Se ordena descendentemente basandose en la probabilidad
df["code"]="" #Se agrega una nueva columna al documento CSV llamada "code"
df.iat[0,2]="1" #Se agrega el valor de "1" en la posicion 0,2 de la tabla
rowsNumber=len(df.index) #Se obtiene el numero de caracteres del alfabeto a usar en la compresion
originalNodes=[]
Alfabeto=np.zeros(25)
for i in range(rowsNumber):
  character=df.iloc[i,0]
  valorHoja=str(df.iloc[i,1])+character
  originalNodes.append(Node(valorHoja))
  #Llenado hash Alfabeto
  index=ord(character)-65
  Alfabeto[index]=i

lastValue=(originalNodes[len(originalNodes-1)].value)[]
penultimateValue=(originalNodes[len(originalNodes-2)].value)[]
lastCharacter=lastValue[len(lastCharacter)-1:len(lastCharacter)-1]
penultimateCharacter=penultimateValue[len(lastCharacter)-1:len(lastCharacter)-1]

while len(finalNodes)!=1:
  #Asignar valores nodo raiz arbol binario original
  lastNodeValue=finalNodes[len(finalNodes)-1].value
  penultimateNodeValue=finalNodes[len(finalNodes)-2].value
  raiz=Node(lastNodeValue+penultimateNodeValue)

  #Asignar valores nodo raiz arbol binario personalizado

  raiz.right=finalNodes[len(finalNodes)-1]
  raiz.left=finalNodes[len(finalNodes)-2]

  finalNodes[len(finalNodes)-2]=raiz
  finalNodes.pop()
  finalNodes.sort(key=lambda x: x.value,reverse=True)
print(originalNodes[0])
df.head()