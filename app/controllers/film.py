from app.models.film import Film, resource
from app.utils.create_bp import create_bp

bp = create_bp(Film, resource)