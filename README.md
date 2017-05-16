# ReadMe

## Before Running

### 1, Intstall a database
Install a database (I use mariadb which is the same as mysql) and then change database connection string.

The database connection string is in myforest.py change
```
dbconnector='mysql+mysqlconnector://root:root@localhost/randomforst'
 string.
```
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

## Answer:

### Question 1: Briefly explain how would you develop this workflow using AWS if tables 1 and 2 had over 1 mill records and over 500 columns. How would this higher dimension impact the design of the Web app?
if table 1 and table 2 have mill records I will do:

#### 1, divide the records into training set and testing set.
#### 2, normalization the columns I mean I will use [1,-1] to zoom out or zoom in the every columns
#### 3, use Covariance and Correlation
Using [correlation coefficient](http://www.math.uah.edu/stat/expect/Covariance.html)
array and filter the correlation rate  more than 95%
delete the duplicate columns

#### 4, use the [principal component analysis,PCA](https://en.wikipedia.org/wiki/Principal_component_analysis) method to find the largest eigenvector in Covariance, and regard corresponding columns as main columns using this method to select around about 10-20 columns and build the random forest by these columns.

### Question 2: What would you have to do if you want the application to be HIPAA compliant? (That is compliant with the US Health Insurance Portability and Accountability Act)

1,Control use regulated data internally and how information expose externally.

2,Manage data security and risk with formal HIPAA policies and internal controls.

3,Identify and log the data visiting and data using CQRS, event sourcing to not only record the data, but also record who and when
do what kind of operation in Data.

4,require Aptible customers to force SSL/TLS

5, Build and use log analysis tools

6, security audit for downstream entity.
