
## データ読み込み

``` Python
domain = 'https://archive.ics.uci.edu'
path = '/ml/machine-learning-databases/adult/'
file = 'adult.data'

df = pd.read_csv(domain + path + file, header=None, skipinitialspace=True)

col_name = ['age','workclass','fnlwgt','education','education.num','marital.status','occupation','relationship','race','sex','capital.gain','capital.loss','hours.per.week','native.country','income']
df.columns = col_name

df.iloc[25:28]
```

```
    age  workclass  fnlwgt     education  ...  capital.loss hours.per.week native.country income
25   56  Local-gov  216851     Bachelors  ...             0             40  United-States   >50K
26   19    Private  168294       HS-grad  ...             0             40  United-States  <=50K
27   54          ?  180211  Some-college  ...             0             60          South   >50K
```

NaN が ? になっているので、read_csv の時点で、NaN に変換する様にする。

``` Python
df = pd.read_csv(domain + path + file, header=None, skipinitialspace=True, na_values='?')
df.columns = col_name

df.iloc[25:28]
```
```
    age  workclass  fnlwgt     education  ...  capital.loss hours.per.week native.country income
25   56  Local-gov  216851     Bachelors  ...             0             40  United-States   >50K
26   19    Private  168294       HS-grad  ...             0             40  United-States  <=50K
27   54        NaN  180211  Some-college  ...             0             60          South   >50K
```

使用しない column を削除。

``` Python
df = df.drop(columns = ['fnlwgt', 'relationship', 'race', 'capital.gain','capital.loss', 'native.country'])
```

データの shape

``` Python
df.shape
```
```
(32561, 9)
```
## データ表示

### descripbe メソッドで、年齢の要約統計量を表示

``` Python
df['age'].describe()
```
```
count    32561.000000
mean        38.581647
std         13.640433
min         17.000000
25%         28.000000
50%         37.000000
75%         48.000000
max         90.000000
Name: age, dtype: float64
```
文字列を含む列の場合、別の表示になる。

``` Python
df[['education', 'workclass']].describe()
```
```
       education workclass
count      32561     30725
unique        16         8
top      HS-grad   Private
freq       10501     22696
```

### 分布（データの個数)

``` Python
df['education'].value_counts()
```

```
HS-grad         10501
Some-college     7291
Bachelors        5355
Masters          1723
Assoc-voc        1382
11th             1175
Assoc-acdm       1067
10th              933
7th-8th           646
Prof-school       576
9th               514
12th              433
Doctorate         413
5th-6th           333
1st-4th           168
Preschool          51
Name: education, dtype: int64
```

## データ参照
0 ~ 2 行目の age と workclass を表示。

```Python
df.loc[0:2, ['age', 'workclass']]
```

```
   age         workclass
0   39         State-gov
1   50  Self-emp-not-inc
2   38           Private
```


### 行100〜102の全カラムを表示
```Python
df.iloc[100: 103, :]
```
```
age         workclass  education  education.num      marital.status       occupation     sex  hours.per.week income
100   76           Private    Masters             14  Married-civ-spouse  Exec-managerial    Male              40   >50K
101   44           Private  Bachelors             13  Married-civ-spouse  Exec-managerial    Male              60   >50K
102   47  Self-emp-not-inc    Masters             14       Never-married   Prof-specialty  Female              50  <=50K
```

### データ数の確認
``` Python
df[df['sex'] == 'Male'].shape
df[df['sex'] == 'Female'].shape
```
```
(21790, 9)
(10771, 9)
```

### 男性の年齢の要約統計量
``` Python
df[df['sex'] == 'Male']['age'].describe()
```

```
count    21790.000000
mean        39.433547
std         13.370630
min         17.000000
25%         29.000000
50%         38.000000
75%         48.000000
max         90.000000
Name: age, dtype: float64
```

### 年齢で並び替え
``` Python
 df.sort_values(by='age')
```
```
       age         workclass     education  education.num      marital.status       occupation     sex  hours.per.week income
12318   17           Private          11th              7       Never-married            Sales  Female               8  <=50K
6312    17           Private          11th              7       Never-married            Sales    Male              15  <=50K
30927   17           Private          11th              7       Never-married    Other-service    Male              17  <=50K
12787   17         Local-gov          11th              7       Never-married     Adm-clerical  Female              15  <=50K
25755   17               NaN          11th              7       Never-married              NaN    Male              10  <=50K
...    ...               ...           ...            ...                 ...              ...     ...             ...    ...
24043   90  Self-emp-not-inc       HS-grad              9       Never-married  Exec-managerial    Male              12  <=50K
32277   90           Private       HS-grad              9             Widowed     Adm-clerical  Female              25  <=50K
5104    90           Private  Some-college             10       Never-married    Other-service    Male              35  <=50K
8963    90               NaN       HS-grad              9             Widowed              NaN  Female              40  <=50K
10210   90  Self-emp-not-inc  Some-college             10  Married-civ-spouse  Farming-fishing    Male              40  <=50K
```

### 複数カラムで並び替え

``` Python
df.sort_values(by=['age', 'education.num'])
```
```
       age  workclass    education  education.num      marital.status       occupation     sex  hours.per.week income
335     17    Private      5th-6th              3       Never-married    Other-service    Male              48  <=50K
9971    17    Private      7th-8th              4       Never-married     Craft-repair    Male              45  <=50K
17474   17    Private      7th-8th              4       Never-married  Farming-fishing    Male              40  <=50K
28770   17    Private      7th-8th              4       Never-married            Sales    Male               8  <=50K
271     17    Private          9th              5       Never-married    Other-service    Male              24  <=50K
...    ...        ...          ...            ...                 ...              ...     ...             ...    ...
5370    90  Local-gov      Masters             14  Married-civ-spouse  Exec-managerial    Male              60   >50K
5406    90    Private      Masters             14       Never-married  Exec-managerial    Male              50   >50K
18832   90    Private      Masters             14       Never-married  Exec-managerial  Female              40  <=50K
20610   90    Private      Masters             14  Married-civ-spouse   Prof-specialty  Female              40   >50K
8806    90    Private  Prof-school             15  Married-civ-spouse   Prof-specialty    Male              72   >50K
```

## 欠損値処理

### 欠損のある column の確認
``` Python
df.isna().any(axis=0)
```
```
age               False
workclass          True
education         False
education.num     False
marital.status    False
occupation         True
sex               False
hours.per.week    False
income            False
dtype: bool
```

### 欠損の個数を確認
``` python
df.isna().sum(axis=0)
```
```
age                  0
workclass         1836
education            0
education.num        0
marital.status       0
occupation        1843
sex                  0
hours.per.week       0
income               0
dtype: int64
```

### 欠損のある行を取り除く
``` Python
df = df.dropna()
df.isna().sum(axis=0)
```
```
age               0
workclass         0
education         0
education.num     0
marital.status    0
occupation        0
sex               0
hours.per.week    0
income            0
dtype: int64
```

## グループ化
性別でグループ化
``` Python
grouped = df.groupby('sex')
grouped.mean()
```
```
        age  education.num  hours.per.week
sex                                             
Female  36.884995      10.102719       36.955287
Male    39.188089      10.143496       42.857177
```

``` Python
grouped = df.groupby('workclass')
grouped['hours.per.week'].mean()
```
```
workclass
Federal-gov         41.379167
Local-gov           40.982800
Private             40.267096
Self-emp-inc        48.818100
Self-emp-not-inc    44.421881
State-gov           39.031587
Without-pay         32.714286
Name: hours.per.week, dtype: float64
```
複数カラムでグループ化
```
grouped = df.groupby(['sex', 'workclass'])
grouped['hours.per.week'].mean()
```
```
sex     workclass       
Female  Federal-gov         40.009524
        Local-gov           39.252695
        Private             36.500000
        Self-emp-inc        42.985185
        Self-emp-not-inc    36.573935
        State-gov           37.008180
        Without-pay         29.200000
Male    Federal-gov         42.048062
        Local-gov           42.131161
        Private             42.221226
        Self-emp-inc        49.620795
        Self-emp-not-inc    45.883754
        State-gov           40.254635
        Without-pay         34.666667
Name: hours.per.week, dtype: float64
```

## データマージ
``` Python
grouped  = df.groupby('workclass')
workclass_hours = pd.DataFrame(grouped['hours.per.week'].mean()

print(workclass_hours)

merged = df.merge(workclass_hours, left_on='workclass', right_index=True, suffixes=('', '_avg'))

print(merged[['workclass', 'hours.per.week', 'hours.per.week_avg']])

```
```
                  hours.per.week
workclass                       
Federal-gov            41.379167
Local-gov              40.982800
Private                40.267096
Self-emp-inc           48.818100
Self-emp-not-inc       44.421881
State-gov              39.031587
Without-pay            32.714286

         workclass  hours.per.week  hours.per.week_avg
0        State-gov              40           39.031587
11       State-gov              40           39.031587
34       State-gov              15           39.031587
48       State-gov              40           39.031587
123      State-gov              50           39.031587
...            ...             ...                 ...
25500  Without-pay              65           32.714286
27747  Without-pay              55           32.714286
28829  Without-pay              25           32.714286
29158  Without-pay              12           32.714286
32262  Without-pay              16           32.714286

```

## データの可視化
### 棒グラフ

``` Python
merged['marital.status'].value_counts().plot(kind='bar')
```
![棒グラフ]('./img/Figure_04_01.png')


### 円グラフ
``` Python
merged['workclass'].value_counts().plot(kind='pie', figsize=(4,4))
```
![棒グラフ]('./img/Figure_04_02.png')

### ヒストグラム

``` Python
merged['education.num'].plot(kind='hist', bins=15)
```
![棒グラフ]('./img/Figure_04_03.png')
