import requests

from requests.exceptions import RequestException
from app.utils.json import loads
from app.errors.app_error import AppError

BASE_API_URL = 'https://swapi.dev/api'

def get_swapi_resource(resource: str, id: int = None, params: dict = None):
    try:
        url = f'{BASE_API_URL}/{resource}/{id}' if id is not None else f'{BASE_API_URL}/{resource}'
        response = requests.get(url, params)
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        if err.response is not None:
            response_json = loads(err.response.text)
            detail_message = response_json.get('detail', response_json)
            raise AppError(f'{resource.capitalize()} - {detail_message}' if detail_message is not None else err.response.text, err.response.status_code)
        else:
            raise AppError(str(err))