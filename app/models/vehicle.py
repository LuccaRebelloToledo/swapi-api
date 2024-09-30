from app.utils.json import loads, process_kwargs

from app.utils.database import db

resource = 'vehicles'
keys_to_process = ['pilots', 'films']

class Vehicle(db.Model):
    __tablename__ = resource

    id = db.Column(db.Integer, primary_key=True)
    cargo_capacity = db.Column(db.String)
    consumables = db.Column(db.String)
    cost_in_credits = db.Column(db.String)
    created = db.Column(db.String)
    crew = db.Column(db.String)
    edited = db.Column(db.String)
    length = db.Column(db.String)
    manufacturer = db.Column(db.String)
    max_atmosphering_speed = db.Column(db.String)
    model = db.Column(db.String)
    name = db.Column(db.String)
    passengers = db.Column(db.String)
    pilots = db.Column(db.Text)
    films = db.Column(db.Text)
    url = db.Column(db.String)
    vehicle_class = db.Column(db.String)

    def __init__(self, **kwargs):
        process_kwargs(self, kwargs, keys_to_process)

    def to_dict(self):
        return {
            'id': self.id,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables,
            'cost_in_credits': self.cost_in_credits,
            'created': self.created,
            'crew': self.crew,
            'edited': self.edited,
            'length': self.length,
            'manufacturer': self.manufacturer,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'model': self.model,
            'name': self.name,
            'passengers': self.passengers,
            'pilots': loads(self.pilots),
            'films': loads(self.films),
            'url': self.url,
            'vehicle_class': self.vehicle_class
        }