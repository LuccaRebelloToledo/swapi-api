from app.utils.database import db

resource = 'favorites'

class Favorite(db.Model):
    __tablename__ = resource

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    character_name = db.Column(db.String)
    birth_year = db.Column(db.String)
    movie_name = db.Column(db.String)
    movie_number = db.Column(db.Integer)
    ship_name = db.Column(db.String)
    ship_model = db.Column(db.String)
    vehicle_name = db.Column(db.String)
    vehicle_model = db.Column(db.String)
    species_homeworld = db.Column(db.String)
    spoken_languages = db.Column(db.String)
    planet_name = db.Column(db.String)
    population = db.Column(db.Integer)
    student1_name = db.Column(db.String)
    student1_registration = db.Column(db.String)
    student2_name = db.Column(db.String, nullable=True)
    student2_registration = db.Column(db.String, nullable=True)
    course = db.Column(db.String)
    university = db.Column(db.String)
    period = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'character_name': self.character_name,
            'birth_year': self.birth_year,
            'movie_name': self.movie_name,
            'movie_number': self.movie_number,
            'ship_name': self.ship_name,
            'ship_model': self.ship_model,
            'vehicle_name': self.vehicle_name,
            'vehicle_model': self.vehicle_model,
            'species_homeworld': self.species_homeworld,
            'spoken_languages': self.spoken_languages,
            'planet_name': self.planet_name,
            'population': self.population,
            'student1_name': self.student1_name,
            'student1_registration': self.student1_registration,
            'student2_name': self.student2_name,
            'student2_registration': self.student2_registration,
            'course': self.course,
            'university': self.university,
            'period': self.period,
        }