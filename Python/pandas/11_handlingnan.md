# 欠損値


NaN は、「Not a Number」の略で、欠損値として扱われる。
None も欠損値として扱われる。

### isnaメソッド
``` Python
df = pd.DataFrame([[0, np.nan, 2],[None, 4, 4]], columns=list('abc'))

df.isna()
```


```
     a    b  c
0  0.0  NaN  2
1  NaN  4.0  4


       a      b      c
0  False   True  False
1   True  False  False
```

### inf の取り扱い
inf は、「無限大]
設定をすることで、inf を欠損値として取り扱うことが可能。

``` Python
df = pd.DataFrame([[0, -np.inf, 2],[np.inf, 4, 4]], columns=list('abc'))  
df.isna()

pd.options.mode.use_inf_as_na = True

df.isna()
```

```
     a    b  c
0  0.0 -inf  2
1  inf  4.0  4

       a      b      c
0  False  False  False
1  False  False  False

       a      b      c
0  False   True  False
1   True  False  False
```

### NaT
Natは、「Not a Time」

### isnull メソッド
``` Python
df = pd.DataFrame([[0, np.nan, 2],[None, 4, 4]], columns=list('abc'))

df.isna()

pd.isnull(df)
```

```
       a      b      c
0  False   True  False
1   True  False  False

       a      b      c
0  False   True  False
1   True  False  False
```

### notna メソッド
notna メソッドは、isna と逆の結果を返す。

``` Python
df.notna()
```

```
       a      b     c
0   True  False  True
1  False   True  True
```

### NaN の行のみを取り出す
``` Python
df[df['a'].isna()]
```
```
    a    b  c
1 NaN  4.0  4
```

### NaN の行のみを取り除く
``` Python
df[df['a'].notna()]
```
```
     a   b  c
0  0.0 NaN  2
```
## 欠損値の削除

### 欠損値のある行を取り除く
``` Python
val = np.arange(9).reshape(3, -1)
df = pd.DataFrame(val, columns=list('abc'), index=list('def'))
df.loc['d', 'a'], df.loc['e', 'b'] = np.nan, np.nan

df.dropna(axis=0)

df.dropna(axis=1)
```
```
     a    b  c
d  NaN  1.0  2
e  3.0  NaN  5
f  6.0  7.0  8

     a    b  c
f  6.0  7.0  8

   c
d  2
e  5
f  8
```
dropna には how オプションがあり、 ```any``` を指定すると、一つでも 欠損している場合、```all``` を指定すると、全てが欠損値の場合の条件となる。

thresh=n を指定すると、欠損値が n 個あったら drop するという指定になる。

subset を指定すると、欠損値をチェックする行、列を指定できる。

``` Python
df.dropna(axis=0, subset=['b', 'c'])
```
```
     a    b  c
d  NaN  1.0  2
f  6.0  7.0  8
```

## 欠損値の置換

### ゼロに変換


### カラム毎の値の指定
``` Python
val = np.arange(9).reshape(3, -1)
df = pd.DataFrame(val, columns=list('abc'), index=list('def'))
df.loc['d', 'a'], df.loc['e', 'b'] = np.nan, np.nan

df.fillna(value=0)
```
```
     a    b  c
d  NaN  1.0  2
e  3.0  NaN  5
f  6.0  7.0  8

     a    b  c
d  0.0  1.0  2
e  3.0  0.0  5
f  6.0  7.0  8
```

``` Python
val = np.arange(9).reshape(3, -1)
df = pd.DataFrame(val, columns=list('abc'), index=list('def'))
df.loc['d', 'a'], df.loc['e', 'b'] = np.nan, np.nan

filling = {'a': 100, 'b': 200, 'c':300}
df.fillna(value=filling)
```
