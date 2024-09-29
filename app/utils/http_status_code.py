from http import HTTPStatus

# Informational
OK = HTTPStatus.OK.value # 200
CREATED = HTTPStatus.CREATED.value #201
NO_CONTENT = HTTPStatus.NO_CONTENT.value #204

# Client Error
BAD_REQUEST = HTTPStatus.BAD_REQUEST.value #400
NOT_FOUND = HTTPStatus.NOT_FOUND.value #404
CONFLICT = HTTPStatus.CONFLICT.value #409

# Server Error
INTERNAL_SERVER_ERROR = HTTPStatus.INTERNAL_SERVER_ERROR.value #500