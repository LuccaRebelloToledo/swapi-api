from app.utils.database import db

def get_record(model, record_id: str):
    record = get_record(model, record_id)

    return record.to_dict() if record is not None else None

def save_record(model, data: dict, record_id: str):
    data['id'] = record_id

    new_record = model(**data)
    db.session.add(new_record)
    db.session.commit()

    return new_record.to_dict()

def delete_record(record):
  db.session.delete(record)
  db.session.commit()