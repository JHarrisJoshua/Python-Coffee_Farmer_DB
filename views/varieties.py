from flask import Flask, Blueprint, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

# Configuration
db_connection = db.connect_to_database()
varieties_view = Blueprint('varieties_view', __name__)

# Varieties READ
@varieties_view.route('/', methods=["POST", "GET"])
def varieties():
    db_connection = db.connect_to_database()
    query = "SELECT plant_id, plant_name, rust_resist, nematode_resist, optimal_altitude, optimal_rainfall, optimal_temp, Organizations.name, Types.name FROM Varieties LEFT JOIN Organizations ON Varieties.organization_id = Organizations.organization_id INNER JOIN Types ON Varieties.type_id = Types.type_id ORDER BY plant_id"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("varieties.j2", varieties=results)

# Varieties CREATE
@varieties_view.route('/add', methods=["POST", "GET"])
def varieties_add():
    db_connection = db.connect_to_database()

    # Retrieve info for dropdowns
    if request.method =="GET":
        query = "SELECT organization_id, name FROM Organizations;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results1 = cursor.fetchall()

        query2 = "SELECT type_id, name FROM Types;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        results2 = cursor.fetchall()

        return render_template("varieties_add.j2", organizations = results1, types = results2)

    # Add a variety
    if request.method == "POST":
        if request.form.get("add_variety"):
            name = request.form["name"]
            rust = request.form["rust_resist"]
            nematode = request.form["nematode_resist"]
            opt_alt = request.form["altitude"]
            opt_rain = request.form["rainfall"]
            opt_temp = request.form["temperature"]
            org_id = request.form["organization_id"]
            type_id = request.form["type_id"]

            if (org_id== "" or org_id =="0" or org_id == "None" or org_id == "NULL"):
                query = "INSERT INTO Varieties (plant_name, rust_resist, nematode_resist, optimal_altitude, optimal_rainfall, optimal_temp, type_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor = db.execute_query(db_connection=db_connection, query = query, query_params = (name, rust, nematode, opt_alt, opt_rain, opt_temp, type_id))

            else:
                query = "INSERT INTO Varieties (plant_name, rust_resist, nematode_resist, optimal_altitude, optimal_rainfall, optimal_temp, organization_id, type_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor = db.execute_query(db_connection=db_connection, query = query, query_params = (name, rust, nematode, opt_alt, opt_rain, opt_temp, org_id, type_id))

            # redirect to varieties page
            return redirect("/varieties")

# Varieties DELETE
@varieties_view.route('/delete/<int:plant_id>', methods=["POST", "GET"])
def varieties_delete(plant_id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Varieties WHERE plant_id = %s" % (plant_id)
    cursor = db.execute_query(db_connection=db_connection, query=query)
    # redirect to varieties page
    return redirect("/varieties")

# Varieties UPDATE
@varieties_view.route('/edit/<int:plant_id>', methods=["POST", "GET"])
def varieties_edit(plant_id):
    db_connection = db.connect_to_database()
    
    # Retrieve info update/dropdowns
    if request.method == "GET":
        query = "SELECT plant_id, plant_name, rust_resist, nematode_resist, optimal_altitude, optimal_rainfall, optimal_temp, Organizations.name, Types.name FROM Varieties LEFT JOIN Organizations ON Varieties.organization_id = Organizations.organization_id INNER JOIN Types ON Varieties.type_id = Types.type_id WHERE plant_id = %s" % (plant_id)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        result = cursor.fetchall()

        query2 = "SELECT organization_id, name FROM Organizations;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        results2 = cursor.fetchall()

        query3 = "SELECT type_id, name FROM Types;"
        cursor = db.execute_query(db_connection=db_connection, query=query3)
        results3 = cursor.fetchall()

        return render_template("varieties_edit.j2", data = result, organizations = results2, types = results3)

    # Update Variety
    if request.method == "POST":
        if request.form.get("edit_variety"):
            name = request.form["name"]
            rust = request.form["rust_resist"]
            nematode = request.form["nematode_resist"]
            opt_alt = request.form["altitude"]
            opt_rain = request.form["rainfall"]
            opt_temp = request.form["temperature"]
            org_id = request.form["organization_id"]
            type_id = request.form["type_id"]

            if (org_id== "" or org_id =="0" or org_id == "None" or org_id == "NULL"):
                query = "UPDATE Varieties SET Varieties.plant_name = %s, Varieties.rust_resist = %s, Varieties.nematode_resist = %s, Varieties.optimal_altitude = %s, Varieties.optimal_rainfall = %s, Varieties.optimal_temp = %s, Varieties.organization_id = NULL, Varieties.type_id = %s WHERE Varieties.plant_id = %s"
                cursor = db.execute_query(db_connection=db_connection, query = query, query_params = (name, rust, nematode, opt_alt, opt_rain, opt_temp, type_id, plant_id))

            else:
                query = "UPDATE Varieties SET Varieties.plant_name = %s, Varieties.rust_resist = %s, Varieties.nematode_resist = %s, Varieties.optimal_altitude = %s, Varieties.optimal_rainfall = %s, Varieties.optimal_temp = %s, Varieties.organization_id = %s, Varieties.type_id = %s WHERE Varieties.plant_id = %s"
                cursor = db.execute_query(db_connection=db_connection, query = query, query_params = (name, rust, nematode, opt_alt, opt_rain, opt_temp, org_id, type_id, plant_id))

            # redirect to varieties page
            return redirect("/varieties")
