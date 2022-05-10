import requests


def post(url, data):
    requests.post(url, data=data)


def create_user(username):
    email = f'{username}@{username}.com'
    password = '123'
    first_name = username
    last_name = username
    data = {'username': username,
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name:': last_name, }
    return post('http://127.0.0.1:8000/auth/users/', data=data)


# def create_course(course_name: str, taken):
#     data = {''}
#     return post('http://127.0.0.1:8000/platform/categories/', data=data)


create_user('ins1')
create_user('ins2')

create_user('std1')
create_user('std2')
