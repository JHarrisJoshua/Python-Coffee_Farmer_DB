import re
from flask import Flask, Blueprint, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

# Configuration
db_connection = db.connect_to_database()
countries_view = Blueprint('countries_view', __name__)

# Countries READ
@countries_view.route('/')
def countries():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Countries"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()  
    print(results)  
    return render_template("countries.j2", countries=results)

# Countries CREATE
@countries_view.route('/add', methods=["POST", "GET"])
def countries_add():
    db_connection = db.connect_to_database()
    
    # Render Add Form
    if request.method =="GET":
        return render_template("countries_add.j2")

    # Add a country
    if request.method == "POST":
        if request.form.get("add_country"):
            country = request.form["country"]
            exportqty = request.form["exportqty"]
            exportusd = request.form["exportusd"]
            area = request.form["area"]

            query = "INSERT INTO Countries (country, export_quantity, export_usd, cultivated_area) VALUES (%s, %s, %s, %s)"
            cursor = db.execute_query(db_connection=db_connection, query = query, query_params = (country, exportqty, exportusd, area))
                        
            # redirect to countries page
            return redirect("/countries")
    