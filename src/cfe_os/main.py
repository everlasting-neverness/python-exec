import pathlib
from flask import Flask
from .resources import get_resource_path


BASE_DIR = pathlib.Path(__file__).resolve().parent
DATA_DIR = get_resource_path("data")
IMG_PATH = DATA_DIR / '1.jpg'

web_app = Flask(__name__)

@web_app.route("/", methods=["GET"])
def index():
    return {"dir": str(BASE_DIR), 'data_dir': str(DATA_DIR)}, 200