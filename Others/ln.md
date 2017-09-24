# ln コマンド

## シンボリックリンクの作成

```
ln -s source dest
```
source に対するシンボリックリンク dest を作成する。
つまり、dest は、source を指し示す。

### シンボリックリンクの更新

```
ln -nfs source dest
```

### シンボリックリンクの削除
```
rm dest
```
シンボリックリンクのみが削除され、source は削除されずに残る。

