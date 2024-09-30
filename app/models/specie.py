from app.utils.json import loads, process_kwargs

from app.utils.database import db

resource = 'species'
keys_to_process = ['people', 'films']

class Specie(db.Model):
    __tablename__ = resource

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    classification = db.Column(db.String)
    designation = db.Column(db.String)
    average_height = db.Column(db.String)
    skin_colors = db.Column(db.String)
    hair_colors = db.Column(db.String)
    eye_colors = db.Column(db.String)
    average_lifespan = db.Column(db.String)
    homeworld = db.Column(db.String)
    language = db.Column(db.String)
    people = db.Column(db.Text)
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
            'classification': self.classification,
            'designation': self.designation,
            'average_height': self.average_height,
            'skin_colors': self.skin_colors,
            'hair_colors': self.hair_colors,
            'eye_colors': self.eye_colors,
            'average_lifespan': self.average_lifespan,
            'homeworld': self.homeworld,
            'language': self.language,
            'people': loads(self.people),
            'films': loads(self.films),
            'created': self.created,
            'edited': self.edited,
            'url': self.url
        }