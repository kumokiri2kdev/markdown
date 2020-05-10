# データ参照

## 位置インデックスとラベル

``` Python
val = np.arange(1, 10).reshape((3, -1))
df = pd.DataFrame(val, index=[0, 2, 4], columns=list('def'))

print(df)

print(df.loc[2])
print(df.iloc[2])
```

```
   d  e  f
0  1  2  3
2  4  5  6
4  7  8  9

d    4
e    5
f    6
Name: 2, dtype: int64

d    7
e    8
f    9
Name: 4, dtype: int64
```
loc で参照するのは ラベル。iloc は、オフセットで参照する。

シリーズでも同様の結果になる。

``` Python
ser = pd.Series([1, 2, 3], index=[0, 2, 4])

print('ser.loc[2] => {}'.format(ser.loc[2]))
print('ser.iloc[2] => {}'.format(ser.iloc[2]))
```

```
ser.loc[2] => 2
ser.iloc[2] => 3
```

### データ参照方法

|記述|解説|
|--|--|
|```df[lable]```|データフレームの列ラベルを指定して列を選択|
|```df[[label1, label2]]```|データフレームの複数の列ラベルを指定して、複数列を選択|
|```df[loc:loc]```|データフレームの行の位置インデックスを指定して行を選択。終点は含まれれない|
|```df.loc[label]```|データフレームの行ラベルを指定して行を選択。```[label,:]``` と同じ|
|```df.loc[:,label]```|データフレームの列ラベルを指定して列を選択|
|```df.loc[label1, label2]```|データフレームの行と列をラベルを指定して要素を選択|
|```df.iloc[loc]```|データフレームの位置インデックスを指定して、行を選択。```[loc,:]```と同じ|
|```df.iloc[[loc1, loc2]]```|データフレームの位置インデックスを指定して行を選択。終点を含む。|
|```df.iloc[loc1, loc2]```|データフレームの行と列を位置インデックスを指定して要素を選択|


サンプルとして、データフレームを作成。
``` Python
val = np.arange(1, 10).reshape((3,-1))
df = pd.DataFrame(val, index=[0, 2, 4], columns=list('def'))
df2 = pd.DataFrame(val, index=[0, 5, 10], columns=[0, 2, 4])
```
```
   d  e  f
0  1  2  3
2  4  5  6
4  7  8  9

    0  2  4
0   1  2  3
5   4  5  6
10  7  8  9
```

### データフレームの列ラベルを指定して列を選択
``` Python
df['e']
```
```
0    2
2    5
4    8
Name: e, dtype: int64
```
### データフレームの複数の列ラベルを指定して複数列を選択
``` Python
df[['e', 'd']]
```
```
   e  d
0  2  1
2  5  4
4  8  7
```
整数ラベルの場合
``` Python
df2[2]
```
```
0     2
5     5
10    8
Name: 2, dtype: int64
```
この場合、２列目が取り出される。
スライスで取り出す場合、
```Python
df2[0:2]
```
```
   0  2  4
0  1  2  3
5  4  5  6
```
この場合、行を取り出す。

bool の配列でも行が取り出される。
``` Python
df[[True, False, True]]
```
```
   d  e  f
0  1  2  3
4  7  8  9
```

[] は、行が取り出されるか列が取り出されるかの法則が曖昧。利便性を重視した実装。
可読性を考えると loc/iloc を使った方がよい。

### 切り出されたデータの変更
``` python
val = np.arange(25).reshape(5,-1)
df = pd.DataFrame(val, columns=list('abcde'))
print('<< 元々の df >>')
delta = df.iloc[1:, 1:]

df.iloc[2,2] = 100

print('<< 変更後の delta >>')

print('<< 変更後の df >>')
```
```
<< 元々の df >>
    a   b   c   d   e
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19
4  20  21  22  23  24

<< 変更後の delta >>
    b    c   d   e
1   6    7   8   9
2  11  100  13  14
3  16   17  18  19
4  21   22  23  24

 << 変更後の df >>
    a   b    c   d   e
0   0   1    2   3   4
1   5   6    7   8   9
2  10  11  100  13  14
3  15  16   17  18  19
4  20  21   22  23  24
```
切り出されたデータを変更すると、切り出しもとも変更される。

```df.copy() ``` とすると、別のインスタンスになる。
copyメソッドには、 deep オプションがあり、default は、True。


|記述|解説|
|--|--|
|```df[start:end:step]```|データフレームの行の位置インデックス start から end まで step の間隔で行を選択。end を含まない。|
|```df[start:end]```|データフレームの行の位置インデックス start から end までの行を選択。endを含まない。|
|```df[start:]```|データフレームの行の位置インデックス start 以降の行を選択|
|```df[:end]```|データフレームの行の位置インデックス end 以前の行を選択。endを含まない|
|```df[:]```|データフレームの全ての行列|
|```df.loc[strt:end]```|データフレームの行ラベル start から end の間の列を選択。end を含む。```df.loc[start:end,:]```と同じ|
|```df.loc[:, start:end]```|データフレームの列ラベル start から end の間の行を選択。end を含む|
|```df.iloc[start:end]```|データフレームの行の位置インデックス start から end 間の行を選択。end を含まない。|
|```df.iloc[:, start:end]```|データフレームの列の位置インデックス start から end 間の列を選択。end を含ま無い。|


サンプルとして、データフレームを作成。
``` python
val = np.arange(0, 25).reshape(5,-1)
df = pd.DataFrame(val, index=[10, 5, 2, 12, 6], columns=list('abcde'))
```
```
     a   b   c   d   e
10   0   1   2   3   4
5    5   6   7   8   9
2   10  11  12  13  14
12  15  16  17  18  19
6   20  21  22  23  24
```

### 角括弧でスライスを指定
```Python
df[2:4]
```
```
     a   b   c   d   e
2   10  11  12  13  14
12  15  16  17  18  19
```
```Python
df[0:5:2]  
```
```
     a   b   c   d   e
10   0   1   2   3   4
2   10  11  12  13  14
6   20  21  22  23  24
```

### step を -1にして逆順データ
``` python
df[::-1]
```
```
     a   b   c   d   e
6   20  21  22  23  24
12  15  16  17  18  19
2   10  11  12  13  14
5    5   6   7   8   9
10   0   1   2   3   4
```

### loc 属性とスライス
```Python
df.loc[:, 'b':'e']
```
```
     b   c   d   e
10   1   2   3   4
5    6   7   8   9
2   11  12  13  14
12  16  17  18  19
6   21  22  23  24
```

### iloc 属性とスライス
``` Python
df.iloc[2:4]
```
```
     a   b   c   d   e
2   10  11  12  13  14
12  15  16  17  18  19
```

``` Python
df.iloc[:, 1:4
```
```
     b   c   d
10   1   2   3
5    6   7   8
2   11  12  13
12  16  17  18
6   21  22  23
```

## 参照属性

### シリーズの属性によるデータ参照
``` Python
ser = pd.Series([1, 2, 3], index=list('abc'))

print('ser.a : {}'.format(ser.a))
print('ser.c : {}'.format(ser.c))
```
```
ser.a : 1
ser.c : 3
```

### データフレームの属性によるデータ参照
``` python
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=list('abc'))

print('<<df.c>>\n{}'.format(df.c))
```
```
<<df.c>>
0    3
1    6
Name: c, dtype: int64
```
データフレームの場合は、column を参照できる。

この参照属性は、参照する id がアルファベット・アンダースコア・数字で構成されていなければいけない。日本語のカラムとかであれば、確実に NG。

## bool 型参照
bool 型の配列を使って、行を取り出せる。

``` Python
df = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
df[[True, False, True]]
```

```
   0  1
0  1  2
2  5  6
```

### 条件式を使用した参照
``` python
val = np.arange(0, 25).reshape(5,-1)
df = pd.DataFrame(val, columns=list('abcde'))

df['a'] < 10
```

```
0     True
1     True
2    False
3    False
4    False
Name: a, dtype: bool
```
データフレームに条件式を適用すると、bool 型の配列となる。
これをそのまま、bool型参照に使用すると、条件にあう行が取り出せる様になる。

``` Python
df[df['a'] < 10]  
```
```
   a  b  c  d  e
0  0  1  2  3  4
1  5  6  7  8  9
```

条件式は複数接続可能。

``` Python
df[(df['a'] >= 5) & (df['b'] % 2 == 0)]  
```
```
    a   b   c   d   e
1   5   6   7   8   9
3  15  16  17  18  19
```

~ を使用すると bool 型は反転する

``` python
~(df['a'] < 10)
```
```
0    False
1    False
2     True
3     True
4     True
Name: a, dtype: bool
```
~ のあとで、データフレームを () でくくる必要ある。

## where メソッド
whereメソッドを使うと、条件に満たない要素は NaNとなる。

```Python
ser = pd.Series([1, 2, 3, 4, 5])
ser.where(ser > 3)  
```
```
0    NaN
1    NaN
2    NaN
3    4.0
4    5.0
dtype: float64
```

``` Python
val = np.arange(25).reshape(5,-1)
df = pd.DataFrame(val, columns=list('abcde'))

df.where(df%2 == 0)

      a     b     c     d     e
0   0.0   NaN   2.0   NaN   4.0
1   NaN   6.0   NaN   8.0   NaN
2  10.0   NaN  12.0   NaN  14.0
3   NaN  16.0   NaN  18.0   NaN
4  20.0   NaN  22.0   NaN  24.0
```

### 値の入れ替え
NaN を別の値に変更する。
``` Python
df.where(df%2 == 0, other=-1)
```

```
    a   b   c   d   e
0   0  -1   2  -1   4
1  -1   6  -1   8  -1
2  10  -1  12  -1  14
3  -1  16  -1  18  -1
4  20  -1  22  -1  24
```
```Python
df.where(df%2 == 0, other=df * 2)
```
```
    a   b   c   d   e
0   0   2   2   6   4
1  10   6  14   8  18
2  10  22  12  26  14
3  30  16  34  18  38
4  20  42  22  46  24
```
### where メソッドを使わずに変更する

``` Python
df[df %2 ==0] = - 1
```
```    
    a   b   c   d   e
0  -1   1  -1   3  -1
1   5  -1   7  -1   9
2  -1  11  -1  13  -1
3  15  -1  17  -1  19
4  -1  21  -1  23  -1
```
## mask

maks メソッドは、where と逆の要素を返す。
``` Python
df.mask(df % 2 == 0)
```
```
      a     b     c     d     e
0   NaN   1.0   NaN   3.0   NaN
1   5.0   NaN   7.0   NaN   9.0
2   NaN  11.0   NaN  13.0   NaN
3  15.0   NaN  17.0   NaN  19.0
4   NaN  21.0   NaN  23.0   NaN
```

## query メソッド
query メソッドを使用すると、文字列表現で参照する行の条件を指定できる。
``` Python
df = pd.DataFrame([[1, 2, 3],[4, 5, 6]], index = [2, 4], columns=list('cde'))

df.query('index > c')
```

```
   c  d  e
2  1  2  3
```

``` Python
scores = [[76, 86, 90],[91, 78, 80],[88, 76, 76]]
names = ['A', 'B', 'C']
subjects = ['数学', '英語', '物理']

df = pd.DataFrame(scores, columns=names, index = subjects)

df.query('A > B')
```
```
      A   B   C
英語  91  78  80
物理  88  76  76
```
AがBより成績がよい科目を抜き出した。


### 複数の query

```Python
df.query('(A > B) & (A > C)')
```
```
A   B   C
英語  91  78  80
物理  88  76  76
```

### 複数の条件式
``` python
df.query('A > C > B')  
```
```
      A   B   C
英語  91  78  80
```

### 文字列の評価

``` Python
df = pd.DataFrame({
    'name': ['荒岩 一味', '荒岩 虹子', '荒岩 まこと', '荒岩 みゆき', '田中 一', '梅田 よしお'],
    'age': [44, 44, 21, 13, 36, 31],
    'sex': ['M', 'F', 'M', 'F', 'M', 'M'],
})

df.query("name == '荒岩 一味'")

df.query("name in ('荒岩 まこと', '荒岩 みゆき')")
```

```
       name  age sex
0  荒岩 一味   44   M

        name  age sex
2  荒岩 まこと   21   M
3  荒岩 みゆき   13   F
```
python の変数を参照。
``` Python
search_name = '田中 一'
df.query("name == @search_name")
```
```
     name  age sex
4  田中 一   36   M
```
部分一致。
```Python
df.query("name.str.startswith('荒岩')", engine='python')
```
```
        name  age sex
0   荒岩 一味   44   M
1   荒岩 虹子   44   F
2  荒岩 まこと   21   M
3  荒岩 みゆき   13   F
```
- startswith
- endswith
- contains
などが使用可能。

<font color="Red">*column 名に 'class' を使ってしまうと、評価できない。*</font>




### 複数の値によるデータ参照
``` Python
df.query('A == [76, 91]')
```
```
      A   B   C
数学  76  86  90
英語  91  78  80
```

* Indexing and Selecting Data

  https://pandas.pydata.org/pandas-docs/version/0.22/indexing.html
