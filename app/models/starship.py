from app.utils.json import loads, process_kwargs

from app.utils.database import db

keys_to_process = ['films', 'pilots']

class Starship(db.Model):
    __tablename__ = 'starships'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    model = db.Column(db.String)
    manufacturer = db.Column(db.String)
    cost_in_credits = db.Column(db.String)
    length = db.Column(db.String)
    max_atmosphering_speed = db.Column(db.String)
    crew = db.Column(db.String)
    passengers = db.Column(db.String)
    cargo_capacity = db.Column(db.String)
    consumables = db.Column(db.String)
    hyperdrive_rating = db.Column(db.String)
    MGLT = db.Column(db.String)
    starship_class = db.Column(db.String)
    pilots = db.Column(db.Text)
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
            'model': self.model,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'length': self.length,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'crew': self.crew,
            'passengers': self.passengers,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables,
            'hyperdrive_rating': self.hyperdrive_rating,
            'MGLT': self.MGLT,
            'starship_class': self.starship_class,
            'pilots': loads(self.pilots),
            'films': loads(self.films),
            'created': self.created,
            'edited': self.edited,
            'url': self.url
        }