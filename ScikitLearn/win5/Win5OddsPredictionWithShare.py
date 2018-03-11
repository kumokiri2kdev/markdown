import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

win5_df = pd.read_csv("data/win5.csv")

X_data = 0.788 / win5_df['odds'].values.reshape(-1,1)
y_data = win5_df['ratio'].values.reshape(-1,1)

lr = LinearRegression().fit(X_data, y_data)

print("intercept : {}".format(lr.intercept_))
print("coefficient : {}".format(lr.coef_[0]))

NewX_data = 0.788 / np.arange(1.1, 50.0, 0.1).reshape(-1,1)
Newy_data = lr.predict(NewX_data)

plt.figure(figsize=(8, 6))

plt.plot(X_data, y_data, "o")
plt.plot(NewX_data, Newy_data)

plt.title('Win5 Odds Prediction')
plt.xlabel('支持率')
plt.ylabel('残割合')
plt.grid(True)
plt.ylim(-0.05,)
plt.xlim(-0.05, )

plt.show()

