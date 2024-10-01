from flask import Blueprint, request

from app.models.favorite import resource
from app.services.favorite import find_all, save

from app.schemas.favorite import BodySchema

from app.utils.api_response import create_api_response
from app.utils.http_status_code import OK, CREATED

bp = Blueprint(resource, __name__, url_prefix=f'/{resource}')

bodySchema = BodySchema()

@bp.get('/')
def fetch_all():
    data =  find_all()

    return create_api_response(data, OK)

@bp.post('/save')
def save_record():
    data = request.get_json()
    
    bodySchema.load(data)

    record =  save(data)

    return create_api_response(record, CREATED)