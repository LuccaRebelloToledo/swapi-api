from app.utils.swapi import get_swapi_resource

from app.utils.sql_alchemy import get_record, save_record, delete_record
from app.models.film import Film

from app.errors.app_error import AppError
from app.errors.app_error_types import app_error_types
from app.utils.http_status_code import NOT_FOUND, CONFLICT

resource = 'films'

def find_all(page: int):
    return get_swapi_resource(resource, params={'page': page})  

def get_record_by_id(id: int):
    record = get_record(Film, record_id=id)

    return record if record is not None else None

def find_by_id(id: int):
    record = get_record_by_id(id)

    return record.to_dict() if record is not None else get_swapi_resource(resource, id)

def save(id: int):
    record = get_record_by_id(id)

    if record is not None:
        raise AppError(app_error_types['alreadyExists'](resource, id), CONFLICT)
    
    response = get_swapi_resource(resource, id)
    saved_record = save_record(Film, response, id)
    
    return saved_record.to_dict()

def delete(id: int):
    record = get_record(Film, id)

    if record is None:
        raise AppError(app_error_types['notFound'](resource, id), NOT_FOUND)

    delete_record(record)