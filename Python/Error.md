# Error

## 全ての例外を処理

``` python
try:
    num = int("")
except:
    print("error")
```

```
error
```

## Error を raise する

``` python
def invoke_error():
    try:
        num = int("")
    except:
        print("error")
        raise

try :
    invoke_error()
except:
    print("The function raises error")
```

```
error
The function raises error
```

