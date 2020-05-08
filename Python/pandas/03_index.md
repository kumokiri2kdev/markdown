# インデックス


## インデックス概要

### インデックス生成

``` Python
df = pd.DataFrame([[1, 2, 3],[4, 5, 6]])

print(df.index)
print(df.columns)
```

[出力]
```
RangeIndex(start=0, stop=2, step=1)
RangeIndex(start=0, stop=3, step=1)
```

インデックス自体を生成することも可能。

``` Python
print(pd.Index([ 1, 2, 3, 4, 5]))
```
[出力]
```
Int64Index([1, 2, 3, 4, 5], dtype='int64')
```

下記の様に
```Python
df1 = pd.DataFrame([1, 2, 3, 4, 5])
print(df1.index)
df2 = pd.DataFrame([1, 2, 3, 4, 5],index=[0,1,2,3,4])
print(df2.index)
```
[出力]
```
RangeIndex(start=0, stop=5, step=1)

Int64Index([1, 2, 3, 4, 5], dtype='int64')
```
インデックスを指定する場合、Int64Index になるが、RangeIndex の方がメモリ効率がよいので計算パフォーマンスが高くなる場合が多い。

### dix_date
インデックスを日付型にする場合は、dix_date を使用する。

※ DatetimeIndex は、deprecated　になっている。
``` Python
idx_date = pd.date_range(
            freq='D',
            start='2018-12-28',
            end='2019-01-05'
            )

df_date = pd.DataFrame([i for i in range(1, 10)], index=idx_date)

print(df_date)
```

[出力]
```
            0
2018-12-28  1
2018-12-29  2
2018-12-30  3
2018-12-31  4
2019-01-01  5
2019-01-02  6
2019-01-03  7
2019-01-04  8
2019-01-05  9
```

次の様な指定で取り出すことも可能。
``` Python
df_date['2019']
```
[出力]
```
            0
2019-01-01  5
2019-01-02  6
2019-01-03  7
2019-01-04  8
2019-01-05  9
```
'2019-01' でも可能。

### 再インデックス
```Python
val = np.arange(1, 10).reshape((3,-1))
df = pd.DataFrame(val, index=[0, 2, 4], columns=['a', 'b', 'c'])

print(df)

df = df.reindex([0, 1, 2, 3, 4])

print(df)

df.index = [5,6,7,8,9]

print(df)

df = df.reindex(columns=['a', 'b', 'c', 'd'])

print(df)
```
[出力]
```
   a  b  c
0  1  2  3
2  4  5  6
4  7  8  9

     a    b    c
0  1.0  2.0  3.0
1  NaN  NaN  NaN
2  4.0  5.0  6.0
3  NaN  NaN  NaN
4  7.0  8.0  9.0

     a    b    c
5  1.0  2.0  3.0
6  NaN  NaN  NaN
7  4.0  5.0  6.0
8  NaN  NaN  NaN
9  7.0  8.0  9.0

     a    b    c   d
5  1.0  2.0  3.0 NaN
6  NaN  NaN  NaN NaN
7  4.0  5.0  6.0 NaN
8  NaN  NaN  NaN NaN
9  7.0  8.0  9.0 NaN
```
#### reset_index
reset_index により、インデックスが再度自動採番される。

``` Python

val = np.arange(1, 10).reshape((3,-1))
df = pd.DataFrame(val, index=[0, 2, 4], columns=['a', 'b', 'c'])

df.reset_index(drop=True)
```

```
   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9
```

drop を指定しないと、元々の インデックスが残ってしまう。
