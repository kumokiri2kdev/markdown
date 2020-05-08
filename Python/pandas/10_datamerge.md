# 連結とマージ
## 連結
### concat

``` Python
df1 = pd.DataFrame({
  'a':['a0', 'a1', 'a2'],
  'b':['b0', 'b1', 'b2'],
  'c':['c0', 'c1', 'c2'] })                                                                           

df2 = pd.DataFrame([
  ['a3', 'a4', 'a5'],
  ['b3', 'b4', 'b5'],
  ['c3', 'c4', 'c5']], columns=list('abc'))                                                         

pd.concat([df1, df2],axis=0)                                         
```

```
    a   b   c
0  a0  b0  c0
1  a1  b1  c1
2  a2  b2  c2
0  a3  a4  a5
1  b3  b4  b5
2  c3  c4  c5
```

ignore_index を指定すると、インデックスが再付与される。

### append
行の追加であれば、append でも同様の動作が可能。


## マージ
マージは、二つのデータフレームの同一キーを基にデータを連結する動作。


``` Python
leftdf = pd.DataFrame({
  'key': ['k0', 'k1', 'k2'],
  'a': ['a0', 'a1', 'a2'],
  'b': ['b0', 'b1', 'b2']
})      

rightdf = pd.DataFrame({
  'key': ['k1', 'k2', 'k0'],
  'c':['c1', 'c2', 'c0'],
  'd':['d1', 'd2', 'd0']
})

pd.merge(leftdf, rightdf, on='key')      
```

```
  key   a   b   c   d
0  k0  a0  b0  c0  d0
1  k1  a1  b1  c1  d1
2  k2  a2  b2  c2  d2
```
