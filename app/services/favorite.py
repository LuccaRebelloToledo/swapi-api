from app.utils.sql_alchemy import get_all_records, save_record

from app.models.favorite import Favorite,resource

from app.models.service import Service
from app.models import people, film, starship, vehicle, specie, planet

from app.errors.app_error import AppError
from app.errors.app_error_types import app_error_types
from app.utils.http_status_code import NOT_FOUND

people_service = Service(people.People, people.resource)
film_service = Service(film.Film, film.resource)
starship_service = Service(starship.Starship, starship.resource)
vehicle_service = Service(vehicle.Vehicle, vehicle.resource)
specie_service = Service(specie.Specie, specie.resource)
planet_service = Service(planet.Planet, planet.resource)

def find_all():
    data = get_all_records(Favorite)

    if not data:
        raise AppError(app_error_types[resource]['notFound'], NOT_FOUND)

    return [item.to_dict() for item in data]

def save(data):
    people = people_service.find_by_id(data['people_id'])
    film = film_service.find_by_id(data['film_id'])
    starship = starship_service.find_by_id(data['starship_id'])
    vehicle = vehicle_service.find_by_id(data['vehicle_id'])
    specie = specie_service.find_by_id(data['specie_id'])
    planet = planet_service.find_by_id(data['planet_id'])

    new_data = {
        'character_name': people['name'],
        'birth_year': people['birth_year'],
        'movie_name': film['title'],
        'movie_number': film['episode_id'],
        'ship_name': starship['name'],
        'ship_model': starship['model'],
        'vehicle_name': vehicle['name'],
        'vehicle_model': vehicle['model'],
        'species_homeworld': specie['homeworld'],
        'spoken_languages': specie['language'],
        'planet_name': planet['name'],
        'population': planet['population'],
        'student1_name': data['student1_name'],
        'student1_registration': data['student1_registration'],
        'student2_name': data['student2_name'],
        'student2_registration': data['student2_registration'],
        'course': data['course'],
        'university': data['university'],
        'period': data['period'],
    }

    record = save_record(Favorite, new_data)

    return record.to_dict()