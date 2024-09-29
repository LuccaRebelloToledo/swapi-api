from app.utils.json import loads, process_kwargs

from app.utils.database import db

keys_to_process = ['species', 'starships', 'vehicles', 'characters', 'planets']

class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    episode_id = db.Column(db.Integer)
    opening_crawl = db.Column(db.Text)
    director = db.Column(db.String)
    producer = db.Column(db.String)
    release_date = db.Column(db.String)
    species = db.Column(db.Text)
    starships = db.Column(db.Text)
    vehicles = db.Column(db.Text)
    characters = db.Column(db.Text)
    planets = db.Column(db.Text)
    url = db.Column(db.String)
    created = db.Column(db.String)
    edited = db.Column(db.String)
    
    def __init__(self, **kwargs):
        process_kwargs(self, kwargs, keys_to_process)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'episode_id': self.episode_id,
            'opening_crawl': self.opening_crawl,
            'director': self.director,
            'producer': self.producer,
            'release_date': self.release_date,
            'species': loads(self.species),
            'starships': loads(self.starships),
            'vehicles': loads(self.vehicles),
            'characters': loads(self.characters),
            'planets': loads(self.planets),
            'url': self.url,
            'created': self.created,
            'edited': self.edited
        }