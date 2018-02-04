# time

## プログラムの実行

```
$ time sleep 10

real	0m10.027s
user	0m0.001s
sys	0m0.003s

```

## bash コマンドの実行
```
$ time bash -c 'echo test'
test

real	0m0.037s
user	0m0.002s
sys	0m0.004s

```

```
$ time bash -c 'for((i=0;i<10000;i++));do which perl; done >/dev/null'

real	0m27.732s
user	0m9.864s
sys	0m7.863s

```


## 参考
[timeコマンドでプログラムの実行時間を知る](https://qiita.com/tossh/items/659e5934e52b38183200)
