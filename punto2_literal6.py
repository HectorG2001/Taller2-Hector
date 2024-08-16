# -*- coding: utf-8 -*-
"""Punto2.Literal6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O8HYEIaVDj8UlBBGCP0VF565GRs5jqZM

# Analítica computacional para la toma de decisiones

Departamento de Ingeniería Industrial

Universidad de los Andes

## Exploración de datos en python

### Importar Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""### Importar Dataset"""

df = pd.read_csv("C:/Users/higut/Downloads/BikePrices.csv")

df.shape

df.head()

df["Brand"].unique()

df.groupby(["Brand"]).count()

df["Brand"].value_counts()

df.describe()

# número de clientes perdido y no perdidosn
counts = df.Brand.value_counts()
perc_churn = (counts.iloc[1] / (counts.iloc[0] + counts.iloc[1]+counts.iloc[3]+counts.iloc[4]+counts.iloc[5]+counts.iloc[6])) * 100
print(f'Churn Rate = {perc_churn:.1f}%')
pppppp
# número de duplicados
duplicates = len(df[df.duplicated()])
print(f'Number of Duplicate Entries: {duplicates}')

# número de valores perdidos
missing_values = df.isnull().sum().sum()
print(f'Number of Missing Values: {missing_values}')

# Tipos de datos en el dataset
types = df.dtypes.value_counts()

print('Number of Features: %d'%(df.shape[1]))
print('Number of Customers: %d'%(df.shape[0]))
print('Data Types and Frequency in Dataset:')
print(types)

"""## Pre-Processing"""

# Conversión de características
df['Brand'] = df['Brand'].map({'TVS': 1, 'Bajaj': 0, 'Yo':2, 'Honda':3, 'Mahindra':4, 'Hero':5, 'Suzuki':6, })

catcols = df.select_dtypes(exclude = ['int64','float64']).columns
intcols = df.select_dtypes(include = ['int64']).columns
floatcols = df.select_dtypes(include = ['float64']).columns

# codificación
df = pd.get_dummies(df, columns = catcols)

print('New Number of Features: %d'%(df.shape[2]))

plt.hist(df['Brand'])
plt.show
print("Punto uno literal 9")
print("liteal 7")