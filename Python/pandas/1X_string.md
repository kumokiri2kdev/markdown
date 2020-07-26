# 文字列

## シリーズデータを分割してデータフレームにする
``` Python
ser = pd.Series([
  '2年1組 山田君',
  '2-1 高橋君君',
  '2年3組 佐藤君',
  '2-4 内山君'
])

df = ser.str.split(' ', expand=True)

df.columns=['class', 'name']
```
```
    class  name
0  2年1組   山田君
1   2-1  高橋君君
2  2年3組   佐藤君
3   2-4   内山君
```

## 文字列の置換

``` Python
df['class'] = df['class'].str.replace(pat='年',repl='-')
df['class'] = df['class'].str.replace(pat='組',repl='')
```

```
   class  name
0   2-1   山田君
1   2-1  高橋君君
2   2-3   佐藤君
3   2-4   内山君
```

### 正規表現

``` python
df['コース'].unique()

```
```                                                   
array(['ダート', '芝・右 外', '芝・左', '芝・右', '芝・左 外', '芝・直'], dtype=object)
```

``` python
df['コース'] = df['コース'].str.replace(pat='・.*', repl='')

df['コース'].unique()  
```
```
array(['ダート', '芝'], dtype=object)
```
