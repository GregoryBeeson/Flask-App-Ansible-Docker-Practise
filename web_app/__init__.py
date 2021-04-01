from flask import Flask, session

template_dir = "/templates"
app = Flask(__name__, template_folder=template_dir)

import routes