# DataFrame
データフレームは、二次元の構造を持つデータ。

横方向のカラム（列）と縦方向のインデックス（行）で構成される。

## 概要

### プリミティブなデータフレームの生成

``` python
val = ['a', 1, 0.5]

df = pd.DataFrame(val)

print(df)
```

[出力]
```
     0
0    a
1    1
2  0.5
```
この例の場合、１列のデータフレームなので、実質的に、シリーズと変わらない。

### ２次元配列からのデータフレームの生成と index, columns の付与

``` Python
val = np.arange(1, 7).reshape((2,-1))
df = pd.DataFrame(val, index=list('ab'), columns=list('cde'))

print(df)
```

[出力]
```
   c  d  e
a  1  2  3
b  4  5  6
```

### 行・列のサイズが異なる配列の場合には、 欠損値 (NaN)が代入される
``` python
df = pd.DataFrame([[1, 2, 3],[4, 5]])

print(df)
```
[出力]
```
   0  1    2
0  1  2  3.0
1  4  5  NaN
```
### ディクショナリからのデータフレーム生成
ディクショナリからデータフレームを生成すると、キーが column 名になる。

``` python
df = pd.DataFrame({'a':[1, 2, 3], 'b': [3, 4, 5]})

print(df)
```
[出力]
```
   a  b
0  1  3
1  2  4
2  3  5
```

### Series の値を持つ ディクショナリからデータフレームを生成

``` python
age = pd.Series([10, 12, 9], index=['A', 'B', 'C'])
sex = pd.Series(['M', 'F', 'F'], index=['C', 'A', 'D'])

print(df)
```

[出力]
```
    age  sex
A  10.0    F
B  12.0  NaN
C   9.0    M
D   NaN    F
```

### ネストされたディクショナリからデータフレームを生成
``` Python
nest_dict = {
  'age': {'A': 10, 'B': 12, 'C': 9},
  'sex': {'C': 'M', 'A': 'F', 'D': 'F'}
}

df = pd.DataFrame(nest_dict)

print(df)
```
[出力]
```
age  sex
A  10.0    F
B  12.0  NaN
C   9.0    M
D   NaN    F
```

### dtypes属性
dtypes 属性で、各カラムのデータ型を確認することができる。
``` Python
nest_dict = {
  'age': {'A': 10, 'B': 12, 'C': 9},
  'sex': {'C': 'M', 'A': 'F', 'D': 'F'}
}

print(df.dtypes)
```
[出力]
```
age    float64
sex     object
dtype: object
```

## データフレームのインデックス参照

### カラム名での取り出し
``` Python
df = pd.DataFrame({
  'math': [82, 93, 77],
  'eng': [77, 87, 71],
  'chem': [69, 91, 89]
})

print(df['math'])
print(type(df['math']))

print(df[['math','eng']])
print(type(df[['math','eng']]))

```
[出力]
```
0    82
1    93
2    77
Name: math, dtype: int64

<class 'pandas.core.series.Series'>

math  eng
0    82   77
1    93   87
2    77   71

<class 'pandas.core.frame.DataFrame'>
```
一列だけを取り出すと、シリーズになるが、複数だとデータフレームになる。

### 条件を満たすデータの取り出し

``` Python
print(df[df['math'] > 80])
```
[出力]
```
math  eng  chem
0    82   77    69
1    93   87    91
```

### インデックス・カラムの変更

``` Python
val = np.arange(1, 7).reshape((2,-1))
df = pd.DataFrame(val)

print(df)

df.index = list('ab')

print(df)

df.columns = list('cde')

print(df)

```
[出力]
```
   0  1  2
0  1  2  3
1  4  5  6

   0  1  2
a  1  2  3
b  4  5  6

c  d  e
a  1  2  3
b  4  5  6
```
