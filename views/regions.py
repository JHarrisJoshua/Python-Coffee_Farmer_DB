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
    query = "SELECT region_id, region, soil_type, altitude, rainfall, temp, Countries.country FROM Regions INNER JOIN Countries ON Regions.country_id = Countries.country_id ORDER BY region_id;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("regions.j2", regions=results)


# Regions CREATE
@regions_view.route('/add', methods=["POST", "GET"])
def regions_add():
    db_connection = db.connect_to_database()

    # Retrieve info for dropdowns
    if request.method == "GET":
        query = "SELECT country_id, country FROM Countries;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        return render_template("regions_add.j2", countries=results)

    # Add a Regions
    if request.method == "POST":
        if request.form.get("add_region"):
            name = request.form["name"]
            soil = request.form["soil"]
            altitude = request.form["altitude"]
            rain = request.form["rainfall"]
            temp = request.form["temperature"]
            country_id = request.form["country_id"]

            query = "INSERT INTO Regions (region, soil_type, altitude, rainfall, temp, country_id) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name, soil, altitude, rain, temp, country_id))

            # redirect to regions page
            return redirect("/regions")


# Update Region
@regions_view.route('/edit/<int:region_id>', methods=["POST", "GET"])
def regions_edit(region_id):
    db_connection = db.connect_to_database()

    # Retrieve info update/dropdowns
    if request.method == "GET":
        query = "SELECT region_id, region, soil_type, altitude, rainfall, temp, Countries.country FROM Regions INNER JOIN Countries ON Regions.country_id = Countries.country_id ORDER BY region_id; WHERE region_id = %s" % (region_id)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        query2 = "SELECT country_id, country FROM Countries;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        results2 = cursor.fetchall()

        return render_template("regions_edit.j2", data=results, countries=results2)

    # Update Variety
    if request.method == "POST":
        if request.form.get("edit_region"):
            region = request.form["region"]
            soil = request.form["soil"]
            alt = request.form["altitude"]
            rainfall = request.form["rainfall"]
            temp = request.form["temp"]
            country_id = request.form["country_id"]

            query = "UPDATE Regions SET region = %s, soil_type = %s,  altitude = %s, rainfall = %s, temp = %s, country_id = %s WHERE region_id = %s"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(region, soil, alt, rainfall, temp, country_id, region_id))

            # Redirect to varieties page
            return redirect("/regions")


# Regions DELETE
@regions_view.route('/delete/<int:region_id>', methods=["POST", "GET"])
def regions_delete(region_id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Regions WHERE region_id = %s" % (region_id)
    cursor = db.execute_query(db_connection=db_connection, query=query)
    # redirect to regions page
    return redirect("/regions")


