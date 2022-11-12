from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dbuserbdbuser@localhost/students'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app)