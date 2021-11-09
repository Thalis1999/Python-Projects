# CLASSIFICAÇÃO E REGRESSAO
# AQUISIÇÃO DE DADOS
#!pip install sklearn
from sklearn import datasets

iris = datasets.load_iris()
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
help(datasets.load_iris)
# PRÉ-PROCESSAMENTO (PREPROCESSING) / ANÁLISE EXPLORATÓRIA
iris.feature_names
# DADOS QUE TEMOS
iris.data
# O QUE DEVEMOS PREVER? SEMPRE SEPARAR OS DADOS DAS RESPOSTAS!
iris.target

#Dados do mundo real?
import pandas as pd

dataset = pd.read_csv('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')
dataset.head()

# DATAVIZ
from matplotlib import pyplot as plt

# Índices das nossas features x/y
x_index = 0 
y_index = 1

# Barra colorida de acordo com a target
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

# Preparamos infos sobre o gráfico
plt.figure(figsize=(10, 6)) # tamanho da figura
plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target) # tipo de gráfico
plt.colorbar(ticks=[0, 1, 2], format=formatter) # cores
plt.xlabel(iris.feature_names[x_index]) # eixo X (horizontal)
plt.ylabel(iris.feature_names[y_index]) # eixo Y (vertical)

# extraia insights/compartilhe com o mundo!
plt.tight_layout()
plt.show()
