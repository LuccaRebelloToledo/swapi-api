from app.utils.http_status_code import BAD_REQUEST

class AppError(Exception):
    status_code = BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code