from ensurepip import bootstrap
from flask import Flask
import logging
import sys


def create_app():
  app = Flask(__name__)

  app.logger.addHandler(logging.StreamHandler(sys.stdout))
  app.logger.setLevel(logging.ERROR)

  from .main import main as main_bp
  app.register_blueprint(main_bp)

  return app