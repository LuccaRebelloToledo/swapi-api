from app.models.vehicle import Vehicle, resource
from app.utils.create_bp import create_bp

bp = create_bp(Vehicle, resource)