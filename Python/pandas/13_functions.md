# 関数処理

## apply メソッド



### ユーザー定義関数の使用

``` python
def test(a):
    return a.sum()

df = pd.DataFrame(np.arange(12).reshape(3,-1))

df['sum'] = df.apply(test, axis=1)  
```

```
   0  1   2   3  sum
0  0  1   2   3    6
1  4  5   6   7   22
2  8  9  10  11   38
```

### lambda 関数の使用

``` Python
df = pd.DataFrame(np.arange(12).reshape(3,-1))
df['sum'] = df.apply(lambda x: x.sum(), axis=1)   
```

```
   0  1   2   3  sum
0  0  1   2   3    6
1  4  5   6   7   22
2  8  9  10  11   38
```

## for 文によるループ

### Series のループ処理

``` python
ser = pd.Series([0, 1, 2, 3, 4], index=list('abcde'))

for val in ser:
  print(val)
```

```
0
1
2
3
4
```

インデックスと要素を同時に取り出す場合は、 iteritems を使用する。

``` python
for idx, val in ser.iteritems():
  print(idx, val)
```

```
a 0
b 1
c 2
d 3
e 4
```

### Data Frame のループ処理
データフレームに対して単純にループ処理をすると、カラムのみが取り出される。

``` python
val = [[81, 79], [91, 90]]
df = pd.DataFrame(val, columns=['math', 'eng'])

for col in df:
  print(col)
```
```
math
eng
```

行毎にループさせるには、 iterrows を使用する。

``` python
for idx, val in df.iterrows():
  print(idx)
  print(val)
```
```
0
math    81
eng     79
Name: 0, dtype: int64
1
math    91
eng     90
Name: 1, dtype: int64
```
itterrows は、行をシリーズで返す。
各行の元のデータ型は保持されない。

itertuples を使用すると、との値を保ったまま、tuple で返す。
``` python
for row in df.itertuples():
  print(row)
  print(row[1])
```
```
Pandas(Index=0, math=81, eng=79)
81
Pandas(Index=1, math=91, eng=90)
91
```
```index=False``` を指定すると、インデックスが削除される。
