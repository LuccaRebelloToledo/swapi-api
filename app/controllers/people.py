from app.models.people import People, resource
from app.utils.create_bp import create_bp

bp = create_bp(People, resource)