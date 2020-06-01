

## CSV

### Read CSV

ヘッダーもあり、UTF-8 で記述されている場合、ファイル名の指定だけでよい。
```
df = pd.read_csv('2020_comparison.csv')  
```

文字コードの指定が必要な場合。
```` python
df = pd.read_csv('2020_comparison.csv', encoding='SHIFT-JIS')  
````

区切り文字の指定
``` python
df = pd.read_csv('xxxx.csv', sep=';')
```

### Read JSON
``` python
pd.read_json('../data/out5.json', typ='frame')
```
typ は、frame (DataFrame) か series (Series)。
