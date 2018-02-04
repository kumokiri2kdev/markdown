# Differ - jQuery

# 基本的な使い方

## promise() の実行
``` html
<!DOCTYPE html>
<html>
  <head>
    <script src='https://code.jquery.com/jquery-2.1.4.min.js'></script>
    <script type="text/javascript">
      $(function() {
        var d = new $.Deferred();
        d.promise().done(function() {
          console.log('hoge');
        });
        d.resolve();
      });
    </script>
  </head>
</html>
```

```
hoge
```

## メソッドチェーン
下記のように、メソッドを数珠つなぎにできる。

``` javascript
d.promise().done(function() {
  console.log('hoge');
}).done(function() {
  console.log('fuga');
});
```

## チェーンするメソッド
基本的な使い方としては、

 - done
 - faile
 - then

の三つがあり、done は成功時のメソッド、fail は失敗時、then は成功と失敗の両方のメソッドを取ることができる。

``` javascript
var d = new $.Deferred();
d.promise().then(function() {
  console.log('hoge');
}, function() {
  console.log('fuga');
});
d.resolve();
d.reject();
```

上記の then では、 成功時は  `hoge` が出力され、失敗時には `fuga` が出力される。

## 成功と失敗
成功時には、Deferred の resolve() を呼ぶ。
失敗時には、Deferred の reject() を呼ぶ。

resolveWith/rejectWith というのもそれぞれある。


## 関数へのパラメーター
関数のパラメーターは、resolve/reject へ渡すパラメーターがそのまま渡される。

``` javascript
  $(function() {
    var d = new $.Deferred();

    d.promise().done(function(val) {
      console.log('hoge : ' + val );
    };

    d.resolve("test");
  });
```

## Promise を返す実装パターン
``` javascript
$(function() {
  function getPromise() {
    var d = new $.Deferred();
    d.resolve();
    return d.promise();
  }
                
  getPromise().done(function() {
    console.log("Hoge");
  });
});
```
resolve の後に then を設定している感じもするが、この例でも then は実行される。

```
Hoge
```

## Deffered 自体と promise オブジェクト

Deffered にも promise をブジェクト自体にも メソッドを設定できる。
ただし、resolve()/reject() などは、Deffered のみに設定できるものになっいる。






# サンプル
## Deferred のサンプル
promise() 自体を使わないサンプル。

``` html
<!DOCTYPE html>
<html>
  <head>
    <script src='https://code.jquery.com/jquery-2.1.4.min.js'></script>
    <script type="text/javascript">
      $(function() {
        function createDeferred(){
          var df = $.Deferred();
          var output = $("#output");

          df.then( function(arg) {
            $("#output").append("<li>Success callback called. parameters are  [" + arg + "]</li>");
          }, function(arg) {
            $("#output").append("<li>Faile callback called. parameters [" + arg + "]</li>");
          }).done(function(arg) {
            $("#output").append("<li>Another success callback</li>");
          }).always(function(arg) {
            $("#output").append("<li>Called always</li>");
          });
          return df;
        }
      
        $("#btnResolve").click(function() {
          console.log("btnResolve");
          var df = createDeferred();
          df.resolve("Success");
        });
        $("#btnReject").click(function() {
          console.log("btnReject");
          var df = createDeferred();
          df.reject("Failed");
        });
      });
    </script>
  </head>
  <body>
    <p>
      <button type="button" id="btnResolve">Resolve</button>
      <button type="button" id="btnReject">Reject</button>
    </p>
    <ul id="output"></ul>
  </body>
</html>
```

