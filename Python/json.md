# json

## dict から json を出力

``` python
import json

raw_data = {}
raw_data['tag'] = 'myData'
raw_data['value'] = 100

print(json.dumps(raw_data))
```

```
'{"tag": "myData", "value": 100}'
```

## ファイルへ出力

### dict を出力する

``` python
with open ('test.json', 'w') as wfp:
    json.dump(raw_data, wfp)
```

### 文字列化されたデータを出力
``` python
with open('test.json','w') as wfp:
	wfp.write(json.dumps(raw_data))
```
このやり方は、通常の文字列をファイルに出力しているのと同じ。

## ファイルから入力

``` python
with open('tmp/test.json', 'rt') as rfp:
    loaded_data = json.load(rfp)
```
読み込みファイルにマルチバイトが入っていても、上記だけで問題ない。


## マルチバイトを出力しようする場合
``` python
json.dumps(raw_data,ensure_ascii=False)
```
ensure_ascii=False は、ファイル出力時の dmp() でも同様に指定可能。


