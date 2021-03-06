# Creating Web APIs for CRUD operations for user management

Documentation for creating a Rest API for CRUD operations through SQLite and Swagger

## Prerequisites
- IDE - VScode _(Install VSCode for better experience)_
- OS - RHEL
- Python (3.6.8)
- Flask (1.1.0)
- Werkzeug (0.16.1)
- flask-marshmallow (0.14.0)
- Flask-RESTful (0.3.9)
- flask-restplus (0.13.0)
- Flask-SQLAlchemy (2.5.1)


## Run the API
### [Git Clone](https://github.com/razeev1419/user-management-API.git)
>```$ https://github.com/razeev1419/user-management-API.git```
### Change the directory
>```$ cd user-management-API/```
  - app.py - Source code for API python file
  - test.py - Unitests python file
### Install required packages to run Web API
>```$ pip3 install -r requirement.txt```
 _If this  command fails please install below packages manually_
### Make sure to check for below packages
>```$ pip3 install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy flask-restplus```
### Export before running application
>```$ export FLASK_APP=app.py```
### Create Database
>```$ python
>```Python 3.6.8 (default, Mar 18 2021, 08:58:41)```
>```[GCC 8.4.1 20200928 (Red Hat 8.4.1-1)] on linux```
>```Type "help", "copyright", "credits" or "license" for more information.```
>``` >>> from app import db```
>``` >>> db.create_all()db.create_all()```
### Start running the API
>```$ flask run```
> Check the response at [API](http://localhost:5000)

Hola!! A simple Web API for CRUD operations is created.
test basic scenerios :
- Get all records from database from swagger API
- Add a Hero name to the database
- Update an excisting Hero name
- Delete a record from database

## Unit Tests
Coded basic testcases for the '/get' request 
- testcase1 - Check for response 200
- testcase2 - Check if the content return is application/json
- testcase3 - Check data returned with the expected message
### Run the testcases from VScode / use below command
```$ python test.py```

## Image of API
![API](Images/2021-06-11_21-52.png)
