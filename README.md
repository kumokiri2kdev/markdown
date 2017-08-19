# markdown

## add
```
git add [$changed]

or

git add .
```

## commit
```
git commit -m "XXX"
```

## push
```
git push -u origin master
```

## .DS_Storeの対処
### igore する

```
git config --global core.excludesfile ~/.gitignore_global
vi /Users/seiichikataoka/.gitignore_global
```

gitignore_global  

```
.DS_Store
```

[グローバルで.gitignoreを適応する](http://qiita.com/katsew/items/5cade12fa743a2f31f25)

### rm 

git rm -r .DS_Store 

