app_error_types = {
    'notFound': lambda resource, id: f'{resource.capitalize()} with id {id} not found!',
    'alreadyExists': lambda resource, id: f'{resource.capitalize()} with id {id} already exists!'
}