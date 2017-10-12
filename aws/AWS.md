# AWS

## aws cli

### インストール
```
$ pip install awscli
```

## aws configure
```
aws configure
```

- region : ap-northeast-1 (東京)
- output format : None でいいみたい


[AWS Configure](http://docs.aws.amazon.com/cli/latest/reference/configure/)


## s3 

### フォルダ内のファイルを一括ダウンロード

``` ws s3 cp s3:$(SOURCE_PATH) $(DEST_PATH) --recursive --include "*.ext"```

```
aws s3 cp s3://jradatabucket/tmp/20171008/京都/01/win/ ./dir/ --recursive --include "*.json"
```



