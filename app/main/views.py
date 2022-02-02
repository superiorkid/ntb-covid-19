from . import main
from flask import render_template
from ..api.covid_data import total_kasus, get_data, kasus_per_kabupaten

@main.route('/')
def index():
  return render_template('index.html', total_kasus=total_kasus(), data=get_data(), kasus_per_kabupaten=kasus_per_kabupaten())