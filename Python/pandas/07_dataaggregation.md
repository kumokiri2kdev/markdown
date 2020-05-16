# データ集計

## 最大値・最小値
### シリーズ

``` Python
ser = pd.Series([0, 1, 2, 3, 4])

print('Min : {}'.format(ser.min()))
print('Max : {}'.format(ser.max()))
```

```
Min : 0
Max : 4
```

### データフレーム
``` Python
val = np.arange(0, 9).reshape(3, -1)
df = pd.DataFrame(val, index=list('edf'))
df.columns = list('abc')

print('<列方向の最小値>')
df.min(axis=0)

print('<行方向の最小値>')
df.min(axis=1)
```

```
   a  b  c
e  0  1  2
d  3  4  5
f  6  7  8

<列方向の最小値>
a    0
b    1
c    2
dtype: int64

<行方向の最小値>
e    0
d    3
f    6
dtype: int64
```
max() についても同様。

## 平均値

``` Python
val = np.arange(0, 9).reshape(3, -1)
df = pd.DataFrame(val, columns=list('abc'), index=list('edf'))

print('<列方向の平均値>')
df.mean(axis=0)

print('<行方向の平均値>')
df.mean(axis=1)
```

```
   a  b  c
e  0  1  2
d  3  4  5
f  6  7  8

<列方向の平均値>
a    3.0
b    4.0
c    5.0
dtype: float64

<行方向の平均値>
e    1.0
d    4.0
f    7.0
dtype: float64
```

## 中央値
``` Python

print('<列方向の中央値>')
df.median(axis=0)

print('<行方向の中央値>')
df.median(axis=1)

```
```
　　a  b  c
e  0  1  2
d  3  4  5
f  6  7  8

<列方向の中央値>
e    1.0
d    4.0
f    7.0
dtype: float64

<行方向の中央値>
a    3.0
b    4.0
c    5.0
dtype: float64
```

## 最頻値
``` Python
df = pd.DataFrame([[1, 1, 2, 3, 4]])

print('<最頻値>')
df.mode(axis=1)

df = df.drop(labels=[0],axis=1)  
print('<最頻値>')
df.mode(axis=1)
```
```
   0  1  2  3  4
0  1  1  2  3  4

0
0  1

   1  2  3  4
0  1  2  3  4
```
最頻値が複数の場合、複数カラムの行として出力される。

## 標準偏差
標準偏差は、データのばらつき度合いを示す指標。

``` Python
table_a = pd.DataFrame([[152, 151, 150, 147, 181, 190, 187, 149, 196]])
table_b = pd.DataFrame([[162, 161, 165, 147, 161, 175, 187, 175, 170]])

print('<<標準偏差>>')
table_a.std(axis=1, ddof=0)
table_b.std(axis=1, ddof=0)
```
```
0    19.607255
dtype: float64

0    10.739336
dtype: float64
```

``` Python
print('<<不偏標準偏差>>')
table_a.std(axis=1, ddof=1)
table_b.std(axis=1, ddof=1)
```
```
0    20.796634
dtype: float64

0    11.390786
dtype: float64
```

stdメソッドの ddof オプションを 0 にすると標準偏差を求め、指定しないと 不偏標準偏差を求める。（デフォルトが ddof=1）
numpy.std は逆の動作をとるので注意が必要。

## 分位数
分位数は、データの相対的位置を確認する値。

``` Python
df = pd.DataFrame([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

print('<<ど真ん中のデータ>>')
df.quantile(q=0.5, axis=1)

print('<<1/4, 1/2, 3/4 のデータ>>')
df.quantile(q=[0.25, 0.5, 0.75], axis=1)
```

```
<<ど真ん中のデータ>>
0    5.5
Name: 0.5, dtype: float64

<<1/4, 1/2, 3/4 のデータ>>
         0
0.25  3.25
0.50  5.50
0.75  7.75
```
quantile は、interpolation のオプションで、算出方法を指定することができる。

## 累積和
累積和は、データを順番に足し合わせていった数値。

``` Python
val = np.arange(9).reshape(3,-1)
df = pd.DataFrame(val, columns=list('abc'), index=list('def'))

print('<< 列方向の累積和 >>')
df.cumsum(axis=0)

print('<< 行方向の累積和 >>')
df.cumsum(axis=1)
```

```
   a  b  c
d  0  1  2
e  3  4  5
f  6  7  8

<< 列方向の累積和 >>
   a   b   c
d  0   1   2
e  3   5   7
f  9  12  15

<< 行方向の累積和 >>
   a   b   c
d  0   1   3
e  3   7  12
f  6  13  21

```

途中に NaN が含まれていても、データ処理は継続される。

``` Python
df.loc['e','a'] = np.nan
df.loc['f','b'] = np.nan

df.cumsum(axis=1)
```
```
     a    b  c
d  0.0  1.0  2
e  NaN  4.0  5
f  6.0  NaN  8

     a    b  c
d  0.0  1.0  2
e  NaN  4.0  5
f  6.0  NaN  8
```
skipna オプションを False にすると、以降の計算をしなくなる。

## 累積積
cumprod メソッドで、累積の積を求められる。

``` Python
df.cumprod(axis=0)
```

```
   a   b   c
d  0   1   2
e  0   4  10
f  0  28  80
```


## ビン分割

### cut関数
cut 関数は、「値」を基にビン分割を行う。
``` Python
age = pd.Series([12,14,26,28,30,32,44,58], index=list('abcdefgh'))
pd.cut(x=age, bins=[0, 10, 19, 29, 39, 49, 59])
```
```
a    (10, 19]
b    (10, 19]
c    (19, 29]
d    (19, 29]
e    (29, 39]
f    (29, 39]
g    (39, 49]
h    (49, 59]
dtype: category
Categories (6, interval[int64]): [(0, 10] < (10, 19] < (19, 29] < (29, 39] < (39, 49] < (49, 59]]

```
分割時に label を指定すると、分割時にラベリングされる。

``` Python
pd.cut(x=age, bins=[0, 19, 60], labels=['non-adult', 'adult'])
```
```
a    non-adult
b    non-adult
c        adult
d        adult
e        adult
f        adult
g        adult
h        adult
dtype: category
Categories (2, object): [non-adult < adult]
```

value_counts() で、個数を確認することができる。

```Python
pd.cut(x=age, bins=[0, 19, 60], labels=['non-adult', 'adult']).value_counts()
```
```
adult        6
non-adult    2
dtype: int64
```

### qcut 関数
qcut 関数は、「量」を基にビン分割を行います。

``` Python
age = pd.Series([12,14,26,28,30,32,44,58])
pd.qcut(x=age, q=2)
```
```
0    (11.999, 29.0]
1    (11.999, 29.0]
2    (11.999, 29.0]
3    (11.999, 29.0]
4      (29.0, 58.0]
5      (29.0, 58.0]
6      (29.0, 58.0]
7      (29.0, 58.0]
dtype: category
Categories (2, interval[float64]): [(11.999, 29.0] < (29.0, 58.0]]
```
位置を指定しての分割も可能。

``` Python
age = pd.Series([12,14,26,28,30,32,44,58])
pd.qcut(x=age, q=[0, 0.25, 0.5, 0.75,1])
```
```
0    (11.999, 23.0]
1    (11.999, 23.0]
2      (23.0, 29.0]
3      (23.0, 29.0]
4      (29.0, 35.0]
5      (29.0, 35.0]
6      (35.0, 58.0]
7      (35.0, 58.0]
dtype: category
Categories (4, interval[float64]): [(11.999, 23.0] < (23.0, 29.0] < (29.0, 35.0] < (35.0, 58.0]]
```
cut 同様、ラベル漬けが可能。

``` Python
pd.qcut(x=age, q=2, labels=['young', 'old'])
```
```
0    young
1    young
2    young
3    young
4      old
5      old
6      old
7      old
dtype: category
Categories (2, object): [young < old]
```
retbins を使用すると、境界とビンを個別に取得可能。

```
bins, labels = pd.qcut(x=age, q=2, labels=['young', 'old'], retbins=True)
print(labels)
```
```
array([12., 29., 58.])
```
qcut で指定したラベルが返ってくるんではなく、どこで分割したかが返ってくる。


## 要約統計量

``` Python
np.random.seed(seed=1)
val = np.random.randint(0,100,size=9).reshape(3,-1)
df = pd.DataFrame(val, columns=list('abc'))
df.describe()
```

```
               a          b          c
count   3.000000   3.000000   3.000000
mean    9.000000  39.666667  68.333333
std     9.848858  31.659648  17.156146
min     1.000000  18.000000  50.000000
25%     3.500000  21.500000  60.500000
50%     6.000000  25.000000  71.000000
75%    13.000000  50.500000  77.500000
max    20.000000  76.000000  84.000000
```
NaN の値がある場合は、無視される。

パーセンタイルの指定が可能。

```Python
df.describe(percentiles=[0.1, 0.2, 0.3])
```
```
               a          b          c
count   3.000000   3.000000   3.000000
mean    9.000000  39.666667  68.333333
std     9.848858  31.659648  17.156146
min     1.000000  18.000000  50.000000
10%     2.000000  19.400000  54.200000
20%     3.000000  20.800000  58.400000
30%     4.000000  22.200000  62.600000
50%     6.000000  25.000000  71.000000
max    20.000000  76.000000  84.000000
```

オブジェクト型の要素は別の観点で統計量が取られる。
``` Python
ser = pd.Series(list('aba'))

ser.describe()  
```

```
count     3
unique    2
top       a
freq      2
dtype: object
```


## ピボットテーブル

### マトリクス変形
```Python
 import pandas as pd

 user_data = [
  [1, 1, 10], [1, 2, 5],[1, 3, 6],[1, 6, 4],[2, 2, 10],[2, 6, 4],[2, 6, 3]
  ]

  df = pd.DataFrame(user_data, columns=['user_id', 'item_id', 'rating'])
```
```
user_id  item_id  rating
0        1        1      10
1        1        2       5
2        1        3       6
3        1        6       4
4        2        2      10
5        2        6       4
6        2        6       3
```
このテーブルを、ユーザー毎の行とアイテムごとの列のマトリクスにして Rating をデータとしてまとめるには、

``` python
pivot = pd.pivot_table(df, index='user_id', columns='item_id', values='rating')
```
```
item_id     1     2    3    6
user_id                      
1        10.0   5.0  6.0  4.0
2         NaN  10.0  NaN  3.5
```

### 集約

```Python
np.random.seed(seed=1)
scores = np.random.randint(70, 100, size=25).reshape(5, -1)
subs = ['math', 'eng', 'scie', 'art', 'hist']
df = pd.DataFrame(scores, columns=subs)
df['club'] = ['soccer', 'tennis', 'tennis', 'soccer', 'tennis']
df['sex'] = list('MMFMF')

```

```
   math  eng  scie  art  hist    club sex
0    75   81    82   78    79  soccer   M
1    81   75    85   70    86  tennis   M
2    71   82    77   83    98  tennis   F
3    76   95    88   90    75  soccer   M
4    88   90    81   98    80  tennis   F
```

```Python
pd.pivot_table(df, index='sex', aggfunc=np.mean)
```
```
art        eng  hist       math  scie
sex                                             
F    90.500000  86.000000    89  79.500000    79
M    79.333333  83.666667    80  77.333333    85
```

```Python
pd.pivot_table(df, index='sex', values='art')
```
```
           art
sex           
F    90.500000
M    79.333333
```

### columns の追加
``` Python
pd.pivot_table(df, index='club', columns='sex', aggfunc=np.mean)
```
```
         art         eng        hist        math        scie      
sex        F     M     F     M     F     M     F     M     F     M
club                                                              
soccer   NaN  84.0   NaN  88.0   NaN  77.0   NaN  75.5   NaN  85.0
tennis  90.5  70.0  86.0  75.0  89.0  86.0  79.5  81.0  79.0  85.0
```

### 複数 index
``` Python
pd.pivot_table(df, index=['sex', 'club'], aggfunc=np.mean)
```
```
             art  eng  hist  math  scie
sex club                               
F   tennis  90.5   86    89  79.5    79
M   soccer  84.0   88    77  75.5    85
    tennis  70.0   75    86  81.0    85
```

```Python
pd.pivot_table(df, index=['sex', 'club'], values='eng', aggfunc=[np.sum, np.max, np.mean])
```
```
            sum amax mean
            eng  eng  eng
sex club                 
F   tennis  172   90   86
M   soccer  176   95   88
    tennis   75   75   75
```
```Python
pd.pivot_table(df, index=['sex', 'club'], aggfunc={'eng': np.max, 'math':np.mean})
```
```
            eng  math
sex club             
F   tennis   90  79.5
M   soccer   95  75.5
    tennis   75  81.0
```

### margins
margins True を指定すると、列方向で合算した値を表示する。

```Python
pd.pivot_table(df, index='club', values='math', aggfunc=np.mean, margins=True)
```
```
        math
club        
soccer  75.5
tennis  80.0
All     78.2
```
``` Python
pd.pivot_table(df, index='club', columns='sex', values='math', aggfunc=np.mean, margins=True)
```

```
sex        F          M   All
club                         
soccer   NaN  75.500000  75.5
tennis  79.5  81.000000  80.0
All     79.5  77.333333  78.2
```

## クロス集計
``` Python
np.random.seed(seed=1)
sex = np.random.choice(['M', 'F'], size=10)
eva = np.random.randint(70, 100, size=10)
city = np.random.choice(['Tokyo', 'Osaka', 'Sapporo'], size=10)
div = np.random.choice(['sales', 'hr', 'marketing', 'dev'], size=10)
dic = {'sex': sex, 'evaluation': eva, 'city': city, 'division':div}

df = pd.DataFrame(dic)
```

```
  sex  evaluation     city   division
0   F          86  Sapporo      sales
1   F          71    Osaka        dev
2   M          82  Sapporo        dev
3   M          77    Tokyo         hr
4   F          83    Tokyo         hr
5   F          98  Sapporo        dev
6   F          76    Tokyo  marketing
7   F          95    Osaka      sales
8   F          88  Sapporo  marketing
9   M          90  Sapporo         hr
```
``` Python
pd.crosstab(index=df['sex'], columns=df['city'])
```
```
city  Osaka  Sapporo  Tokyo
sex                        
F         2        3      2
M         0        2      1
```

``` Python

pd.crosstab(index=[df['sex'], df['city']], columns=df['division'])

```
```
division     dev  hr  marketing  sales
sex city                              
F   Osaka      1   0          0      1
    Sapporo    1   0          1      1
    Tokyo      0   1          1      0
M   Sapporo    1   1          0      0
    Tokyo      0   1          0      0
```
margins も指定可能。

### aggfunc の指定
``` Python
pd.crosstab(index=df['sex'], columns=df['city'], values=df['evaluation'], aggfunc=np.mean)
```
```
city  Osaka    Sapporo  Tokyo
sex                          
F      83.0  90.666667   79.5
M       NaN  86.000000   77.0
```
