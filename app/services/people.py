from app.utils.swapi import get_swapi_resource

from app.utils.sql_alchemy import get_record, save_record, delete_record
from app.models.people import People, keys_to_process

from app.errors.app_error import AppError
from app.errors.app_error_types import app_error_types
from app.utils.http_status_code import NOT_FOUND

resource = 'people'

def find_all():
    return get_swapi_resource(resource)

def find_by_id(id: int):
    record = get_record(People, id)

    if record is not None:
        return record.to_dict()
    
    response = get_swapi_resource(resource, id)

    if response is None or ('detail' in response and response['detail'] == 'Not found'):
        raise AppError(app_error_types['peoples']['notFound'](id), NOT_FOUND)
    
    return response

def save(id: int):
    record = find_by_id(id)

    save_record(People, record, id, keys_to_process)
    
    return record

def delete(id: int):
    record = get_record(People, id)

    if record is None:
        raise AppError(app_error_types['peoples']['notFound'](id), NOT_FOUND)

    delete_record(record)