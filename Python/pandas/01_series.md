# Series

前提事項として、下記を import しておく事。
``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


## シリーズの概要
シリーズは、１次元の配列オブジェクト。
``` python
height_list = [185, 162, 171, 155, 191, 166]
height_series = pd.Series(height_list)
print(height_series)   
```
[出力]
```
0    185
1    162
2    171
3    155
4    191
5    166
dtype: int64




NumPy 配列からも生成可能。

``` python
weight_arr = np.array([72, 51, 69, 55, 87, 78])
weight_series = pd.Series(weight_arr)
print(weight_series)
```
[出力]
```
0    72
1    51
2    69
3    55
4    87
5    78
dtype: int64
```

### name 属性

``` python
ser = pd.Series([1, 2, 3], name='some series')  
print(ser)
```
[出力]
```
0    1
1    2
2    3
Name: some series, dtype: int64
```
### index (label)
``` python
val = [1, 2, 3, 4, 5]
labels = list('aacdf')
ser = pd.Series(val, index=labels)

print(ser)
```
[出力]
```
a    1
a    2
c    3
d    4
f    5
dtype: int64
```
index は、Series から参照可能。
``` python
print(ser.index)
```
[出力]
```
Index(['a', 'a', 'c', 'd', 'f'], dtype='object')
```

### dictionary

``` Python
dic = {'T': 185, 'H': 162, 'B': 171, 'R': 155, 'M': 191, 'S': 166}     
ser = pd.Series(dic)
print(ser)
```

[出力]
```
T    185
H    162
B    171
R    155
M    191
S    166
dtype: int64
```

### dictionary + index
```python
dic = {'a':0,'b':1,'c':2}   
a = pd.Series(dic, index=['a','b','d'])  
print(a)
```

index で与えられていない index に相当する値はNaN になり、dictionary にはあっても index には無い要素は削除される。

[出力]
```
a    0.0
b    1.0
d    NaN
dtype: float64
```

### スカラー値からシリーズを作成
```python
a = pd.Series(10, index=['A', 'B', 'C'])
print(a)
```
[出力]
```
A    10
B    10
C    10
dtype: int64
```
### インデックス参照
```python
val = [i for i in range(1,6)]   
ser = pd.Series(val, index=list('アイウエオ'))
print(ser)

print(ser['ア'])

print(ser['ア':'エ'])

print(ser.iloc[0])

print(ser[ser > 3])

```

[出力]
```
ア    1
イ    2
ウ    3
エ    4
オ    5
dtype: int64

1

ア    1
イ    2
ウ    3
エ    4
dtype: int64

1

エ    4
オ    5
dtype: int64
```

### シリーズの演算
ser を作成している前提で下記を実行。
```python
print(ser + 2)
```

[出力]
```
ア    3
イ    4
ウ    5
エ    6
オ    7
dtype: int64
```
ちなみに、通常のリストに '+' リストの拡張になる。

```python
mylist = [i for i in range(1,6)]   
print(mylist + [2])
```
[出力]
```
[1, 2, 3, 4, 5, 2]
```

リストの各要素に 2 を足したい場合、ループを使わなければならない。

```python
for i in range(len(mylist)):
  mylist[i] += 2

print(mylist)
```
[出力]
```
[3, 4, 5, 6, 7]
```

Series は、最初の例の様に、Series に 演算を行うと全ての要素に演算結果が反映される。

### Series 同士の演算
```Python
val = [i for i in range(1,6)]    
ser = pd.Series(val, index=list('アイウエオ'))  

ser2 = pd.Series([i for i in range(6,11)], index=list('アイウエカ'))
print(ser + ser2)
```
[出力]
```
ア     7.0
イ     9.0
ウ    11.0
エ    13.0
オ     NaN
カ     NaN
dtype: float64
```
双方に同じ インデックスが無い要素は、欠損値(NaN)になっている。

## シリーズの基本操作
### シリーズの index 属性
``` python
val = [i for i in range(1, 6)]

a = pd.Series(val)
b = pd.Series(val, index = [i for i in range 5])
c = pd.Series(val, index = list('abcde'))

print(a.index)
print(b.index)
print(c.index)
```
[出力]
```
RangeIndex(start=0, stop=5, step=1)
Int64Index([0, 1, 2, 3, 4], dtype='int64')
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
```

### dtype 属性
``` Python
a = pd.Series(['a', 'b', 'c'])
b = pd.Series([1, 2, 3])
c = pd.Series([1.0, 2.0, 3.0])
d = pd.Series([True, False, True])
e = pd.Series(['a', 1, True])

print(a.dtype, b.dtype, c.dtype, d.dtype, e.dtype )
```
[出力]
```
object int64 float64 bool object
```

### loc 属性
``` Python
a = pd.Series([1, 2, 3], index = [1, 2, 3])
b = pd.Series([1 ,2, 3], index = list('abc'))

print(a.loc[1])
print(b.loc['a'])
```
[出力]
```
1
1
```

### iloc属性
``` Python
print(a.iloc[0])
print(b.iloc[0])
```
[出力]
```
1
1
```

### スライスの利用
loc 属性のスライスの最後の要素は終点を含むが、iloc属性は終点を含まない。
loc の場合。
``` Python
 a.iloc[0:1]
```
[出力]
```
1    1
dtype: int64
```
iloc は、終点を含む。
``` Python
b.loc['a':'b']
```
[出力]
```
a    1
b    2
dtype: int64
```

### size属性

```Python
ser = pd.Series([1 , 1, 3, 4, 'a'])
print(ser.size)
```
[出力]
```
5
```

### is_unique属性
``` Python
a = pd.Series([1, 2, 3])
b = pd.Series([1, 1, 3])

print(a.is_unique)
print(b.is_unique)
```
[出力]
```
True
False
```

### values属性
values属性で、要素を numpy 配列として取り出せる。
ただし、dtype category のデータは、numpy 配列にならない。

``` python
a = pd.Series([1, 2, 3])
b = pd.Series(list('abc'))
c = pd.Series(list('aab'), dtype='category')

print(type(a.values), a.values)
print(type(b.values), b.values)
print(type(c.values), c.values)
```
[出力]
```
<class 'numpy.ndarray'> [1 2 3]
<class 'numpy.ndarray'> ['a' 'b' 'c']
<class 'pandas.core.arrays.categorical.Categorical'> [a, a, b]
Categories (2, object): [a, b]
```

## 要素の変更と追加
### 変更
``` Python
ser = pd.Series([i for i in range(1,6)], index=list('abcde'))

ser['a'] = 6
ser['b':'d'] = 7

print(ser)
```
[出力]
```
a    6
b    7
c    7
d    7
e    5
dtype: int64
```

### 追加

``` Python
ser = pd.Series([i for i in range(1,6)], index=list('abcde'))

ser['あ'] = 4

print(ser)
```
[出力]
```
a    1
b    2
c    3
d    4
e    5
あ    4
dtype: int64
```

```Python
ser = pd.Series([i for i in range(1,6)], index=list('abcde'))  
ser2 = pd.Series([5, 6], index=list('いう'))

print(ser.append(ser2))
```
[出力]
```
a    1
b    2
c    3
d    4
e    5
あ    4
い    5
う    6
dtype: int64
```

append() に、ingore_index を指定すると、新たな index が付与される。
``` Python
ser = pd.Series([i for i in range(1,6)], index=list('abcde'))  
ser2 = pd.Series([5, 6], index=list('いう'))

print(ser.append(ser2, ignore_index=True))
```

[出力]
```
0    1
1    2
2    3
3    4
4    5
5    4
6    5
7    6
dtype: int64
```

### 削除
``` Python
ser = pd.Series([i for i in range(1,6)], index=list('abcde'))

del ser['b']

print(ser)
```
[出力]
```
a    1
c    3
d    4
e    5
dtype: int64
```

drop() による削除。
``` Python
ser = pd.Series([i for i in range(1,6)], index=list('abcde'))

ser.drop('b', inplace=True)

print(ser)
```
[出力]
```
a    1
c    3
d    4
e    5
dtype: int64
```
inplaceを指定すると、シリーズ自体を変更する。

### 重複値の削除
```Python
ser = pd.Series([1, 1, 2, 2, 2, 3], index = list('abcdef'))

ser.drop_duplicates(keep='first')


```
[出力]
```
a    1
c    2
f    3
dtype: int64
```
```python
ser = pd.Series([1, 1, 2, 2, 2, 3], index = list('abcdef'))
ser.drop_duplicates(keep=False)
```
[出力]
```
f    3
dtype: int64
```

###欠損値
``` Python
ser = pd.Series([1, np.nan, 3, 4, np.nan], index=list('abcde'))

ser.isna()

ser.dropna()

```
[出力]
```
a    False
b     True
c    False
d    False
e     True
dtype: bool

a    1.0
c    3.0
d    4.0
dtype: float64
```
