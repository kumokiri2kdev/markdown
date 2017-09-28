# EC2

## Amazon Linux

### OSX ターミナルからのログイン

ログイン用の鍵のパーミッション設定

```
sudo chmod 400 ~/.ssh/AMI-Linux.pem 
```
ssh ログイン

```
ssh -i $(key_path) ec2-user@ec2-52-199-41-194.ap-northeast-1.compute.amazonaws.com
```

鍵は、フルパスで指定。
ユーザー名は、`ec2-user`。

## Ubuntu
### ログイン
ログインは、Amazon Linux とほぼ同じ。
ユーザー名のみを `ubuntu` に変更。





