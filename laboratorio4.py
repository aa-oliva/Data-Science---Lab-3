# -*- coding: utf-8 -*-
"""Laboratorio4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10y7hG8K8mw-DCz4Ctei0Ll-fLThit78d

# Laboratorio 4

---
Se necesita tener acceso los archivos de google drive para poder usar este código, aqui esta el link de compartir: <br>[Google Drive](https://drive.google.com/drive/folders/1EGaVv-qekeA--pPsToN5DUZC868gv14k?usp=sharing) <br>

--- 
Tabla de contenido


*   Análisis Exploratorio
*   something else

## IMPORTACIONES
"""

import pandas as pd
import numpy as np
#import tensorflow as tf
#from google.colab import files
import matplotlib.pyplot as plt
import re
import io 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk import ngrams
#import heapq
#import operator
# Load library
from nltk.corpus import stopwords

# You will have to download the set of stop words the first time
import nltk
nltk.download('stopwords')



"""##Limpieza de datos (remover @,# y apostrofes)

- Revisar si hay emoticones y quitarlos
- Quitar los artículos, preposiciones y conjunciones (stopwords)
- Quitar números si considera que interferirán en las predicciones.
"""

# Prepociciones
prep = []
with open('prepositions.txt') as f:
  content = f.readlines()
  content = [x.strip() for x in content] 
  prep.extend(content)
print (prep)

# conjugaciones
conj = []
with open('conjunctions.txt') as f:
  content = f.readlines()
  content = [x.strip() for x in content] 
  conj.extend(content)
print (conj)

with open(r'en_US.news.txt', encoding="utf8") as infile, \
     open(r'news.txt', 'w') as outfile:
    data = infile.read()
    data = data.lower()
    # eliminar prep
    for word in prep:
      data = data.replace (" "+str(word)+" ", "")
    # eliminar conj
    for word in conj:
      data = data.replace(" "+str(word)+" ", "")
    # Eliminar simbolos
    data = re.sub("@", "", data)
    data = re.sub("#", "", data)
    data = re.sub('\"','', data)
    data = re.sub('\.','', data)
    data = re.sub(r'\bhttp\S+', '', data, re.IGNORECASE)
    # Eliminar Articulos
    data = data.replace(' a ', '')
    data = data.replace(" an ", "")
    data = data.replace(" the ", "")
    data = data.replace(" and ", "")
    data = data.replace("\n", "")

      
    outfile.write(data)
    print ("Success")

if 'http' in open('news.txt').read():
    print("true")

with open(r'en_US.blogs.txt', 'r') as infile, \
     open(r'blogs.txt', 'w') as outfile:
    data = infile.read()
    data = data.lower()
    # eliminar prep
    for word in prep:
      data = data.replace (" "+str(word)+" ", "")
    # eliminar conj
    for word in conj:
      data = data.replace(" "+str(word)+" ", "")
    # Eliminar simbolos
    data = re.sub("@", "", data)
    data = re.sub("#", "", data)
    data = re.sub('\"','', data)
    data = re.sub('\.','', data)
    data = re.sub(r'\bhttp\S+', '', data, re.IGNORECASE)
    # Eliminar Articulos
    data = data.replace(' a ', '')
    data = data.replace(" an ", "")
    data = data.replace(" the ", "")
    data = data.replace(" and ", "")
    data = data.replace("\n", "")

      
    outfile.write(data)
    print ("Success")

with open(r'en_US.twitter.txt', 'r') as infile, \
     open(r'twitter.txt', 'w') as outfile:
    data = infile.read()
    data = data.lower()
    # eliminar prep
    for word in prep:
      data = data.replace (" "+str(word)+" ", "")
    # eliminar conj
    for word in conj:
      data = data.replace(" "+str(word)+" ", "")
    # Eliminar simbolos
    data = re.sub("@", "", data)
    data = re.sub("#", "", data)
    data = re.sub('\"','', data)
    data = re.sub('\.','', data)
    data = re.sub(r'\bhttp\S+', '', data, re.IGNORECASE)
    # Eliminar Articulos
    data = data.replace(' a ', '')
    data = data.replace(" an ", "")
    data = data.replace(" the ", "")
    data = data.replace(" and ", "")
    data = data.replace("\n", "")

      
    outfile.write(data)
    print ("Success")


"""## Analisis

## Diccionario de Palabras
Aqui se ba a buscar hacer un contador de cuantas palabras únicas hay y cuantas veces se repite ciertas palabras
"""

palabrasNews = {}
palabrasBlog = {}
palabrasTwitter = {}

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

with open('news.txt', 'r') as infile:
  data = infile.read()
  palabrasNews = word_count(data)

with open('blogs.txt', 'r') as infile:
  data = infile.read()
  palabrasBlog = word_count(data)

with open('twitter.txt', 'r') as infile:
  data = infile.read()
  palabrasTwitter = word_count(data)

"""### Ordenar listado
Lo ordenamos para poder hacer busquedas mas rapidas y encontrar las palabras mas comunes
"""

"""##Histogramas

Se realizan histogramas para un mejor entendimiento

histNews = []
with open('news.txt') as f:
    [histNews.append(word for line in f for word in line.split())]
"""

plt.bar(palabrasNews.keys(), palabrasNews.values(), color='g')





"""##Nube de palabras"""


##N-Grams
"""



"""##Matrices de términos para cada palabra"""



"""## Probabilidad de ocurrencia de cada uno de los n-gramas"""



"""## Prediccion de 3 palabras siguientes"""

