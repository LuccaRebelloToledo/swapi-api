from app.utils.sql_alchemy import get_all_records, save_record

from app.models.favorite import Favorite,resource

from app.errors.app_error import AppError
from app.errors.app_error_types import app_error_types
from app.utils.http_status_code import NOT_FOUND

def find_all():
    data = get_all_records(Favorite)

    if not data:
        raise AppError(app_error_types[resource]['notFound'], NOT_FOUND)

    return data