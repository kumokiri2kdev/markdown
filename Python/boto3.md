# boto3

## 参考
[boto3](https://boto3.readthedocs.io/en/latest/index.html)

## client の生成

### 環境変数から AWS Key を使用する

確認はできていないが、aws configure で設定した asw key 等を使って動作している様子。

```
import boto3
cloud_watch = boto3.client('events')
```

### 明示的に aws key を指定
``` python
from boto3.session import Session
import os
 
accesskey = os.environ.get("AWS_ACCESS_KEY_ID")
secretkey = os.environ.get("AWS_SECRET_ACCESS_KEY")
region    = os.environ.get("AWS_DEFAULT_REGION")
 
session = Session(aws_access_key_id=accesskey,
                  aws_secret_access_key=secretkey,
                  region_name=region)
 
cloud_watch = session.client('events')

```

この例だと、環境変数から aws key とかを持ってきているが、このようにして明示的に指定することも可能。

## CloudWatchEvents

### ルールリストの取得
``` python
import boto3
cloud_watch = boto3.client('events')
rule = response = cloud_watch.list_rules()

print(rule)
```

### ルールの Enable/Disable
``` python
import boto3
import os

cloud_watch = boto3.client('events')

response = cloud_watch.describe_rule(Name='ratetest')
print("{} is {}".format(response['Name'], response['State']))

if response['State'] == 'ENABLED':
	cloud_watch.disable_rule(Name='ratetest')
else:
	cloud_watch.enable_rule(Name='ratetest')	

response = cloud_watch.describe_rule(Name='ratetest')
print("{} state is changed to {}".format(response['Name'], response['State']))
```

## s3

### バケッドの一覧
``` python
import boto3
import sys

client = boto3.client('s3')

response = client.list_buckets()

if response['ResponseMetadata']['HTTPStatusCode'] != 200:
    print("Response Error")
    sys.exit(1)

for bucket in response['Buckets']:
    print("Bucket Name : {}".format(bucket['Name']))
```
```
Bucket Name : girldscheule
Bucket Name : girlsscheduledata
```

### objectリストの取得

``` python
import boto3

BACKET_NAME = 'jradatabucket'
PREFIX = 'aa'

client = boto3.client('s3')

response = client.list_objects(
    Bucket= BACKET_NAME,
    Prefix=PREFIX
)

for content in response['Contents']:
    print("Name : {}".format(content['Key']))
```

```
Name : aaa
Name : aac/
Name : aac/fdsa/
Name : aad/
```



### バケッド以下にフォルダを作成
``` python
import boto3

BACKET_NAME = 'hoge'
FOLDER_NAME = 'hoge_hoge/'

s3 = boto3.resource('s3')
bucket = s3.Bucket(BACKET_NAME)

bucket.put_object(Key=FOLDER_NAME)
```

Key に 指定する文字列の最後を '/' にすることが重要。
付いていないと単にファイルが作られる。

### バゲッド・フォルダへのオブジェクトアップロード

``` python
wobj = s3.Object(BACKET_NAME, key)
wobj.put(Body = json.dumps(output, ensure_ascii=False))
```
key が aaa/bbb.json のようになっていれば、ファイルが、バゲットの下のフォルダ aaa の下に bbb.json として置かれる。


### 参考
[CloudWatchEvents](https://boto3.readthedocs.io/en/latest/reference/services/events.html)


## EC2

### EC2 instance 一覧

``` python
ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
	print(i.state)
```

```
{'Code': 80, 'Name': 'stopped'}
{'Code': 80, 'Name': 'stopped'}
```

### 特定 instance の状態表示

``` python
ec2 = boto3.resource('ec2')

instance = ec2.Instance('i-0b8b22ecf7e7f4415')
print(instance.state)
```

```
{'Code': 80, 'Name': 'stopped'}
```

### 特定インスタンスの起動

``` python
ec2 = boto3.resource('ec2')

instance = ec2.Instance('i-0b8b22ecf7e7f4415')
instance.start()
```

```
{'ResponseMetadata': {'HTTPHeaders': {'content-type': 'text/xml;charset=UTF-8',
   'date': 'Thu, 28 Sep 2017 12:43:25 GMT',
   'server': 'AmazonEC2',
   'transfer-encoding': 'chunked',
   'vary': 'Accept-Encoding'},
  'HTTPStatusCode': 200,
  'RequestId': '945e3315-2bc2-47db-b608-5f3008bb0fb3',
  'RetryAttempts': 0},
 'StartingInstances': [{'CurrentState': {'Code': 0, 'Name': 'pending'},
   'InstanceId': 'i-0b8b22ecf7e7f4415',
   'PreviousState': {'Code': 80, 'Name': 'stopped'}}]}

```







