# 追加と削除

## 行と列の追加

### 拡張代入による列の追加

``` Python
df = pd.DataFrame([[1,2],[3,4]], columns=['a', 'b'])
print('<<初期状態>>')
print(df)

df['c'] = [1, 2]
print('<<追加 01>>')
print(df)

df['d'] = 3
print('<<追加 02>>')
print(df)

df.loc[:,'e'] = [5, 6]
print('<<追加 03>>')
print(df)

```

```
<<初期状態>>
a  b
0  1  2
1  3  4

<<追加 01>>
   a  b  c
0  1  2  1
1  3  4  2

<<追加 02>>
   a  b  c  d
0  1  2  1  3
1  3  4  2  3

<<追加 03>>
   a  b  c  d  e
0  1  2  1  3  5
1  3  4  2  3  6

```
iloc は拡張代入をサポートしていない。

### assign メソッドによる列の追加

``` Python
df.assign(f=[7, 8])
```
```
a  b  c  d  e  f
0  1  2  1  3  5  7
1  3  4  2  3  6  8
```
assign() は直接代入するのではなく、代入した data frame を返す。


## 行の追加
``` Python
df = pd.DataFrame([[1,2],[3,4]], columns=['a','b'])
df2 = pd.DataFrame([[5,6]], columns=list('ab'))

df.append(df2)
```
```
a  b
0  1  2
1  3  4
0  5  6
```
ignore_index を指定すると、インデックスを付け直す。

``` Python
df.append(df2, ignore_index=True)
```
```
a  b
0  1  2
1  3  4
2  5  6
```
## 列の削除
### del による削除
``` Python
val = np.arange(0,12).reshape(3,4)
df = pd.DataFrame(val, columns=list('abcd'))

del df['d']

```
```
   a  b   c
0  0  1   2
1  4  5   6
2  8  9  10
```

### drop による削除
``` Python
df.drop(labels='b', axis=1)
```
```
   a   c
0  0   2
1  4   6
2  8  10
```
columns を指定しても削除可能。
``` Python
df.drop(columns=['a','c'])
```

```
   b
0  1
1  5
2  9
```
## 行の削除
del では削除できない。

### drop による削除

``` Python
val = np.arange(0,12).reshape(3,4)
df = pd.DataFrame(val, columns=list('abcd'))

df.drop(labels=2, axis=0)
```
```
   a  b  c  d
0  0  1  2  3
1  4  5  6  7
```
index を指定しても削除可能。

``` Python
val = np.arange(0,12).reshape(3,4)
df = pd.DataFrame(val, columns=list('abcd'))

df.drop(index=2)
```
```
   a  b  c  d
0  0  1  2  3
1  4  5  6  7
```

## popメソッド
pop メソッドを使うと、１列を取り出せる。
取り出された列は、元のデータフレームから削除される。

```
df.pop('c')  
```
```
0     2
1     6
2    10
Name: c, dtype: int64
```


## データの変更
演算結果を代入することで、データを一律で変更可能。
``` Python
val = np.arange(0,12).reshape(3,4)
df = pd.DataFrame(val, columns=list('abcd'))   

df['c'] = df['c'] * 2

```

```
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

   a  b   c   d
0  0  1   4   3
1  4  5  12   7
2  8  9  20  11

```

### roundメソッド
round メソッドを使うことで、小数点データを切り捨てることが可能。

``` Python
df['時期'] = df['時期'].round()  
```   

### 型キャスト
astype メソッドを使うことで、型変換が可能。

``` Python
df['時期'] = df['時期'].astype('int64')
```
