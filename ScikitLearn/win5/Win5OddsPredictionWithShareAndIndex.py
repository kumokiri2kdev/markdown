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
lr = LinearRegression().fit(X_train, y_train)

print("intercept : {}".format(lr.intercept_))
print("coefficient : {}".format(lr.coef_[0]))
print("score : {}".format(lr.score(X_test, y_test)))

#plt.figure(figsize=(8, 6))

#plt.plot(X_data, y_data, "o")

#plt.title('Win5 Odds Prediction')
#plt.xlabel('支持率')
#plt.ylabel('残割合')
#plt.grid(True)
#plt.ylim(-0.05,)
#plt.xlim(-0.05, )

#plt.show()

