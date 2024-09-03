from flask import Flask 
import yaml, os.path

app = Flask(__name__)

data_file_path = os.path.join(os.path.dirname(__file__), 'data/data.yml')
with open(data_file_path, 'r') as file:
    data = yaml.safe_load(file)