# AWS SDK

## boto3 のインストール
Boto は、AWS SDK for Python。

[Boto 3](https://boto3.readthedocs.io/en/latest/)

```
sudo pip install boto3
```

## S3

### S3 からダウンロード
S3 からダウンロードし、ファイルには落とさずに、直接オンメモリで取り扱う。

``` python
import json
import boto3

BUCKET_NAME = 'mybucket'
FILE_NAME = 'myfile.json'

s3 = boto3.resource('s3')
obj = s3.Object(BUCKET_NAME, FILE_NAME)   
response = obj.get()
body = response['Body'].read()
json_data = json.loads(body.decode('utf-8'))

print(json_data)
```

```
$ python s3sandbox.py 
{'girls': [{'name': 'kurara', 'shop': 'Kawasaki Premium', 'id': '350'}, {'name': 'shiina', 'shop': 'Kawasaki Celeb', 'id': '239'}]}
```

### S3 へアップロード

``` python
import json
import boto3

BUCKET_NAME = 'mybucket'
FILE_NAME = 'myfile.json'

s3 = boto3.resource('s3')
obj = s3.Object(BUCKET_NAME, FILE_NAME)   

obj.put(Body = json.dumps(" {'test' : 'テスト'} ", ensure_ascii=False,))
```
アップロードされたファイル
``` 
" {'test' : 'テスト'} "
```

ensure_ascii=False がないと、エスケープされる。
(pythonでjsonを扱う時、日本語をエスケープさせない方法)[http://qiita.com/tadokoro/items/131268c9a0fd1cf85bf4]

putをすると、既存のオブジェクトに上書きしたとしても、既存のアクセス権限がリセットされてしまうので、明示的に指定が必要。

``` python
response = object.put(
    ACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
```



## 参考
[Python(boto3)でS3にデータをファイル保存せず直接アップロードする方法](http://dev.classmethod.jp/cloud/aws/upload-json-directry-to-s3-with-python-boto3/)

