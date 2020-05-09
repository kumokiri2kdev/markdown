
## 列と行

列 は column。
行 は index。

```
[[ 0,  1,  2,  3,  4],
 [ 5,  6,  7,  8,  9],
 [10, 11, 12, 13, 14]]
```
上の配列は、(3, 5)の配列で、３行 x ５列。


## データフレーム
### 列参照
``` df['id'] ``` は、列の参照。

### 行参照
行を参照するには、loc/iloc を使用しなければいけない。

```df.iloc[0]```

```df.loc[0]```

### iloc/loc のスライス
loc は、最後の要素を含むが、iloc は含まない。

### bool 型配列で行を取り出す。
```df[[True, False, True]]```

これも、bool 型配列での行の取り出しと原理は同じ。

```df[df['a'] < 10]  ```

## axis
axis = 0 は、列方向。
axis = 1 は、行方向。

https://qiita.com/Phoeboooo/items/b464b7df3c64a33caf94

## 欠損値の置換
置換する値を対応する列名を dict で渡す。
``` Python
illing = {'a': 100, 'b': 200, 'c':300}
df.fillna(value=filling)
```

## 列を新規に追加してデータをいれる
``` df['new'] = df['exist_a'] + df['exist_b'] ```

## インデックス
インデックスを numpy 配列として取り出す。
``` df.index.values```

インデックスを振り直す
``` df.reset_index(drop=True) ```

## マージ
``` pd.merge(leftdf, rightdf, on='key') ```

## グループ
### グルーピング
カラム名（列名）でグルーピング。　```  df.groupby('class') ```



## 分析

### データ数
``` df.groupedby('hoge').count()```
### 平均値
``` df.groupedby('hoge').mean()```


## ロード・セーブ
### picle
``` df.to_pickle(ファイル名) ```


### excel
``` df.to_excel({ファイル名}, sheet_name={シート名}) ``` ファイル名は *.xlsx
