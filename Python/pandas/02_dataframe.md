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

### empty データフレーム
``` Python
pd.DataFrame(None, columns=list('abc'))
```
データが全く無いデータフレームも作成可能。
ただし、group のあとの操作（mean()等）で問題が起こるので、使用しない方がいいかも。


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

### loc属性
loc 属性により、インデックス名やカラム名で参照可能。

``` Python
print(df.loc['a',:])
```

[出力]
```
c    1
d    2
e    3
Name: a, dtype: int64
```
１列もしくは、１列 だけを指定すると、シリーズになって出てくる。
複数列であれば、データフレームのまま。


列 + 行指定
```Python
print(df.loc['b','e'])
```
[出力]
```
6
```

### iloc属性
iloc により、名前ではなく順番で参照可能。
```Python
print(df[0:1])

print(df.iloc[0,:])

print(df.iloc[1, 2])
```
[出力]
```
   c  d  e
a  1  2  3

c    1
d    2
e    3

6
```

### データフレームの他の属性
```Python
print(df.shape)
print(df.size)
```

[出力]
```
(2, 3)
6
```

### 変更・追加
```Python
df = pd.DataFrame([[1, 2, 3],[4, 5, 6]]
df.iloc[1, 1] = 100

print(df)

df['new1'] = 10
df['new2'] = [5, 6]
```

[出力]
```
   0    1  2
0  1    2  3
1  4  100  6

   0    1  2  new1
0  1    2  3    10
1  4  100  6    10
```
### 追加した列に値を一括で代入
``` Python
df = pd.DataFrame(np.arange(9).reshape(3,-1), columns = list('abc'))
df['d'] = df['a'] + df['b']
```
```
   a  b  c
0  0  1  2
1  3  4  5
2  6  7  8


   a  b  c   d
0  0  1  2   1
1  3  4  5   7
2  6  7  8  13
```


### append による行の追加
```python
val = [i for i in range(7, 12)]
idx = [0, 1, 2, 'new1', 'new2']
series_add = pd.Series(val, index=idx, name='new3')
df = df.append(series_add)  

print(df)
```
[出力]
```
      0    1  2  new1  new2
0     1    2  3    10     5
1     4  100  6    10     6
new3  7    8  9    10    11
```

### 行の削除
行の削除は、drop メソッドを axis = 0 で指定する。
```Python
print(df.drop(labels='new3', axis=0))
# print(df.drop(labels=['new3'], axis=0)) でも同様

print(df.drop(labels=[1, 'new3'], axis=0))
```
[出力]
```
   0    1  2  new1  new2
0  1    2  3    10     5
1  4  100  6    10     6

   0  1  2  new1  new2
0  1  2  3    10     5
```
### 列の削除
列の削除は、drop メソッドを axis = 1 で指定する。

```Python
print(df.drop(labels=['new1', 'new2'], axis=1))
```
[出力]
```
      0    1  2
0     1    2  3
1     4  100  6
new3  7    8  9
```

### 重複値の削除

```Python
val = [[1,2,3],[4,5,6],[1,2,3],[3,5,6],[1,2,3]]
df = pd.DataFrame(val, columns=list('ABC'))

print(df[df.duplicated(keep='first') == False])

print(df.drop_duplicates(keep='first'))
```

[出力]
```
   A  B  C
0  1  2  3
1  4  5  6
3  3  5  6

   A  B  C
0  1  2  3
1  4  5  6
3  3  5  6
```

### 欠損値
isna と notna を使うことで、NaN であるかどうかのデータフレームを取り出せる。

``` Python
val = [[1,2,3],[4,5,np.nan],[1,np.nan,np.nan],[3,5,6],[7,8,9]]
df = pd.DataFrame(val, columns=list('ABC'))

print(df.isna)  

print(df.notna)

```
[出力]
```
   A    B    C
0  1  2.0  3.0
1  4  5.0  NaN
2  1  NaN  NaN
3  3  5.0  6.0
4  7  8.0  9.0

   A    B    C
0  1  2.0  3.0
1  4  5.0  NaN
2  1  NaN  NaN
3  3  5.0  6.0
4  7  8.0  9.0
```

dropna を使用することで、NaN をもつ行・列を削除することができる。

``` ptyhon
print(df.dropna(axis=0))

print(df.dropna(axis=1))
```

[出力]
```
   A    B    C
0  1  2.0  3.0
3  3  5.0  6.0
4  7  8.0  9.0

   A
0  1
1  4
2  1
3  3
4  7
```
