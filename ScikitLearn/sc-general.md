# scikit-learn general

## 学習結果のセーブ・ロード

``` python
from sklearn.externals import joblib

# lr is learned model

# Save
joblib.dump(lr, 'lr.pkl')

# Load
lr = joblib.load('lr.pkl') 
```
