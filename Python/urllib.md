# urllib

python3 では、urllib.request を使用して、url request を発行する。

## urllib.request

### get
以下は、JRAのトップページへリクエストサンプル。

``` python
import urllib.request

request = urllib.request.Request('http://jra.jp/')

with urllib.request.urlopen(request) as response:
	response_body = response.read().decode("'shift_jis'")
	print(response_body)

```
### post
post のサンプル。

``` python
import urllib.request
 
str = 'cname=pw15oli00/6D'
data = str.encode('utf-8')
 
url = 'http://jra.jp/JRADB/accessO.html'
 
request = urllib.request.Request(url, data=data, method='POST')

with urllib.request.urlopen(request) as response:
	response_body = response.read().decode("'shift_jis'")
	print(response_body)
```
### User-Agent の変更
User Agent に限らず、何かのヘッダを追加する場合は、Request 設定時に指定する。

``` python
request = urllib.request.Request(url, 
	data=data, 
	method='POST',
	headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    	}
	)
```



