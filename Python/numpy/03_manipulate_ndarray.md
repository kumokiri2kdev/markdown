## np.append

配列の末尾に要素を追加した新しい配列を生成する。


``` python
numpy.append(arr, values, axis=None)
```

|引数名|型|概要|
|:--|:-----|:--|
|arr|array_like<br>(配列に相当するもの)|要素が追加される配列を指定する|
|values|array_like<br>(配列に相当するもの)|追加する要素または配列を指定する|
|axis|int|省略可能)初期値 None。<br>どの軸方向に append 演算を適用するか指定する|

``` python
a = np.arange(12)

np.append(a, [12, 13, 14])
```
```
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
```
多次元配列は、axis を指定しないと、１次元配列に変換される。
``` python
a = np.arange(12).reshape((3, 4))  
np.append(a, [[12, 13, 14, 15]])
```
```
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
```
``` python
np.append(a, [[12, 13, 14, 15]], axis=0)  
```
```
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
```

``` python
np.append(a, [[100], [200], [300]], axis=1)  
```
```
array([[  0,   1,   2,   3, 100],
       [  4,   5,   6,   7, 200],
       [  8,   9,  10,  11, 300]])
```


## np.all
配列全体、もしくは、行・列の値が、**全て真** であるかどうかを返す。

``` python
numpy.all(a, axis=None, out=None, keepdims=False)
```

|引数名|型|概要|
|:--|:-----|:--|
|a |array_like<br>(配列に相当するもの)| 入力する配列、または配列に変換できるオブジェクト を指定する|
|axis |None、int または int のタプル| (省略可能)初期値 None。 どの軸方向に要素を見ていくかを指定する|
|out|ndarray|(省略可能)初期値 None。 結果を格納する配列を指定する |
|keepdims|bool 値|(省略可能)初期値 False。 結果を出力する際、要素数が1になった次元もそのま ま残すかどうかを指定する。True にすると元の配列に 対してブロードキャストを正しく適用して演算を施す ことができる|

``` python
a = np.array([
  [1, 1, 1],
  [1, 0, 0],
  [1, 0, 1],
])    

np.all(a)
```
```
False
````
``` python
b = np.ones((3, 3))
np.all(b)
```
```
True
```
``` python
np.all(a < 2)
```
```
True
```
行方向に対するオペレーション。
``` python
np.all(a, axis=0)
```
```
array([ True, False, False])
```
列方向に対するオペレーション。
``` python
np.all(a, axis=1)
```
```
array([ True, False, False])
```
keepdims を指定すると、元の次元を残す。
``` python
np.all(a, axis=0, keepdims=True)
```
```
array([[ True, False, False]])
```
ndarray に all メソッドを使っても同じ結果が得られる。

## np.any
配列全体、もしくは、行・列の値に、**一つでも真** があるかどうかを返す。

``` python
numpy.any(a, axis=None, out=None, keepdims=False)
```

|引数名|型|概要|
|:--|:-----|:--|
|a |array_like<br>(配列に相当するもの)| 入力する配列、または配列に変換できるオブジェクト を指定する|
|axis |None、int または int のタプル| (省略可能)初期値 None。 どの軸方向に要素を見ていくかを指定する|
|out|ndarray|(省略可能)初期値 None。 結果を格納する配列を指定する |
|keepdims|bool 値|(省略可能)初期値 False。 結果を出力する際、要素数が1になった次元もそのま ま残すかどうかを指定する。True にすると元の配列に 対してブロードキャストを正しく適用して演算を施す ことができる|


``` python
a = np.array([[9, 8, 6], [4, 6, 4]])  
np.any(a==9)
```
```
True
```
``` python
np.any(a==9, axis=0)
```
```
array([ True, False, False])
```
``` python
np.any(a==9, axis=1)  
```
```
array([ True, False])
```



## np.where
条件を満たす要素の**インデックス**を返す。

``` python
numpy.where(condition[, x, y])
```

|引数名|型|概要|
|:--|:-----|:--|
|condition|array_like(配列に相当す るもの)もしくは bool 値|条件もしくは bool 値を指定する|
|x, y|array_like(配列に相当するもの)|(省略可能)conditionで指定された条件や bool値に対してTrueならxを、Falseなら y を返す。<br>x、y の shape は元の配列と揃えるようにする<br>(指定する時は x、y の両方を指定する必要があ る)|


``` python
a = np.array([10, 12, 9, 3, 19])   

np.where(a < 10)
```
```
(array([2, 3]),)
```
``` python
a[np.where(a < 10)]
```
```
array([9, 3])
```
これだけであれば、```a[a < 10]  ``` と同じ動作。



```x, y``` に 条件を満たすときと満たさない時の値を指定することで、インデックスではなく、指定した値の配列に変換できる。

``` python
a = np.arange(10)
np.where(a % 2 == 0, 'even', 'odd')
```
```
array(['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even',
       'odd'], dtype='<U4')
```

変換に配列を指定すると、その位置にそった値が適用される。
```python
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.zeros(a.shape, dtype=int)

np.where(a % 2 == 0, a, b)   
```
```
array([[0, 2, 0],
       [4, 0, 6]])
```

## np.arange
連番や等差整列を生成する関数。

np.arange
``` python
numpy.arange([start, ]stop, [step, ]dtype=None)
```
np.arangeの引数

|引数名|型|概要|
|:--|:-----|:--|
|start|int または float|(省略可能)初期値 0。<br>生成する等差数列の最初の項を設定する。これを指定しない と 0 から始まる等差数列が生成される。|
|stop|int または float|生成する等差数列の終点を指定する。|
|step| int または float | (省略可能)初期値 1。<br>生成される数列の 1 つ 1 つの項間における差(公差)を指定 する。
|dtype|データ型|(省略可能)初期値 None。 生成される数列のデータ型を指定する。これを指定しない と start や stop で入力したデータ型がそのまま適用される|

``` python
np.arange(1, 10)
```
```
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
```
start と end に 1x1 の numpy 配列を渡しても同じ結果になる。
``` python
np.arange(np.array([1]), np.array([10]))
```
