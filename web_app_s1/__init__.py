from flask import Flask
from flask_sqlalchemy import SQLAlchemy

template_dir = "/templates"
app = Flask(__name__)

from web_app_s1 import routes