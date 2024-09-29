from app.utils.swapi import get_swapi_resource

from app.utils.sql_alchemy import get_record, save_record, delete_record
from app.models.people import People

from app.errors.app_error import AppError
from app.errors.app_error_types import app_error_types
from app.utils.http_status_code import NOT_FOUND, CONFLICT

resource = 'people'

def find_all(page: int):
    return get_swapi_resource(resource, params={'page': page})  

def get_record_by_id(id: int):
    record = get_record(People, record_id=id)

    return record if record is not None else None

def find_by_id(id: int):
    record = get_record_by_id(id)

    return record.to_dict() if record is not None else get_swapi_resource(resource, id)

def save(id: int):
    record = get_record_by_id(id)

    if record is not None:
        raise AppError(app_error_types[resource]['alreadyExists'](id), CONFLICT)
    
    response = get_swapi_resource(resource, id)
    saved_record = save_record(People, response, id)
    
    return saved_record.to_dict()

def delete(id: int):
    record = get_record(People, id)

    if record is None:
        raise AppError(app_error_types[resource]['notFound'](id), NOT_FOUND)

    delete_record(record)