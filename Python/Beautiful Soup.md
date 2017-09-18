# Beautiful Soup


## import

``` python
from bs4 import BeautifulSoup
```

## インスタンス生成
``` python
soup = BeautifulSoup(html,"html.parser")
```
２番目の引数の設定が必要かどうかは、環境によるらしい

iMac 上で２番目の引数なしで実行すると

``` python
//anaconda/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 7 of the file ./sandbox.py. To get rid of this warning, change code that looks like this:

 BeautifulSoup([your markup])

to this:

 BeautifulSoup([your markup], "lxml")
```

## タグの検索
``` python
schedule = soup.find("div")
```
### attribute を指定して検索
``` python
schedule = soup.find("div", attrs={"class": "schedule_area"})
```

## find all/siblings/next

``` python
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<div class='cls1'>
<p>p-1-1</p>
<p>p-1-2</p>
<p>p-1-3</p>
</div>
<div class='cls2'>
<p>p-2-1</p>
<p>p-2-2</p>
<p>p-2-3</p>
<b>bold</b>
</div>
<div class='cls3'>
<p>p-3-1</p>
<p>p-3-2</p>
<p>p-3-3</p>
</div>
<div class='cls4'>
<p>p-4-1</p>
<p>p-4-2</p>
<p>p-4-3</p>
</div>
"""

soup = BeautifulSoup(html_doc,"html.parser")

div_class2 = soup.find("div", attrs={"class":"cls2"})
print("<<children>>")
for child in div_class2.children:
    print('"{}"'.format(child))


ps = div_class2.find_all_next("p")
print("<<all next p>>")
print(ps)

ps = div_class2.find_next_siblings("p")
print("<<next siblings p>>")
print(ps)

divs = div_class2.find_next_siblings("div")
print("<<next sigbling div>>")
print(divs)

ps = div_class2.find_all("p")
print("<<find all p in cls2>>")
print(ps)
```
[結果]

```
$ python bssandbox.py 
<<children>>
"
"
"<p>p-2-1</p>"
"
"
"<p>p-2-2</p>"
"
"
"<p>p-2-3</p>"
"
"
"<b>bold</b>"
"
"
<<all next p>>
[<p>p-2-1</p>, <p>p-2-2</p>, <p>p-2-3</p>, <p>p-3-1</p>, <p>p-3-2</p>, <p>p-3-3</p>, <p>p-4-1</p>, <p>p-4-2</p>, <p>p-4-3</p>]
<<next siblings p>>
[]
<<next sigbling div>>
[<div class="cls3">
<p>p-3-1</p>
<p>p-3-2</p>
<p>p-3-3</p>
</div>, <div class="cls4">
<p>p-4-1</p>
<p>p-4-2</p>
<p>p-4-3</p>
</div>]
<<find all p in cls2>>
[<p>p-2-1</p>, <p>p-2-2</p>, <p>p-2-3</p>]
```

## get_text()
element に対して、get_text() を呼ぶと、内部のコンテンツが取得できる。

``` python
html_doc = """
<p>p-1-1</p>
"""

soup = BeautifulSoup(html_doc,"html.parser")

p_element = soup.find("p")
print(p_element.get_text())
```

 
```
$ python bssandbox.py 
p-1-1

```

その element が、子 element を持っている場合、その子 element のテキストも含めて出力される。

``` python
html_doc = """
<p><div>uuu</div>p-1-1</p>
"""

soup = BeautifulSoup(html_doc,"html.parser")

p_element = soup.find("p")
print(p_element.get_text())
```

```
$ python bssandbox.py 
uuup-1-1

```
## attributes の取得
attribute は、メソッドではなく、連想配列から取得する。

``` python
html_doc = """
<p onclick='onclick_attribute'>p-1-1</p>
"""

soup = BeautifulSoup(html_doc,"html.parser")

p_element = soup.find("p")
print(p_element['onclick'])
```

```
$ python bssandbox.py 
onclick_attribute

```
上記のように、連想配列から取得できるが、

``` python
'onclick' in p_element
```
とやってしまうと、判定ができない。  
※常に False が返ってしまう。

存在チェックは

``` python
anchor.has_attr('onclick')
```
とする。



## element の置換

下記の処理で、\<br> を "-" に入れ替わる。

``` python
psb = soup.find("br")
if psb:
	psb.replace_with('-')
```


## 参考

[PythonとBeautiful Soupでスクレイピング](http://qiita.com/itkr/items/513318a9b5b92bd56185)  
[BeautifulSoup Documents](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


