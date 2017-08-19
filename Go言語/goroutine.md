# goroutine

## gorutineの生成
### 1)埋め込み関数

```go
go func(){
	hogehoge
}()

```
関数の後に、( )をつけるのを忘れずに。 

### 2)関数呼び出し

``` go
func sub() {
	hogehoge
}
go sub()
```

### (1) と (2) の差分
(1) の場合、呼び出し元のスコープにある変数なら直接アクセス可能。
(2) の場合は、明示的に関数パラメーターとして渡してあげる必要性がある。

## 同期
### channel を使う場合

``` go
func main() {
	fmt.Println("Hello Channel")
	
	c := make(chan struct{})
	
	go func(){
		for i := 1; i <= 100; i++ {
	        fmt.Println(i)
	        time.Sleep(500 * time.Millisecond)
	    }
	    c <- struct{}{}
	}()

	<-c
	
	fmt.Println("Fin")
}

```
### waitgroup を使用する場合
```
func sub(start int, wg *sync.WaitGroup) {
	for i := start; i <= 100; i++ {
	    fmt.Println(i)
	    time.Sleep(500 * time.Millisecond)
	}
	
	wg.Done()
}

func main() {
	fmt.Println("Hello Channel")
	
	var wg sync.WaitGroup
	
	wg.Add(2)
	
	go sub(10, &wg)
	go sub(20, &wg)
	
	wg.Wait()
	
	fmt.Println("Fin")
}
```
waitgroup の方が、複数の同期を取る場合は使いやすい。  
ただし、channel でも複数の同期は取れる。







