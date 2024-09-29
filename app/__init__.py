from flask import Flask

from app.utils.database import db

from app.errors.app_error import AppError
from app.utils.api_response import create_api_error_message
from app.utils.http_status_code import INTERNAL_SERVER_ERROR

from app.controllers import status, people, film, starship, planet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///swapi.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(status.bp)
app.register_blueprint(people.bp)
app.register_blueprint(film.bp)
app.register_blueprint(starship.bp)
app.register_blueprint(planet.bp)

@app.errorhandler(AppError)
def handle_invalid_usage(error):
    return create_api_error_message(error.message, error.status_code)

@app.errorhandler(Exception)
def handle_internal_server_error(error):
    print(error)
    return create_api_error_message('Internal Server Error', INTERNAL_SERVER_ERROR)

with app.app_context():
    db.create_all()