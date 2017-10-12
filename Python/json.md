# json

## ファイルから読み込み

``` python
with open('kyoto/' + file, 'r') as rfp:
	jsonData = json.load(rfp)
```

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
``` python
with open('test.json','w') as wfp:
	wfp.write(json.dumps(raw_data))
```

## マルチバイトをしようする場合
``` python
raw_data,ensure_ascii=False)
```
