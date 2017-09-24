# datetime

## package import
``` python
from datetime import datetime as dt
```

## 文字列を datetime 化
### yyyy/mm/dd 形式
``` python
date_str = '2017/08/09'
date_time = dt.strptime(date_str, '%Y/%m/%d')

print(date_time)
```

```
2017-08-09 00:00:00
```

### yy/mm/dd 形式
フォーマットを %Y => %y に変更する。

``` python
date_str = '17/08/09'
date_time = dt.strptime(date_str, '%y/%m/%d')

print(date_time)

```
```
2017-08-09 00:00:00
```

### yyyy/mm/dd 00:00 形式
``` python
date_str = '17/08/09 19:01'
date_time = dt.strptime(date_str, '%y/%m/%d %H:%M')

print(date_time)

```
```
2017-08-09 00:00:00
```

## 今日の datetime
``` python
today = dt.datetime.now()

```

## JST で取得する場合
``` python
from pytz import timezone
from datetime import datetime

now = datetime.now()
jst_now = timezone('Asia/Tokyo').localize(now)
```



## 各要素へのアクセス
### 年
``` python
today.year
```

## 計算
### 加算
``` python
date_time = date_time + dt.timedelta(days=3) 
```
### 日数の計算
``` python
from datetime import timedelta

today = date_time.now()
yesterday = today - timedelta(days=-1)

diff = today - yesterday

print(diff.days)
```

```
-1
```
timedelta で指定できるのは

- days
- seconds
- microseconds

のみ。

## timestamp
``` python
print(dt.datetime.now().timestamp())
```
```
1504527253.90865
```








