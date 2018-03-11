import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

win5_df = pd.read_csv("data/win5.csv")

X_data = win5_df['odds'].values.reshape(-1,1)
y_data = win5_df['ratio'].values.reshape(-1,1)

lr = LinearRegression().fit(X_data, y_data)

plt.figure(figsize=(8, 6))

plt.plot(X_data, y_data, "o")

plt.title('Win5 Odds Prediction')
plt.xlabel('オッズ')
plt.ylabel('残割合')
plt.grid(True)
plt.ylim(-0.05,)
plt.xlim(-10,)

plt.show()

