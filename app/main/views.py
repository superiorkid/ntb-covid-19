from . import main
from flask import render_template
from ..api.covid_data import total_kasus, get_data

@main.route('/')
def index():
  kasus = total_kasus()

  return render_template('index.html', total_kasus=kasus, data=get_data())