# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#importar librerias 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el dataset
dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, :1]

#dividir dataset en conjunto de entrenamiento y conjunto testing 

from sklearn.model_selection import train_test_split
X_train, x_test, y_train, y_test = train_test_split( x, y, test_size= 1/3, random_state = 0)


from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

y_pred = regression.predict(x_test)

plt.scatter(X_train, y_train, color = "#B755ED")
plt.plot(X_train, regression.predict(X_train), color = "#59F7B8")
plt.title("Sueldo vs Años de experiencia (Conjunto entrenamiento)")
plt.xlabel("Años y experiencia")
plt.ylabel("Sueldo en ($)")
plt.show()

plt.scatter(x_test, y_test, color = "#B755ED")
plt.plot(X_train, regression.predict(X_train), color = "#59F7B8")
plt.title("Sueldo vs Años de experiencia (Conjunto testing)")
plt.xlabel("Años y experiencia")
plt.ylabel("Sueldo en ($)")
plt.show()



