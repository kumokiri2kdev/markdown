# ndarray

## axis

- axis = 0 => 列方向
- axis = 1 => 行方向

![axis](img/np_01_01.jpg)


## ブロードキャスト
ブロードキャストは、計算を配列全てに適用する機能。

``` python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 1, 1], [2, 4, 1]])

b + a
```

```
array([[2, 3, 4],
       [3, 6, 4]])
```
