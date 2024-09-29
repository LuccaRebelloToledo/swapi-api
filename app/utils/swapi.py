import requests
from requests.exceptions import RequestException

from app.errors.app_error import AppError

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