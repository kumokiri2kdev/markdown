# jQuery

## 導入
### jQuery のロード
``` html
<head>
	<script src="js/jquery-2.1.4.min.js"></script>
	<script src="js/script.js"></script>     
</head>
```
自前のロジック（script.js）は必ず、jQuery（jquery-2.1.4.min.js）のあとにロードすること。

下記のように、jQuery のサイトからロードでも良い。

``` html
<script src='https://code.jquery.com/jquery-2.1.4.min.js'></script>
```

### HTMLの読み込み完了

``` javascript
<script type="text/javascript">
  $(function() {

  });
<script>
```

``` javascript
$(document).ready(function) {

});
```

上記は、どちらも同じ意味となり、この中にコードを書いておくとHTMLの読み込みが完了してからコードが動作し始める。


## dataset IDL属性

### querySelectorAll()
document に対してだけ有効。

```html
    <ul id="Sample">
      <li data-custom-id="kita" data-grade=5>キタサンブラック</li>
      <li data-custom-id="mo-mo" data-grade=3>モーリス</li>
      <li data-custom-id="shonan">ショウナンマルシェ</li>
      <li data-custom-id="jyoru">ジョルジュサンク</li>
      <li data-custom-id="lay">レイデオロ</li>
    </ul>
```

``` javascript
var grade = document.querySelectorAll('[data-grade]');
console.log(grade);
```



参考
http://dresscording.com/blog/html5/custom_data_attribute.html






