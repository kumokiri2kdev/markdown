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


### 参考
[CloudWatchEvents](https://boto3.readthedocs.io/en/latest/reference/services/events.html)



