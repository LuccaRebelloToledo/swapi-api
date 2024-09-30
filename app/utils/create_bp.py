from flask import Blueprint

from app.utils.http_status_code import OK, CREATED, NO_CONTENT
from app.utils.api_response import create_api_response
from app.utils.request import get_page_number
from app.models.service import Service

def create_bp(model, resource: str):
  bp = Blueprint(resource, __name__, url_prefix=f'/{resource}')
  service = Service(model, resource)

  @bp.get('/')
  def fetch_all():
      page = get_page_number()
      data = service.find_all(page)

      return create_api_response(data, OK)

  @bp.get('/<int:id>')
  def fetch_by_id(id):
      data = service.find_by_id(id)
      return create_api_response(data, OK)

  @bp.post('/<int:id>/save')
  def save_record(id):
      data = service.save(id)

      return create_api_response(data, CREATED)

  @bp.delete('/<int:id>/delete')
  def delete_record(id):
      service.delete(id)

      return create_api_response(None, NO_CONTENT)
  
  return bp