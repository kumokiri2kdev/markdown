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




## 参考

[PythonとBeautiful Soupでスクレイピング](http://qiita.com/itkr/items/513318a9b5b92bd56185)  
[BeautifulSoup Documents](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


