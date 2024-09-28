from flask import jsonify

from app.utils.http_status_code import HTTPStatus, BAD_REQUEST

def create_response(data: dict, status_code: int):
    return jsonify(data), status_code

def create_api_response(message: any, status_code: int):
    data = {'statusCode': status_code, 'message': message}
    return create_response(data, status_code)

def create_api_error_message(message: any, status_code: int = BAD_REQUEST):
    data = {'statusCode': status_code, 'error': HTTPStatus(status_code).phrase, 'message': message}
    return create_response(data, status_code)