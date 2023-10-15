#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint

# Create a Blueprint for the views with the prefix '/api/v1'
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import views from the 'index' module to define your API routes
from api.v1.views.index import *
