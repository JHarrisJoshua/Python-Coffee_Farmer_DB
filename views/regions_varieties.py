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
def regions_varieties(region_id = None):
      db_connection = db.connect_to_database()
      
      # Get region from search if applicable
      if request.method == "POST":
            if request.form.get("region_variety_search"):
                  region_id = request.form["region_id"]
                 

      if (region_id is None) or (region_id == '0'):
            query = "SELECT region_plant_id, Varieties.plant_name, Varieties.rust_resist, Varieties.nematode_resist, Regions.altitude, Regions.rainfall, Regions.temp, Regions.region FROM Regions_Varieties INNER JOIN Regions ON Regions.region_id = Regions_Varieties.region_id INNER JOIN Varieties ON Varieties.plant_id = Regions_Varieties.plant_id ORDER BY region_plant_id ASC;"
      else:
            query = "SELECT region_plant_id, Varieties.plant_name, Varieties.rust_resist, Varieties.nematode_resist, Regions.altitude, Regions.rainfall, Regions.temp, Regions.region FROM Regions_Varieties INNER JOIN Regions ON Regions.region_id = Regions_Varieties.region_id INNER JOIN Varieties ON Varieties.plant_id = Regions_Varieties.plant_id WHERE Regions.region_id = %s" % (region_id)
      cursor = db.execute_query(db_connection=db_connection, query=query)
      results = cursor.fetchall()
      
      # For Search function, populate dropdown with all regions
      query2 = "SELECT DISTINCT Regions.region_id, Regions.region FROM Regions_Varieties INNER JOIN Regions ON Regions.region_id = Regions_Varieties.region_id ORDER BY Regions.region"
      cursor = db.execute_query(db_connection=db_connection, query=query2)
      region_list = cursor.fetchall()

      return render_template("regions_varieties.j2", regions_varieties=results, regions=region_list)

# Regions & Varieties Create
@regions_varieties_view.route('/add', methods=["POST", "GET"])
def regions_varieties_add():
      db_connection = db.connect_to_database()

      # Retrieve info for dropdowns
      if request.method =="GET":
        query = "SELECT region_id, region FROM Regions;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results1 = cursor.fetchall()

        query2 = "SELECT plant_id, plant_name FROM Varieties;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        results2 = cursor.fetchall()
        
        return render_template("regions_varieties_add.j2", regions = results1, plants = results2)

      if request.method == "POST":
            if request.form.get("region_variety_add"):
                  region_id = request.form["region_id"]
                  plant_id = request.form["plant_id"]
                  
                  query = "INSERT INTO Regions_Varieties (region_id, plant_id) VALUES (%s, %s)"
                  cursor = db.execute_query(db_connection=db_connection, query= query, query_params= (region_id, plant_id))

                  return redirect("/regions-varieties")                  



# Regions & Varieties UPDATE
# Pass plant_id via route
@regions_varieties_view.route('/edit/<int:region_plant_id>', methods=["POST", "GET"])
def regions_varieties_edit(region_plant_id):
      db_connection = db.connect_to_database()
      # Display the names of all Regions and name of user selected plant variety
      if request.method == "GET":
            query = "SELECT Regions_Varieties.region_plant_id, Varieties.plant_id, Varieties.plant_name, Regions.region_id, Regions.region FROM Regions_Varieties INNER JOIN Regions ON Regions.region_id = Regions_Varieties.region_id INNER JOIN Varieties ON Varieties.plant_id = Regions_Varieties.plant_id WHERE region_plant_id = %s" % (region_plant_id)
            cursor = db.execute_query(db_connection=db_connection, query=query)
            result = cursor.fetchall()
            
            # populate regionlist with all possible regions
            query2 = "SELECT region_id, region from Regions"
            cursor = db.execute_query(db_connection=db_connection, query=query2)
            regionlist = cursor.fetchall()

            # populate regionlist with all possible regions
            query3 = "SELECT plant_id, plant_name from Varieties"
            cursor = db.execute_query(db_connection=db_connection, query=query3)
            plantlist = cursor.fetchall()
            
            return render_template("regions_varieties_edit.j2", result=result, regionlist=regionlist, plantlist=plantlist)
    # Update Regions_Varieties
      if request.method == "POST":
            if request.form.get("edit_regions_varieties"): 
                  region_id = request.form["region_id"]
                  plant_id = request.form["plant_id"]
                  query = "UPDATE Regions_Varieties SET Regions_Varieties.region_id = %s, Regions_Varieties.plant_id = %s WHERE Regions_Varieties.region_plant_id = %s"
                  cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(region_id, plant_id, region_plant_id))
            return redirect("/regions-varieties")

# Regions & Varieties DELETE
@regions_varieties_view.route('/delete/<int:region_plant_id>', methods=["POST", "GET"])
def regions_varieties_delete(region_plant_id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Regions_Varieties WHERE region_plant_id= %s" % (region_plant_id)
    cursor = db.execute_query(db_connection=db_connection, query=query)
    # redirect
    return redirect("/regions-varieties")
