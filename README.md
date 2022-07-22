# Coffee Farmer's Almanac

## Table of Contents
* [Overview](#Overview)
* [Web App](#Web-App)
* [ERD](#ERD)


## Overview
### Description
A web application that facilitates the CRUD operations for the coffee farmer's almanac from the perspective of a database administrator (i.e. non-client facing).
The database represents information about the farming and cultivation of genetic varieties of coffee and the agricultural conditions of various coffee-growing regions. The database is intended to enable coffee farmers to select plants based on their region and speficic challenges, from pests to climate conditions.

## Web App
### Heroku Link
The application is hosted on Heroku. Use the following link to view the project.
https://coffee-farmers-almanac.herokuapp.com/regions-varieties/

### Framework
The app is implemented using Python, Flask, and SQL. While the database was originally housed in MariaDB(an open-source fork of MySQL), the database was migrated to PostgreSQL for deployment on Heroku. The data was also stored and tested locally using MySQL.   

## ERD

While the database was originally house in MariaDB, it was also stored locally using MySQL. The following relationship diagram was created using MySQL Workbench. For purposes of hosting on Heroku, the database was migrated to PostgreSQL.

![image](https://user-images.githubusercontent.com/81477294/173967204-1e267163-f0ee-43de-8b41-870a50c8fde2.png)
