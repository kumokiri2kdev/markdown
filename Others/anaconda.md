# anaconda

## ダウンロード

[anacondaのダウンロードページ](!https://www.anaconda.com/download/) からダウンロード。

### AWS - Ubuntu
anaconda のページのダウンロードのリンクを取得し、シェルスクリプトをダウンロード。

``` 
$ mkdir anaconda
$ cd anaconda/
$ wget https://repo.continuum.io/archive/Anaconda3-5.0.0-Linux-x86_64.sh
```
シェルスクリプトを実行。

```
$ ./Anaconda3-5.0.0-Linux-x86_64.sh 
Please answer 'yes' or 'no':'
>>> yes
>>> 
>>> Do you wish the installer to prepend the Anaconda3 install location
to PATH in your /home/ubuntu/.bashrc ? [yes|no]
[no] >>> yes

Thank you for installing Anaconda3!

$ source ~/.bashrc

a$ python -V
Python 3.6.2 :: Anaconda, Inc.

```

```
Python 3.6.2 :: Anaconda, Inc.
```

