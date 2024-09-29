import requests
from requests.exceptions import RequestException

from app.errors.app_error import AppError
from app.errors.app_error_types import app_error_types
from app.utils.http_status_code import NOT_FOUND

BASE_API_URL = 'https://swapi.dev/api'

def get_swapi_resource(resource: str, param: int = None):
    try:
        url = f'{BASE_API_URL}/{resource}/{param}' if param is not None else f'{BASE_API_URL}/{resource}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        if err.response is not None:
            raise AppError(err.response.text, err.response.status_code)
        else:
            raise AppError(str(err))

def get_swapi_resource_by_id(resource: str, id: int):
    response = get_swapi_resource(resource, id)

    if response is None or ('detail' in response and response['detail'] == 'Not found'):
        raise AppError(app_error_types[resource]['notFound'](id), NOT_FOUND)
    
    return response