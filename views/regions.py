from flask import Flask, Blueprint, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

# Configuration
db_connection = db.connect_to_database()
regions_view = Blueprint('regions_view', __name__)

# Regions READ
@regions_view.route('/')
def regions():
    db_connection = db.connect_to_database()
    query = "SELECT region_id, region, altitude, soil_type, rainfall, temp, Countries.country FROM Regions INNER JOIN Countries ON Regions.country_id = Countries.country_id ORDER BY region_id;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("regions.j2", regions=results)
    
# Regions CREATE
@regions_view.route('/add', methods=["POST", "GET"])
def regions_add():
    db_connection = db.connect_to_database()
    #print(request.method, request.form.get("add_variety"), request)

    # Retrieve info for dropdowns
    if request.method =="GET":
        query = "SELECT country_id, country FROM Countries;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        return render_template("regions_add.j2", countries = results)

    # Add a Regions
    if request.method == "POST":
        if request.form.get("add_region"):
            name = request.form["name"]
            altitude = request.form["altitude"]
            soil = request.form["soil"]
            rain = request.form["rainfall"]
            temp = request.form["temperature"]
            country_id = request.form["country_id"]

            query = "INSERT INTO Regions (region, altitude, soil_type, rainfall, temp, country_id) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor = db.execute_query(db_connection=db_connection, query = query, query_params = (name, altitude, soil, rain, temp, country_id))

            # redirect to regions page
            return redirect("/regions")

#Regions DELETE
@regions_view.route('/delete/<int:region_id>', methods=["POST", "GET"])
def regions_delete(region_id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Regions WHERE region_id = %s" % (region_id)
    cursor = db.execute_query(db_connection=db_connection, query=query)
    # redirect to regions page
    return redirect("/regions")


