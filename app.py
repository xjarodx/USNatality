import os

import sys

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

engine = create_engine("sqlite:///Files/Data/birthrate3.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
birthrate = Base.classes

# Create our session (link) from Python to the DB
session = Session(engine) 
#print (Base.classes.keys())
print(Base.classes.keys(), file=sys.stderr)
@app.route("/")
def index():
    """Return the homepage."""
    results = session.query(birthrate.countylevel).all()
    print(results) 
   # return ''.join(Base.classes.keys())
    return render_template("index.html")


@app.route("/data")
def data():
    """Return the data"""
    return render_template("data.html")


@app.route("/choropleth")
def choropleth():
    """Return the choropleth for US"""
    return render_template("choropleth.html")


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
