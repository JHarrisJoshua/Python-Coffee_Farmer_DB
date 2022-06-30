from flask import Flask, Blueprint, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

# Configuration
db_connection = db.connect_to_database()
types_view = Blueprint('types_view', __name__)


# Types READ
@types_view.route('/', methods=["POST", "GET"])
def types():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Types"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("types.j2", types=results)


# Types CREATE
@types_view.route('/add', methods=["POST", "GET"])
def varieties_add():
    db_connection = db.connect_to_database()
    
    # Render Add Form
    if request.method == "GET":
        return render_template("types_add.j2")

    # Add a variety
    if request.method == "POST":
        if request.form.get("add_type"):
            name = request.form["name"]
            desc = request.form["desc"]

            query = "INSERT INTO Types (type_name, description) VALUES (%s, %s)"
            cursor = db.execute_query(db_connection=db_connection, query=query,
                                      query_params=(name, desc))
                        
            # redirect to types page
            return redirect("/types")
