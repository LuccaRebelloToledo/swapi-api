from marshmallow import Schema, fields

class BodySchema(Schema):
    people_id = fields.Int(required=True)
    film_id = fields.Int(required=True)
    starship_id = fields.Int(required=True)
    vehicle_id = fields.Int(required=True)
    specie_id = fields.Int(required=True)
    planet_id = fields.Int(required=True)
    student1_name = fields.Str(required=True)
    student1_registration = fields.Str(required=True)
    student2_name = fields.Str(allow_none=True)
    student2_registration = fields.Str(allow_none=True)
    course = fields.Str(required=True)
    university = fields.Str(required=True)
    period = fields.Str(required=True)