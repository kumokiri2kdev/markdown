# Datatables

## Datatables
[Datatables](https://datatables.net/)

## 導入
jQuery 1.x or 3.x が必要と思われる。

``` html
<!-- jQuery UI -->
<link rel="stylesheet" type="text/css" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script type="text/javascript" src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

<!-- Datatables -->
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css"/>
<script type="text/javascript" src="https://cdn.datatables.net/v/dt/dt-1.10.16/datatables.min.js"></script>

```

先に jQuery を読み込んで、その後 Datatables を読み込む必要があるらしく、順番を変えるとまともに動作しない。

## 最初のサンプル

``` html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <!-- jQuery UI -->
  <link rel="stylesheet" type="text/css" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  <script type="text/javascript" src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

  <!-- Datatables -->
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css"/>
  <script type="text/javascript" src="https://cdn.datatables.net/v/dt/dt-1.10.16/datatables.min.js"></script>
  <script>
    $(function() {
      $("#foo-table").DataTable();
    });
  </script>
  <title></title>
</head>
<body>
  <table id="foo-table" class="table table-bordered">
    <thead>
        <tr><th>No</th><th>都道府県</th></tr
    </thead>
    <tbody>
      <tr><td>1</td><td>北海道</td></tr>
      <tr><td>2</td><td>青森県</td></tr>
      <tr><td>3</td><td>岩手県</td></tr>
      <tr><td>4</td><td>宮城県</td></tr>
      <tr><td>5</td><td>秋田県</td></tr>
      <tr><td>6</td><td>山形県</td></tr>
      <tr><td>7</td><td>福島県</td></tr>
      <tr><td>8</td><td>茨城県</td></tr>
      <tr><td>9</td><td>栃木県</td></tr>
      <tr><td>10</td><td>群馬県</td></tr>
      <tr><td>47</td><td>沖縄県</td></tr>
      </tbody>

  </table>
</body>
</html>
```

## 

## 日本語化
[DataTablesの使い方](DataTablesの使い方)

## デフォルト設定の無効化
デフォルトでは、

 - 件数切替
 - 検索
 - ソート
 - 情報表示
 - ページング
 
がデフォルトで有効になるので、若干のうっとおしい。

それらを OFF にするには、

``` javascript
$("#foo-table").DataTable({
    // 件数切替機能 無効
    lengthChange: false,
    // 検索機能 無効
    searching: false,
    // ソート機能 無効
    ordering: false,
    // 情報表示 無効
    info: false,
    // ページング機能 無効
    paging: false
});
```

とする。

## select event
公式ドキュメントの select イベントに関しては、動作させることができていない。
他のサンプルとして、

``` javascript
$('#foo-table tbody').on("click", "tr", function(){
	var data = $('#foo-table').dataTable().fnGetData(this);
	$(this).toggleClass('selected');
      console.log(data);
});
```

## class='display'
table にこのクラスを設定するしておくと、テーブルの行の色が互い違いになってくれる。
ただし、dataTable() をするテーブルはクラスではなく id で指定しなければいけない。





