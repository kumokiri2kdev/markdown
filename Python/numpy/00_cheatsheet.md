
１列を行に変換して取り出す
``` python
x[:, 0]
```
1 x n を n x 1 にして取り出す。
``` python
x[:, np.newaxis]
```

行方向に結合する。
``` python
np.concatenate([x, y], axis=1)
np.hstack([x, y])
```

列方向に結合する。
``` python
np.concatenate([x, y])
np.vstack([x, y])
```

分割
``` python
np.split(x, [3, 5])
```
