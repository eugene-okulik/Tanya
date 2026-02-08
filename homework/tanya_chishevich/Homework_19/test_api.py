import requests


def create_object():
    body = {
        "name": "Tanya object",
        "data": {"age": 33, "specialty": "Tester"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    return response.json()['id']


def get_object(post_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{post_id}')
    print(response.status_code)


def put_object(post_id):
    body = {
        "name": "Tanya object - UPD get",
        "data": {"age": 33, "specialty": "Tester - UPD get"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Tanya object - UPD get'
    print(response)


def patch_object(post_id):
    body = {
        "name": "Tanya object - UPD patch"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Tanya object - UPD patch'
    print(response)


def delete_object(post_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    print(response.status_code)


new_id = create_object()
print(new_id)
put_object(new_id)
patch_object(new_id)
delete_object(new_id)
get_object(new_id)
