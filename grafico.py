# -*- coding: utf-8 -*-
"""Grafico.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16-xgw-1bt638gDjMw-Ys1Sd9gHdiWcr6
"""

!pip install --upgrade pip setuptools wheel

!pip install matplotlib --prefer-binary

!pip freeze > requirements.txt

"""#Grafico 01

Grafico 1x1 1 linha e 1 coluna
"""

# passo 1 - importa a biblioteca
import matplotlib.pyplot as plt

#passo 2 - intanciar o objeto figura
fig, ax = plt.subplots() # 1x1

#passo 3 - Definir os dados
indices = [1,2,3,4]
amostra_a = [1,4,2,3]
amostra_b = [2,8,4,6]
amostra_c = [4,16,8,12]

#passo 4 - plotar os dados no axe/eixo(grafico)
ax.plot(indices, amostra_a, label="Amostra A", color = 'blue', marker = 'o')
ax.plot(indices, amostra_b, label="Amostra B", color = 'green', marker = 'o')
ax.plot(indices, amostra_c, label="Amostra C", color = 'red', marker = 'o')

# titulo do grafico
ax.set_title("Titúlo do Gráfico")

# titulo do x
ax.set_xlabel("Label X")

# titulo y
ax.set_ylabel("Label y")

# a legenda
ax.legend()

#passo 5 - apresentar o grafico
plt.show()

"""#Grafico 02

Grafico 1x2, 1 linha 2 coluna
"""

# passo 1 - importa a biblioteca
import matplotlib.pyplot as plt

#passo 2 - intanciar o objeto figura
fig, ax = plt.subplots(1, 2) # 1x2

#passo 3 - Definir os dados
indices = [1,2,3,4]
amostra_a = [1,4,2,3]
amostra_b = [2,8,4,6]

#passo 4 - plotar os dados no axe/eixo(grafico)
ax[0].plot(indices, amostra_a, label="Amostra A", color = 'blue', marker = 'o')
ax[1].plot(indices, amostra_b, label="Amostra B", color = 'green', marker = 'o')

# titulo do grafico
ax[0].set_title("Titúlo do Gráfico 0")
ax[1].set_title("Titúlo do Gráfico 1")

# titulo do x
ax[0].set_xlabel("Label X 0")
ax[1].set_xlabel("Label X 1")

# titulo y
ax[0].set_ylabel("Label y 0")
ax[1].set_ylabel("Label y 1")

# a legenda
ax[0].legend()
ax[1].legend()

#passo 5 - apresentar o grafico
plt.show()

"""#Grafico 03

Grafico 2x2, 2 linha 2 coluna
"""

# passo 1 - importa a biblioteca
import matplotlib.pyplot as plt

#passo 2 - intanciar o objeto figura
fig, ax = plt.subplots(2, 2) # 2x2

#passo 3 - Definir os dados
indices = [1,2,3,4]
amostra_a = [1,4,2,3]
amostra_b = [2,8,4,6]
amostra_c = [4,16,8,12]
amostra_d = [8,32,16,24]

#passo 4 - plotar os dados no axe/eixo(grafico)
ax[0][0].plot(indices, amostra_a, label="Amostra A", color = 'blue', marker = 'o')
ax[0][1].plot(indices, amostra_b, label="Amostra B", color = 'green', marker = 'o')
ax[1][0].plot(indices, amostra_c, label="Amostra C", color = 'red', marker = 'o')
ax[1][1].plot(indices, amostra_d, label="Amostra D", color = 'yellow', marker = 'o')

# titulo do grafico
ax[0][0].set_title("Titúlo do Gráfico 0x0")
ax[0][1].set_title("Titúlo do Gráfico 0x1")
ax[1][0].set_title("Titúlo do Gráfico 1x0")
ax[1][1].set_title("Titúlo do Gráfico 1x1")

# titulo do eixo x
ax[0][0].set_xlabel("Label X 0x0")
ax[0][1].set_xlabel("Label X 0x1")
ax[1][0].set_xlabel("Label X 1x0")
ax[1][1].set_xlabel("Label X 1x1")

#ax[1].set_xlabel("Label X 1")

# titulo do eixo y
ax[0][0].set_ylabel("Label y 0x0")
ax[0][1].set_ylabel("Label y 0x1")
ax[1][0].set_ylabel("Label y 1x0")
ax[1][1].set_ylabel("Label y 1x1")

# a legenda
ax[0][0].legend()
ax[0][1].legend()
ax[1][0].legend()
ax[1][1].legend()

#passo 5 - apresentar o grafico
plt.show()

"""Grafico de Barra"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

frutas = ['Laranja', 'Melancia', 'Manga', 'Jaca']
quantidades = [60, 100, 85, 30]

ax.bar(frutas, quantidades, label = 'Quantidade')
ax.set_xlabel('Frutas')
ax.legend()

plt.show()

"""Grafico de Histograma"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

pesquisa = np.random.normal(170, 10, 250) # 250 dados 10 disvio padrao e 170 valor mediano

ax.hist(pesquisa, bins = 8, linewidth = 0.5, edgecolor = '#ffffff')

plt.show()

"""Grafico de Pizza"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

frutas = ['Uva', 'Morango', 'Abacaxi', 'Mamão']
porcentagem = [15, 30, 45, 10]

ax.pie(porcentagem, labels = frutas, autopct = '%1.2f%%')

plt.show()

"""Salvando imagem do grafico"""

import matplotlib.pyplot as plt
from pathlib import Path

image_dir = Path.cwd() / 'images'

fig, ax = plt.subplots()

frutas = ['Uva', 'Morango', 'Abacaxi', 'Mamão']
porcentagem = [15, 30, 45, 10]

ax.pie(porcentagem, labels = frutas, autopct = '%1.2f%%')

fig.savefig(image_dir/'meu_grafico.png')

#plt.show()

import matplotlib.pyplot as plt
from pathlib import Path

#image_dir = Path.cwd() / 'images'

fig, ax = plt.subplots()

frutas = ['Uva', 'Morango', 'Abacaxi', 'Mamão']
porcentagem = [15, 30, 45, 10]

ax.pie(porcentagem, labels = frutas, autopct = '%1.2f%%')

#fig.savefig(image_dir/'meu_grafico.png')
fig.savefig('meu_grafico.png')


#plt.show()

import matplotlib.pyplot as plt
from pathlib import Path

#image_dir = Path.cwd() / 'images'

fig, ax = plt.subplots()

frutas = ['Uva', 'Morango', 'Abacaxi', 'Mamão']
porcentagem = [15, 30, 45, 10]

ax.pie(porcentagem, labels = frutas, autopct = '%1.2f%%')

#fig.savefig(image_dir/'meu_grafico.png')
fig.savefig('meu_grafico3.jpg', transparent = True, dpi = 150, bbox_inches = 'tight')