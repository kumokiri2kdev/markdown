# 初期化あれこれ

## 構造体
###サンプルの構造体

```go
type Horse struct {
	Name string
	Age int
}
```


###初期化方法1

```go
a := Horse{}
a.Name = "Admire Deus"
a.Age = 5
```

###初期化方法2

```go
b := Horse{"Kitasan Episode", 7}
```
メンバの上から順に値が設定される。

###初期化方法3

```go
c := Horse{Age : 6, Name : "Agea"}
```
明示的に、メンバーを指定して初期値を設定

###初期化方法4

```go
d := Horse{Name : "Informer"}
```
一部のメンバーのみ指定  
  
###初期化方法5
new を使用すると、ゼロ初期化された状態で生成される。

```go
horse := new(Horse)
	
fmt.Println("Age : ", horse.Age)
fmt.Println("Name : ", horse.Name)	

```
```
Age :  0
Name :  
```
new で生成されたオブジェクトは、ポインタ。


  

## 埋め込み
### サンプルの埋め込み

```go
type SuperHorse struct {
	Horse
	Title string
}
```

### 初期化方法1
```go
a := SuperHorse{Horse{Name : "Narita Brian", Age : 32}, "Arima Kinen"}
```

### 初期化方法2

```go
b := SuperHorse{Horse : Horse{Name : "Narita Brian", Age : 32}, Title : "Arima Kinen"}
```
メンバの明示的な指定  
埋め込み構造体のメンバIDは、構造体名になる

### 埋め込みメンバーが別パッケージの場合
```go
type SuperHorse struct {
	different.Horse
	Title string
}
```
### 初期化方法
```go
b := SuperHorse{Horse : different.Horse{Name : "Narita Brian", Age : 32}, Title : "Arima Kinen"}
```
タグの方には、パッケージ名はつけない。


