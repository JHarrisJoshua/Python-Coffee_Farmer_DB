# Coffee Farmer's Almanac

## Table of Contents
* [Overview](#Overview)
* [Web App](#Web-App)
* [ERD](#ERD)


## Overview
### Description
A web application that facilitates the CRUD operations for a database from the perspective of a database administrator (i.e. non-client facing).
The database represents information about the farming and cultivation of genetic varieties of coffee and the agricultural conditions of various coffee-growing regions. The database is intended to enable coffee farmers to select plants based on their region and specific challenges, from pests to climate conditions.

## Web App
### Heroku
The application was hosted on Heroku. RIP Heroku free tier. If I get time I plan on migrating the project. I plan on spiking a few free-tier providers to see which I like best.  

<!--- 
https://coffee-farmers-almanac.herokuapp.com/

// Note that Heroku puts the app to sleep after 30 minutes of inactivity. Visiting the site will load the app from sleep, which results in noticeable lag for the first visit. Subsequent visits will not require booting the app. There are ways to mitigate this, and in production, the app would be run on a higher service tier.
--->

### Framework
The app is implemented using Python, Flask, and SQL. While the database was originally housed in MariaDB(an open-source fork of MySQL), the database was migrated to PostgreSQL for deployment on Heroku. The data was also stored and tested locally using MySQL.   

## ERD

The following relationship diagram was created using MySQL Workbench (Database > Reverse Engineer...). For purposes of hosting on Heroku, the database was migrated to PostgreSQL.

![image](https://user-images.githubusercontent.com/81477294/173967204-1e267163-f0ee-43de-8b41-870a50c8fde2.png)
