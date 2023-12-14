# -*- coding: utf-8 -*-
"""012T-SNE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/155LXqBmZgWANtsFeSfg7wbiOD6mm21Sn
"""

# Elaborado por:
# Ana Mantilla : anagmd2019@gmail.com

from sklearn.manifold import TSNE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/PAPER_DL/TRAINING/02_Train_PCA.csv', sep=';')

train

#Extraer las variables de entrada y de salida de la tabla

y_names=['DEP'] # Valores de salida-etiquetas de depósito (1) y no depósito (0)
y=train[y_names].values

x_names=['PC1','PC2','PC3','PC4','PC5','PC6','PC7','PC8','PC9']
X=train[x_names].values

X_embedded = TSNE(n_components=2, learning_rate='auto', init='random', perplexity=3).fit_transform(X)

X_embedded.shape

raster  = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/PAPER_DL/TRAINING/05_Random.csv')

raster

raster = raster.dropna()

raster.shape

R_embedded = TSNE(n_components=2, learning_rate='auto', init='random', perplexity=3).fit_transform(raster)

R_embedded.shape

plt.scatter(R_embedded[:,0], R_embedded[:,1], c = 'gray', alpha = 0.2)
plt.scatter(X_embedded[:,0], X_embedded[:,1], c = y)
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.colorbar()
plt.savefig('/content/drive/MyDrive/Colab Notebooks/PAPER_DL/FIGURAS/Imbalanced_data.svg')

"""# **Créditos**
---

* **Autores:**
  * [Ana Gabriela Mantilla, Geóloga](https://www.linkedin.com/in/ana-gabriela-mantilla-24377a21a)
"""