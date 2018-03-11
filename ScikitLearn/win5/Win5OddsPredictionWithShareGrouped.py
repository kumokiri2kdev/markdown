import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

win5_df = pd.read_csv("data/win5.csv")
X_pred = 0.788 / np.arange(1.1, 50.0, 0.1).reshape(-1,1)

plt.figure(figsize=(8, 6))

for i in range(1,6):
  grouped = win5_df.query("index=={}".format(i))
  X_data = 0.788 / grouped['odds'].values.reshape(-1,1)
  y_data = grouped['ratio'].values.reshape(-1,1)
  lr = LinearRegression().fit(X_data, y_data)
  print("[index {}] intercept : {}".format(i, lr.intercept_))
  print("[index {}] coefficient : {}".format(i, lr.coef_[0]))
  plt.plot(X_data, y_data, "o", label="index {}".format(i))
  y_pred = lr.predict(X_pred)
  plt.plot(X_pred, y_pred, label="index {} pred".format(i))

plt.title('Win5 Odds Prediction')
plt.xlabel('支持率')
plt.ylabel('残割合')
plt.grid(True)
plt.ylim(-0.05,)
plt.xlim(-0.05, )
plt.legend()

plt.show()

