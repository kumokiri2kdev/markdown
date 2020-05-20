

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

```x, y``` に 条件を満たすときと満たさない時の値を指定することで、インデックスではなく、指定した値の配列に変換できる。



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
