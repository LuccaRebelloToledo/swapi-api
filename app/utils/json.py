import json

def loads(value):
    try:
        return json.loads(value) if value else []
    except json.JSONDecodeError:
        return []

def dumps(value):
    try:
        return json.dumps(value) if value else '[]'
    except (TypeError, ValueError):
        return '[]'
    
def process_kwargs(self, kwargs, keys_to_process: list):
    for key, value in kwargs.items():
        if key in keys_to_process:
            if isinstance(value, list):
                value = dumps(value)
            elif isinstance(value, str):
                value = loads(value)
        setattr(self, key, value)