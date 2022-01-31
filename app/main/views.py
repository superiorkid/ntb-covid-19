from . import main
from flask import render_template
from ..api.covid_data import total_cases

@main.route('/')
def index():
  total_kasus = total_cases()

  return render_template('index.html', case_total=total_kasus)