import os

import pandas as pd
import numpy as np
import datetime as dt 

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

# need to make sure that the reference is updated for the structure
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/natality.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# need to make sure that the reference is updated for the structure
# Save references to each table
state = Base.classes.state
national = Base.classes.national


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/data")
def data():
    """Return the state level data"""
    return render_template("data.html")


@app.route("/nationalchoropleth")
def n_choropleth(national):
    """Return the choropleth for US"""
    return render_template("national.html")



@app.route("/statechoropleth")
def s_choropleth(state):
    """Return the choropleth for the state"""
    return render_template("state.html")


@app.route("/bubblechart")
def bubble():
    """Return the bubble chart"""
    return render_template("bubblechart.html")

@app.route("/linechart")
def line():
    """Return the line chart"""
    return render_template("linechart.html")

if __name__ == "__main__":
    app.run()
