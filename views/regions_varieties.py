from flask import Flask, Blueprint, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

# Configuration
db_connection = db.connect_to_database()
regions_varieties_view = Blueprint('regions_varieties_view', __name__)


# Regions & Varieties READ
@regions_varieties_view.route('/', methods=["POST", "GET"])
@regions_varieties_view.route('/<int:region_id>', methods=["POST", "GET"])
def regions_varieties(region_id=None):
    db_connection = db.connect_to_database()

    # Get region from search if applicable
    if request.method == "POST":
        if request.form.get("region_variety_search"):
            region_id = request.form["region_id"]

    if (region_id is None) or (region_id == '0'):
        query = "SELECT plant_name, rust_resist, nematode_resist, altitude, rainfall, temp, region FROM Regions JOIN Varieties ON Regions.altitude = Varieties.optimal_altitude AND Regions.rainfall = Varieties.optimal_rainfall AND Regions.temp = Varieties.optimal_temp ORDER BY plant_id, region_id"
    else:
        query = "SELECT plant_name, rust_resist, nematode_resist, altitude, rainfall, temp, region FROM Regions JOIN Varieties ON Regions.altitude = Varieties.optimal_altitude AND Regions.rainfall = Varieties.optimal_rainfall AND Regions.temp = Varieties.optimal_temp WHERE Regions.region_id = %s ORDER BY plant_id, region_id" % (region_id)
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()

    # For Search function, populate dropdown with all regions
    query2 = "SELECT DISTINCT region_id, region FROM Regions JOIN Varieties ON Regions.altitude = Varieties.optimal_altitude AND Regions.rainfall = Varieties.optimal_rainfall AND Regions.temp = Varieties.optimal_temp ORDER BY region"
    cursor = db.execute_query(db_connection=db_connection, query=query2)
    region_list = cursor.fetchall()

    return render_template("regions_varieties.j2", regions_varieties=results, regions=region_list)
