import datetime
import json

import requests


def post(url, json_data=None, headers=None, data=None):
    data = requests.post(url, json=json_data, headers=headers, data=data)
    try:
        data = data.json()
    except:
        pass
    return data


def get(url, json_data=None, headers=None, data=None):
    data = requests.get(url, json=json_data, headers=headers, data=data)
    try:
        data = data.json()
    except:
        pass
    return data


def create_user(username, password='123'):
    email = f'{username}@{username}.com'
    first_name = username
    last_name = username
    json_data = {'username': username,
                 'email': email,
                 'password': password,
                 'first_name': first_name,
                 'last_name:': last_name, }
    return post('http://127.0.0.1:8000/auth/users/', json_data=json_data)


def login(username, password='123'):
    url = 'http://127.0.0.1:8000/auth/jwt/create'
    json_data = {'username': username, 'password': password}
    return post(url, json_data)


def make_instructor(_token):
    url = 'http://127.0.0.1:8000/platform/instructors/'
    headers = {'Authorization': f'JWT {_token}'}
    return post(url, headers=headers)


def make_student(_token, user_id):
    url = 'http://127.0.0.1:8000/platform/audiences/'
    json_data = {'user': user_id}
    headers = {'Authorization': f'JWT {_token}'}
    return post(url, json_data=json_data, headers=headers)


def create_category(name, _token):
    url = 'http://127.0.0.1:8000/platform/categories/'
    json_data = {'title': name}
    headers = {'Authorization': f'JWT {_token}'}
    return post(url, json_data, headers)


def enroll_in_a_course(course_id, _token):
    url = f'http://127.0.0.1:8000/platform/courses/{course_id}/enroll/'
    headers = {'Authorization': f'JWT {_token}'}
    return get(url, headers=headers)


def create_course(name,
                  _token,
                  category,
                  provider,
                  description='description',
                  brief_description='',
                  image=None,
                  requirements='requirements',
                  what_will_learn='what_will_learn',
                  status='Pu',
                  duration=datetime.datetime.now()
                  ):
    url = 'http://127.0.0.1:8000/platform/courses/'
    json_data = {'title': name,
                 'category': category,
                 'provider': provider,
                 'description': description,
                 'brief description': brief_description,
                 'image': image,
                 'requirements': requirements,
                 'what_will_learn': what_will_learn,
                 'status': status,
                 'duration': str(duration)[:9],
                 }

    headers = {'Authorization': f'JWT {_token}'}
    return post(url, json_data=json_data, headers=headers)


def create_lecture(title,
                   _token,
                   course_id,
                   brief_description='brief_description',
                   text='text',
                   video='https://www.youtube.com/watch?v=oRrCRTgg8eM&list=RD-8eEf05NykE&index=18',
                   duration=datetime.datetime.now()):
    url = f'http://127.0.0.1:8000/platform/courses/{course_id}/lectures/'
    json_data = {'title': title,
                 'brief_description': brief_description,
                 'text': text,
                 'video': video,
                 'duration': str(duration)[:9],
                 }

    headers = {'Authorization': f'JWT {_token}'}
    return post(url, json_data=json_data, headers=headers)


admin = 'admin'
token = login(admin, admin)['access']
print(admin + ':', token)
create_category('Python', token)
create_category('Java', token)

ins1 = 'ins1'
create_user(ins1)
token = login(ins1)['access']
print(ins1 + ':', token)
make_instructor(token)
create_course('Python1', token, 1, 1)
create_course('Python2', token, 1, 1)
print(create_lecture('lecture1', token, 1))
create_lecture('lecture2', token, 1)
create_lecture('lecture3', token, 2)

ins2 = 'ins2'
create_user(ins2)
token = login(ins2)['access']
print(ins2 + ':', token)
make_instructor(token)
create_course('Java1', token, 1, 2)
create_course('Java2', token, 1, 2)
create_lecture('lecture4', token, 3)

std1 = 'std1'
create_user(std1)
token = login(std1)['access']
make_student(token, 4)
print(std1 + ':', token)
enroll_in_a_course(1, token)
enroll_in_a_course(2, token)

std2 = 'std2'
create_user(std2)
token = login(std2)['access']
make_student(token, 5)
print(std2 + ':', token)
enroll_in_a_course(4, token)
