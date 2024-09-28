from app.utils.json import process_kwargs

from app.utils.database import db

def get_record(model, record_id: str):
    return model.query.get(record_id)

def save_record(model, data: dict, record_id: str, keys_to_process: list):
    existing_record = model.query.get(record_id)
    
    if existing_record:
        return update_record(existing_record, data, keys_to_process)
    
    data['id'] = record_id

    new_record = model(**data)
    db.session.add(new_record)
    db.session.commit()
    return new_record
    existing_record = model.query.get(record_id)
    
    if existing_record:
        for key, value in data.items():
            setattr(existing_record, key, value)
        db.session.commit()
        return existing_record
    
    data['id'] = record_id

    new_record = model(**data)
    db.session.add(new_record)
    db.session.commit()
    return new_record

def update_record(existing_record, data, keys_to_process):
    process_kwargs(existing_record, data, keys_to_process)
    db.session.commit()
    return existing_record

def delete_record(record):
  db.session.delete(record)
  db.session.commit()