def not_found_message(resource, id=None):
    if id is None:
        return f'The {resource} was not found!'
    else:
        return f'The {resource} with id {id} was not found!'

app_error_types = {
    'notFound': not_found_message,
    'alreadyExists': lambda resource, id: f'{resource.capitalize()} with id {id} already exists!',
}