from flask import Flask, Blueprint, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request

# Import Table views for Flask Blueprints
from views.varieties import varieties_view
from views.regions import regions_view
from views.regions_varieties import regions_varieties_view
from views.types import types_view
from views.countries import countries_view
from views.organizations import organizations_view
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()
db_connection.ping(True)

# Register Flask Blueprints
app.register_blueprint(varieties_view, url_prefix='/varieties')
app.register_blueprint(regions_view, url_prefix='/regions')
app.register_blueprint(regions_varieties_view, url_prefix='/regions-varieties')
app.register_blueprint(types_view, url_prefix='/types')
app.register_blueprint(countries_view, url_prefix='/countries')
app.register_blueprint(organizations_view, url_prefix='/organizations')

# Route to Index 
@app.route('/')
def root():
    return render_template("index.j2")

# Listener
if __name__ == "__main__":
    # Local
    port = int(os.environ.get('PORT', 51737)) 
    app.run(port=port, debug=True)

