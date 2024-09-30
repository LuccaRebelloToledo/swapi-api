from flask import Blueprint

from app.services.status import check_database_status

from app.utils.http_status_code import OK
from app.utils.api_response import create_api_response
  
bp = Blueprint('status', __name__)

@bp.get('/')
def status():
    check_database_status()
    
    return create_api_response('Everything is Fine!', OK)

