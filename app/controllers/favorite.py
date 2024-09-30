from flask import Blueprint

from app.models.favorite import resource
from app.services.favorite import find_all

from app.utils.api_response import create_api_response
from app.utils.http_status_code import OK

bp = Blueprint(resource, __name__, url_prefix=f'/{resource}')

@bp.get('/')
def fetch_all():
    data =  find_all()

    return create_api_response(data, OK)

@bp.post('/save')
def save_record():
    return 'save_record'