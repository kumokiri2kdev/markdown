# Package

## 外部ファイルが、同一のディレクトリにある場合

```python
import class_def as cd

cdi = cd.Class_Sample()
```


## 外部ファイルが直下のサブディレクトリにある場合
``` python
from libdir import class_def as cd

cdi = cd.Class_Sample()
```

## サブディレクトリにあるモジュール間でのインポート

サブディレクトリに

- super_class.py  
- sub_class.py

があり、

``` python:super_class.py
class A():
    def test_func(self):
        print("Super Class Func")
        
    def test(self):
        self.test_func()
```
``` python:sub_class.py
from . import super_class as sc

class B(sc.A):
    def test_func(self):
        print("Sub Class Func")   
    
    def test2(self):
        return super(B, self).test()
        
class C(sc.A):
    def test2(self):
        return super(C, self).test()
```
のように、呼び出す側で、

``` python
from .
```
のように、明示的な相対インポートを使用する。

[Python: 明示的な相対インポートの使い方](http://blog.amedama.jp/entry/2016/05/31/213741)

`__init__.py` は これとは直接的には関係ない。
エンコーディングの指定とか言っている人もいたが、それとも関係ない。
ちなみに、全てのコードが同じディレクトリにあれば、そもそも、気にする必要がないが、たまたまうまく行っていると思った方が良い。
import や from で指定するパスは、実行フォルダからのパス。







