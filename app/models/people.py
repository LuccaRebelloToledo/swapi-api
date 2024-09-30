from app.utils.json import loads, process_kwargs

from app.utils.database import db

resource = 'people'
keys_to_process = ['films', 'species', 'vehicles', 'starships']

class People(db.Model):
    __tablename__ = resource

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    height = db.Column(db.String)
    mass = db.Column(db.String)
    hair_color = db.Column(db.String)
    skin_color = db.Column(db.String)
    eye_color = db.Column(db.String)
    birth_year = db.Column(db.String)
    gender = db.Column(db.String)
    homeworld = db.Column(db.String)
    films = db.Column(db.Text)
    species = db.Column(db.Text)
    vehicles = db.Column(db.Text)
    starships = db.Column(db.Text)
    created = db.Column(db.String)
    edited = db.Column(db.String)
    url = db.Column(db.String)

    def __init__(self, **kwargs):
        process_kwargs(self, kwargs, keys_to_process)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
            'eye_color': self.eye_color,
            'birth_year': self.birth_year,
            'gender': self.gender,
            'homeworld': self.homeworld,
            'films': loads(self.films),
            'species': loads(self.species),
            'vehicles': loads(self.vehicles),
            'starships': loads(self.starships),
            'created': self.created,
            'edited': self.edited,
            'url': self.url
        }