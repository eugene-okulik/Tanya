import pytest
import requests


@pytest.fixture()
def new_post_id():
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
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('\ndeleting object')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


def test_get_object(new_post_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_post_id}').json()
    assert response['id'] == new_post_id


test_data = [
    ("Tanya", {"age": 33, "specialty": "Automation Tester"}),
    ("New Tanya", {"age": 34, "specialty": "New Tester"}),
    ("Update Tanya", {"age": 35, "specialty": "Updating Tester"}),
]


@pytest.mark.critical
@pytest.mark.parametrize("name, data", test_data)
def test_put_object(new_post_id, name, data):
    body = {
        "name": name,
        "data": data
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_post_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200


@pytest.mark.medium
def test_patch_object(new_post_id):
    body = {
        "name": "Tanya object - UPD patch"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_post_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()['name'] == 'Tanya object - UPD patch'
