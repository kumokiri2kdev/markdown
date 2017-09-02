# urllib

python3 では、urllib.request を使用して、url request を発行する。

## 最もシンプルな例

```python
import urllib.request

request = urllib.request.Request('http://jra.jp/')

with urllib.request.urlopen(request) as response:
	response_body = response.read().decode("'shift_jis'")
	print(response_body)
	
```


