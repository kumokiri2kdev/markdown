# tabulate

## tabulate について

```tabulate```は、コマンドライン でデータを表形式で表示するライブラリ。


[tabulate](https://pypi.org/project/tabulate/)

## インポート

``` python
from tabulate import tabulate
```

## デフォルト表示

``` Python
table = [
  ["Sun",696000,1989100000],
  ["Earth",6371,5973.6],
  ["Moon",1737,73.5],
  ["Mars",3390,641.85]
]

print(tabulate(table))

```
```
-----  ------  -------------
Sun    696000     1.9891e+09
Earth    6371  5973.6
Moon     1737    73.5
Mars     3390   641.85
-----  ------  -------------
```
これだけでも、数値の位置が調整されているのがわかる。

日本語でも、表示ズレがない。

``` python
table = [
  ['山田　テッド', 310, 11.3],
  ['大山', 255, 5.3],
  ['岡本かーずーま', 298, 31]
]

print(tabulate(table))  
```
```
--------------  ---  ----
山田　テッド      310  11.3
大山            255   5.3
岡本かーずーま    298  31
--------------  ---  ----
```
ここではずれている様に表示されてしまうが、CLI上では揃っている。（フォントの問題と思われる）

## ヘッダの付与
```python
print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))
```
```
Planet      R (km)    mass (x 10^29 kg)
--------  --------  -------------------
Sun         696000           1.9891e+09
Earth         6371        5973.6
Moon          1737          73.5
Mars          3390         641.85
```

## 最初の行を ヘッダにする場合
``` python
table = [
  ["Planet", "R (km)", "mass (x 10^29 kg)"],
  ["Sun",696000,1989100000],
  ["Earth",6371,5973.6],
  ["Moon",1737,73.5],
  ["Mars",3390,641.85]
]  

print(tabulate(table,headers='firstrow'))       
```
```
Planet      R (km)    mass (x 10^29 kg)
--------  --------  -------------------
Sun         696000           1.9891e+09
Earth         6371        5973.6
Moon          1737          73.5
Mars          3390         641.85
```

## dict の キーをヘッダにする
``` python
table = {'Name': ['Alice', 'Bob'],'Age': [24, 19]}

print(tabulate(table, headers='keys'))
```
```
Name      Age
------  -----
Alice      24
Bob        19
```

## テーブルフォーマット

``` python
table = [["spam",42],["eggs",451],["bacon",0]]
headers = ["item", "qty"]
```
### plain
``` python
print(tabulate(table, headers, tablefmt="plain"))
```
```
item      qty
spam       42
eggs      451
bacon       0
```

### simple (default)
``` python
print(tabulate(table, headers, tablefmt="simple"))
```
```
item      qty
------  -----
spam       42
eggs      451
bacon       0
```
### github
``` python
print(tabulate(table, headers, tablefmt="github"))
```
```
| item   |   qty |
|--------|-------|
| spam   |    42 |
| eggs   |   451 |
| bacon  |     0 |
```

### grid
``` python
print(tabulate(table, headers, tablefmt="grid"))
```
```
+--------+-------+
| item   |   qty |
+========+=======+
| spam   |    42 |
+--------+-------+
| eggs   |   451 |
+--------+-------+
| bacon  |     0 |
+--------+-------+
```

### fancy_grid
``` Python
print(tabulate(table, headers, tablefmt="fancy_grid"))
```
```
╒════════╤═══════╕
│ item   │   qty │
╞════════╪═══════╡
│ spam   │    42 │
├────────┼───────┤
│ eggs   │   451 │
├────────┼───────┤
│ bacon  │     0 │
╘════════╧═══════╛
```

### presto
``` python
print(tabulate(table, headers, tablefmt="presto"))
```
```
item   |   qty
--------+-------
spam   |    42
eggs   |   451
bacon  |     0
```

### pretty
``` python
print(tabulate(table, headers, tablefmt="pretty"))
```
```
+-------+-----+
| item  | qty |
+-------+-----+
| spam  | 42  |
| eggs  | 451 |
| bacon |  0  |
+-------+-----+
```

### psql
``` python
print(tabulate(table, headers, tablefmt="psql"))
```
```
+--------+-------+
| item   |   qty |
|--------+-------|
| spam   |    42 |
| eggs   |   451 |
| bacon  |     0 |
+--------+-------+
```

### pipe
``` python
print(tabulate(table, headers, tablefmt="pipe"))
```
```
| item   |   qty |
|:-------|------:|
| spam   |    42 |
| eggs   |   451 |
| bacon  |     0 |
```

### orgtbl
``` python
print(tabulate(table, headers, tablefmt="orgtbl"))
```
```
| item   |   qty |
|--------+-------|
| spam   |    42 |
| eggs   |   451 |
| bacon  |     0 |
```

### jira
``` python
print(tabulate(table, headers, tablefmt="jira"))
```
```
|| item   ||   qty ||
| spam   |    42 |
| eggs   |   451 |
| bacon  |     0 |
```

###  reStructuredText
``` python
print(tabulate(table, headers, tablefmt="rst"))
```
```
======  =====
item      qty
======  =====
spam       42
eggs      451
bacon       0
======  =====
```

### Wikipedia
``` python
print(tabulate(table, headers, tablefmt="mediawiki"))
```
```
{| class="wikitable" style="text-align: left;"
|+ <!-- caption -->
|-
! item   !! align="right"|   qty
|-
| spam   || align="right"|    42
|-
| eggs   || align="right"|   451
|-
| bacon  || align="right"|     0
|}
```

###  MoinMoin

``` python
print(tabulate(table, headers, tablefmt="moinmoin"))
```
```
|| ''' item   ''' ||<style="text-align: right;"> '''   qty ''' ||
||  spam    ||<style="text-align: right;">     42  ||
||  eggs    ||<style="text-align: right;">    451  ||
||  bacon   ||<style="text-align: right;">      0  ||
```

### Youtrack
``` python
print(tabulate(table, headers, tablefmt="youtrack"))
```
```
||  item    ||    qty  ||
|  spam    |     42  |
|  eggs    |    451  |
|  bacon   |      0  |
```

### Textile
``` python
print(tabulate(table, headers, tablefmt="textile"))
```
```
|_.  item   |_.   qty |
|<. spam    |>.    42 |
|<. eggs    |>.   451 |
|<. bacon   |>.     0 |
```

### HTML
``` python
print(tabulate(table, headers, tablefmt="html"))
```
```
<table>
<thead>
<tr><th>item  </th><th style="text-align: right;">  qty</th></tr>
</thead>
<tbody>
<tr><td>spam  </td><td style="text-align: right;">   42</td></tr>
<tr><td>eggs  </td><td style="text-align: right;">  451</td></tr>
<tr><td>bacon </td><td style="text-align: right;">    0</td></tr>
</tbody>
</table>
```
### latex
``` python
print(tabulate(table, headers, tablefmt="latex"))
```
```
\begin{tabular}{lr}
\hline
 item   &   qty \\
\hline
 spam   &    42 \\
 eggs   &   451 \\
 bacon  &     0 \\
\hline
\end{tabular}
```
