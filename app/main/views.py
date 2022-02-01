from . import main
from flask import render_template
from ..api.covid_data import get_data 

@main.route('/')
def index():
  data = get_data()
  return render_template('index.html', data=data)