# データのソート

## ラベルによるソート

### シリーズのソート
``` Python
ser = pd.Series([5,1,0,9,3],index=list('acdbe'))
ser.sort_index()
```
```
a    5
b    9
c    1
d    0
e    3
dtype: int64
```

ascending 引数により、降順・昇順を切り替えられる。
``` Python
ser = pd.Series([5,1,0,9,3],index=list('いおあうえ'))
ser.sort_index(ascending=False)
```

```
お    1
え    3
う    9
い    5
あ    0
dtype: int64
```

### データフレームのソート

``` Python
np.random.seed(seed=1)
val = np.random.randint(0,10,size=9,).reshape(3,-1)
df = pd.DataFrame(val, index=[2,0,1],columns=list('cba'))
```
```
   c  b  a
2  5  8  9
0  5  0  0
1  1  7  6
```
axis = 0 で列方向でソート
``` Python
df.sort_index(axis=0)

```
```
   c  b  a
0  5  0  0
1  1  7  6
2  5  8  9
```
axis = 1 で行方向でソート

``` python
df.sort_index(axis=1)  
```
```
   a  b  c
2  9  8  5
0  0  0  5
1  6  7  1
```
NaN は、ソート時に最後に持ってこられるが、na_position を指定することで変更可能。


## 要素によるソート

### シリーズのソート
``` Python
ser = pd.Series([4,1,0,3,2])
ser.sort_values()
```
```
2    0
1    1
4    2
3    3
0    4
dtype: int64
```
ascending 引数により、降順・昇順を切り替えられる。

### データフレームのソート
``` Python
np.random.seed(seed=10)
scores = np.random.randint(70,100,size=20,).reshape(5,-1)
df = pd.DataFrame(scores, columns=['math','eng','chem','phys'])
```

```
math  eng  chem  phys
0    95   88    90    75
1    88   90    81    98
2    80   98    99    84
3    88   74    93    93
4    79   87    93    70
```

``` Python
df.sort_values(by='math')
```
```
   math  eng  chem  phys
4    79   87    93    70
2    80   98    99    84
1    88   90    81    98
3    88   74    93    93
0    95   88    90    75
```
``` Python
df.sort_values(by=['math','eng'])
```
```
   math  eng  chem  phys
4    79   87    93    70
2    80   98    99    84
3    88   74    93    93
1    88   90    81    98
0    95   88    90    75
```

### 最大・最小
#### シリーズの最大・最小を取得
``` python
df['eng'].nlargest(3)
df['eng'].nsmallest(3)
```

```
2    98
1    90
0    88
Name: eng, dtype: int64

3    74
4    87
0    88
Name: eng, dtype: int64
```
#### データフレームのの最大・最小を取得
``` Python
df.nlargest(3, 'eng')
df.nsmallest(3, 'eng')
```
```
   math  eng  chem  phys
2    80   98    99    84
1    88   90    81    98
0    95   88    90    75

   math  eng  chem  phys
3    88   74    93    93
4    79   87    93    70
0    95   88    90    75
```

## 並べ替え
ソートではなく、任意の順番に並べ替えたい場合。

### カラムを指定しての並べ替え
メソッドでは無いが、下記で代用できる。

``` Python
df = pd.DataFrame(np.arange(9).reshape(3,-1), columns=list('abc'))

df = df[['b','c','a']]
```

```
   a  b  c
0  0  1  2
1  3  4  5
2  6  7  8

   b  c  a
0  1  2  0
1  4  5  3
2  7  8  6
```
