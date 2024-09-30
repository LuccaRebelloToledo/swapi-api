from app.utils.swapi import get_swapi_resource

from app.utils.sql_alchemy import get_record, save_record, delete_record

from app.errors.app_error import AppError
from app.errors.app_error_types import app_error_types
from app.utils.http_status_code import NOT_FOUND, CONFLICT

class Service:
    def __init__(self, model, resource):
        self.resource = resource
        self.model = model

    def find_all(self, page: int):
        return get_swapi_resource(self.resource, params={'page': page})

    def get_record_by_id(self, id: int):
        record = get_record(self.model, record_id=id)
        
        return record if record is not None else None

    def find_by_id(self, id: int):
        record = self.get_record_by_id(id)

        return record.to_dict() if record is not None else get_swapi_resource(self.resource, id)

    def save(self, id: int):
        record = self.get_record_by_id(id)

        if record is not None:
            raise AppError(app_error_types['alreadyExists'](self.resource, id), CONFLICT)
        
        response = get_swapi_resource(self.resource, id)
        saved_record = save_record(self.model, response, id)
        
        return saved_record.to_dict()

    def delete(self, id: int):
        record = self.get_record_by_id(id)

        if record is None:
            raise AppError(app_error_types['notFound'](self.resource, id), NOT_FOUND)
        
        return delete_record(record)