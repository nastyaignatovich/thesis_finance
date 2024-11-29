import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

with open('data.pkl', 'rb') as f:
    data = pickle.load(f)

dependant_var = ['10. How would you rate your financial literacy?',
                 '11. How confident are you in your investment decisions?',
                 '12. How would you rate your risk tolerance?',
                 '18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?',
                 '19. What percentage of your entire assets (real estate, financial assets including cryptocurrency and other instruments, and other assets) is invested in assets outside your home country? ']

X = data.drop(dependant_var, axis=1)
Y = data['10. How would you rate your financial literacy?']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = LinearRegression()

model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(Y_test, y_pred)
print('Mean Squared Error',mse)

