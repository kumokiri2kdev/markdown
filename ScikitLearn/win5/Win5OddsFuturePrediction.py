import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

win5_df = pd.read_csv("data/win5.csv")

X_data_odds = 0.788 / win5_df['odds'].values.reshape(-1,1)
X_data_index =  win5_df[['index', 'hcount']].values.reshape(-1,2)
X_data = np.c_[X_data_odds, X_data_index]
y_data = win5_df['ratio'].values


X_train, X_test, y_train,y_test = train_test_split(X_data, y_data)
lr = LinearRegression().fit(X_data, y_data)

new_remaining = 7069088

new_data_array= [
  [0.788 / 2.6, 1, 13],
  [0.788 / 26.6, 2, 12],
  [0.788 / 1.6, 3, 9],
  [0.788 / 22.3, 4, 18],
  [0.788 / 2.7, 5, 13],
]
print("intercept : {}".format(lr.intercept_))
print("coefficient : {}".format(lr.coef_[0]))

predicteds = lr.predict(new_data_array)
for predicted in predicteds:
  new_remaining = predicted * new_remaining
  print("remaining : {}, prediction : {} ".format(new_remaining, predicted))


