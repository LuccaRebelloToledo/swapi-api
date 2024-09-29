from flask import request

def get_page_number():
    page = request.args.get('page', 1, type=int)

    if page < 1:
        page = 1
        
    return page