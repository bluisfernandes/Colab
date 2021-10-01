# -*- coding: utf-8 -*-
"""SBA31_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zqdt2Uy3f1iSRAgpoZUqzJP4ZAjWMJhG
"""

print("Python é divertido") # Este é um comentário
numeros = [1,2,3,4,5]
numeros

type(numeros)

variavel = 1.0
variavel

type(variavel)

nome = "Este é 'o' Python123456"
nome

nome[0:10:2]

type(nome)

"""**Palavras reservadas da linguagem Python**"""

help("keywords")

import keyword
keyword.kwlist

"""**Operações matemáticas básicas - Python como calculadora!**"""

# Adição
5 + 3

# Subtração
5 - 3

# Multiplicação
5 * 3

# Divisão
5 / 3

# Divisão sem resto (Floor)
5 // 3

# Módulo (resto da divisão)
5 % 3

# Potência
5 ** 3

# Número inteiro para flutuante
float(9)

# Número inteiro para flutuante
float(-9999)

# Número flutuante para inteiro
int(10.6)

# Caracteres representando números
int("2")

"""**Ops!! Como o Python reage a erros no Notebook**"""

# Caracteres representando números
int("2.3")

# Caracteres representando números 
float("2.3")

"""**Operadores Lógicos no Python**"""

2 > 5

2 < 5

3 >= 3

5 == 6

5 != 6

bool(0)

bool(1)

int(False)

int(True)

# Use aspas simples
saudacoes = 'Olá como vão? Tudo bem?'
saudacoes

# Use aspas duplas
bemvindo = "Bem-vindo ao Python!"
bemvindo

# Use aspas triplas
mensagem = """Obrigado por se tornar um 'Pythonista!'"""
mensagem

# Use aspas triplas
mensagem = "Obrigado por se tornar um 'Pythonista!'"
mensagem

# Concatenação
"Feliz "+"Pythoning!!"

# Comprimentos
len("Feliz")

# Comprimentos
len("Feliz "+"Pythoning!")

# Tudo Maiúscula
"Feliz Pythoning".upper()

# Tudo Minúscula
"Feliz Pythoning".lower()

# Formatação
nome = "Antonio Vidal"
idade = 63
print("Meu nome é {0} e eu tenho {1} anos".format(nome, idade))

# Ou você também pode utilizar f
f"Meu nome é {nome} e eu tenho {idade} anos."

# Ou você também pode utilizar f
f"Meu nome é {nome} e eu tenho {idade} anos."
1+2

bemvindo = "Bem-vindo ao Python"
bemvindo[0]

bemvindo[13]

bemvindo[-1]

bemvindo[0:3]

bemvindo[13:19]

bemvindo[0:11:2]

"""**Listas**"""

# Defina uma lista vazia
vazia = []
vazia

# Defina uma lista com números
numeros = [1,2,3,100]
numeros

# Modifique um determinado elemento da Lista
numeros[3] = 200
numeros

# Defina uma lista de strings
superherois = ["Batman", "Superhomem", "Homem Aranha"]
superherois

# Defina uma lista de objetos de tipos diferentes
lista_mista = ["Olá Python", [4,5,6], False]
lista_mista

numeros[2]

superherois[-1]

nova_lista = numeros[0:3]
nova_lista

lista_mista[1][2]

frutas = ["maçã","limão","laranja"]
vegetais = ["milho","cenoura","chuchu"]
lista_saudavel = frutas + vegetais
lista_saudavel

len(numeros)

frutas.append("melancia")
frutas

frutas.sort()
frutas

"""**Dicionários**"""

salario_dic = {'Pedro': 1000,'Carlos': 750,'Ricardo': 2000,'Letícia':2500}
salario_dic

salario_dic['Pedro']

salario_dic['Letícia']

len(salario_dic)

salario_dic

salario_dic.keys()



"""**Tuplas**"""

tupla1 = 'a','b','c','d','e'
tupla1

type(tupla1)

tupla2 = ('f','g','i','h')
tupla2

tupla2[0]

tupla2[0] = 'x'

empregados = {'João','Maria','Jose'}
empregados

type(empregados)

funcionarios = set(["David","Mark","Marie"])
funcionarios

type(funcionarios)

teste = {'teste','teste','teste'}
teste

teste2 = {'teste1','teste2','teste3'}
teste2

"""**Estruturas Condicionais**"""

idade = 21
if idade >= 18:
  print("Você já é considerado um adulto")

idade = 16
if idade >= 18:
  print("Você é já é considerado um adulto")
else:
  print("Você ainda não é considerado um adulto")

idade = 18
if idade > 18:
  print("Você tem mais de 18 anos")
elif idade == 18:
  print("Você tem exatamente 18 anos")
else:
  print("Você tem menos de 18 anos")

lista = [10, 77, 88, 32, 100]
for i in lista:
  print(i)

for i in range(10):
  print(i+1)

i = 0
while i < 10:
  print(i)
  i = i+1

"""**Funções**"""

def soma(a,b):
  return a+b

def subtracao(a,b):
  return a-b

def multiplicacao(a,b):
  return a*b

def divisao(a,b):
  if b != 0:
    return a/b
  else:
    return "Erro: não é possível dividir por zero!"

x = 10
y = 20
print('Soma de x com y:',soma(x,y))
print('Subtração de x com y:',subtracao(x,y))
print('Multiplicação de x por y:', multiplicacao(x,y))
print('Divisão de x por y:', divisao(x,y))

"""Funções Lambda"""

def duplica(x):
  resposta = x*2
  return(resposta)
duplica(2)

duplica(3)

def duplica2(x):
  return(x*2)
duplica2(6)

def duplica3(x): return(x*2)
duplica(5)

duplicaLambda = lambda x:x*2
duplicaLambda(8)

"""**Biblioteca PANDAS - Trabalhando com DataFrames**"""

import pandas as pd

data = {'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori', 'Tabajara'],
        'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka', 'Rio'], 
        'age': [41, 28, 33, 34, 38, 31, 37, 32], 
        'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0, 85.0]}
data

row_labels = [101, 102, 103, 104, 105, 106, 107, 108]
row_labels

df = pd.DataFrame(data=data, index=row_labels)
df

df.head(2)

df.tail(3)

df.city

cidades = df['city']
cidades

cidades[102]

df.loc[103]

df.index

df.columns[1]

df.dtypes

df.ndim

df.shape

df['name']

df.loc[101]

df.iloc[0]

df.loc[:,'py-score']

df.loc[:,'age']

Gisele = pd.Series(data=['Gisele','Brasília',54,79],index=df.columns, name=109)

df

df = df.append(Gisele)
df

import numpy as np
df['r-score'] = np.array([71.0,95.0,88.0,79.0,91.0,91.0,80.0,70.0,50.0])
df

df['total-score'] = 0.6*df['py-score']+0.4*df['r-score']
df

df.sort_values(by=['total-score','py-score'], ascending=[False,False])

selecao = df['total-score'] > 80
selecao

df[selecao]

import matplotlib.pyplot as plt
df.loc[:,['py-score','r-score']].plot.hist(bins=5,alpha=0.4)
plt.show()

df.loc[:,['py-score','r-score']].plot.line()
plt.show()