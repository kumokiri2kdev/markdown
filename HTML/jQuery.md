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

### HTMLの読み込み完了

``` javascript
$(function() {

});
```

``` javascript
$(document).ready(function) {

});
```

上記は、どちらも同じ意味となり、この中にコードを書いておくとHTMLの読み込みが完了してからコードが動作し始める。








