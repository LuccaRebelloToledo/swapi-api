from app.utils.json import loads, process_kwargs

from app.utils.database import db

keys_to_process = ['residents', 'films']

class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    rotation_period = db.Column(db.String)
    orbital_period = db.Column(db.String)
    diameter = db.Column(db.String)
    climate = db.Column(db.String)
    gravity = db.Column(db.String)
    terrain = db.Column(db.String)
    surface_water = db.Column(db.String)
    population = db.Column(db.String)
    residents = db.Column(db.Text)
    films = db.Column(db.Text)
    created = db.Column(db.String)
    edited = db.Column(db.String)
    url = db.Column(db.String)

    def __init__(self, **kwargs):
        process_kwargs(self, kwargs, keys_to_process)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'diameter': self.diameter,
            'climate': self.climate,
            'gravity': self.gravity,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'population': self.population,
            'residents': loads(self.residents),
            'films': loads(self.films),
            'created': self.created,
            'edited': self.edited,
            'url': self.url
        }