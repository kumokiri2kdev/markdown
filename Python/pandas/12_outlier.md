#外れ値
## zスコア
``` Python
height = [178,190,187,179,192,186,188,1.81,187,177,190,181,178,180,171]
ser = pd.Series(height)
```

```
0     178.00
1     190.00
2     187.00
3     179.00
4     192.00
5     186.00
6     188.00
7       1.81
8     187.00
9     177.00
10    190.00
11    181.00
12    178.00
13    180.00
14    171.00
dtype: float64
```
このデータの zスコアを算出
``` Python
(ser - ser.mean())/ser.std(ddof=0)
```
```
0     0.152318
1     0.415464
2     0.349677
3     0.174247
4     0.459321
5     0.327748
6     0.371606
7    -3.711324
8     0.349677
9     0.130389
10    0.415464
11    0.218104
12    0.152318
13    0.196175
14   -0.001184
dtype: float64
```
一般的に、Zスコアが ± 3 より大きい場合に外れ値として取り扱う。

外れ値を取り除くには、下記の様にする。

``` Python
zscore = (ser - ser.mean())/ser.std(ddof=0)
ser = ser[(zscore >= -3) & (zscore <= 3)]
```
```
0     178.0
1     190.0
2     187.0
3     179.0
4     192.0
5     186.0
6     188.0
8     187.0
9     177.0
10    190.0
11    181.0
12    178.0
13    180.0
14    171.0
dtype: float64
```