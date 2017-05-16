# ReadMe

## Before Running

### 1, Intstall a database
Install a database (I use mariadb which is the same as mysql) and then change database connection string.

The database connection string is in myforest.py change dbconnector='mysql+mysqlconnector://root:root@localhost/randomforst'
 string.

### 2, Install requirements
pip install sklearn numpy SQLAlchemy Flask pandas

### 3, If you do not want to use database and want to speed up the app
Since the requirements need to database support. I write database by pandas Dataframe.
```
   df.to_sql("sample",engine,if_exists='replace')
```

## Running
From command-line:

```
python app.py
```
