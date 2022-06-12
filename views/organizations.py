from flask import Flask, Blueprint, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

# Configuration
db_connection = db.connect_to_database()
organizations_view = Blueprint('organizations_view', __name__)

# Organizations READ
@organizations_view.route('/')
def organizations():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Organizations"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("organizations.j2", organizations=results)

# Organizations CREATE
@organizations_view.route('/add', methods=["POST", "GET"])
def organizations_add():
    db_connection = db.connect_to_database()
    
    # Render Add Form
    if request.method =="GET":
        return render_template("organizations_add.j2")

    # Add an organization
    if request.method == "POST":
        if request.form.get("add_org"):
            name = request.form["name"]
            type = request.form["type"]

            query = "INSERT INTO Organizations (name, type) VALUES (%s, %s)"
            cursor = db.execute_query(db_connection=db_connection, query = query, query_params = (name, type))
                        
            # redirect to organizations page
            return redirect("/organizations")
    