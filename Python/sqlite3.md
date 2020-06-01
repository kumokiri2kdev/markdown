# SQLite3

## import

``` python
import sqlite3
```

## connect to a DB
```python
conn = sqlite3.connect('data/db/keiba.sqlite3')
```

## cursor

``` python
cur = conn.cursor()
```

## sql command
``` python
sql_query = 'select distinct date from races;'

cur.execute(sql_query)

list = cur.fetchall()
```

## sample
``` python
import sqlite3


if __name__ == '__main__':
    sql_query = 'select distinct date from races;'


    conn = sqlite3.connect('data/db/keiba.sqlite3')
    cur = conn.cursor()

    cur.execute(sql_query)

    list = cur.fetchall()

    print(list)
```

## SQL Commands
### select
```
select * from races;
```
### distinct
```
select distinct date from races;

```
### delete
```
delete from races;
```
