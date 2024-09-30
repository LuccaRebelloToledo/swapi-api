from sqlalchemy import text

from app.utils.database import db

from app.errors.app_error import AppError
from app.utils.http_status_code import SERVICE_UNAVAILABLE

def check_database_status():
        result = db.session.execute(text("SELECT 1"))

        if result.fetchone() is None:
                raise AppError('Database is not available.', SERVICE_UNAVAILABLE)