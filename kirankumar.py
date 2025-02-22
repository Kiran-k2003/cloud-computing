# -*- coding: utf-8 -*-
"""kirankumar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uWVF09IN5weOE2zPSqIltLroA_rx1Bvh
"""

import numpy as np
import sklearn
from sklearn import linear_model

# Data: heights and corresponding weights
height = [[4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0]]
weight = [8, 10, 12, 14, 16, 18, 20]

# Create a linear regression model
reg = linear_model.LinearRegression()

# Fit the model
reg.fit(height, weight)

# Predict the weight for a height of 12.0
X_height = [[12.0]]
print(reg.predict(X_height))  # Corrected line with closing parenthesis

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

# Input data
x = [[4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0]]
y = [16, 25, 36, 49, 64, 81, 100]

# Step 2 - Fitting Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# Step 4 - Linear Regression prediction
print("Linear Regression Prediction for x=11:", lin_reg.predict([[11]]))

# Step 5 - Polynomial Regression prediction (using a higher degree)
polynomial_regression = make_pipeline(
    PolynomialFeatures(degree=2, include_bias=False),  # Change degree for a true polynomial regression
    LinearRegression(),
)
polynomial_regression.fit(x, y)
X_height = [[20.0]]
target_predicted = polynomial_regression.predict(X_height)
print("Polynomial Regression Prediction for x=20:", target_predicted)