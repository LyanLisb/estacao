from flask import Flask, render_template

from config import config_all

app = Flask(__name__)

config_all(app)


