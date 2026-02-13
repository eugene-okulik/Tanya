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


@pytest.fixture(scope="session", autouse=True)
def print_test_status():
    print("\n>>> Start testing")
    yield
    print("\n>>> Testing completed")


@pytest.fixture(autouse=True)
def run_before_after_tests():
    print("\nbefore test")
    yield
    print("\nafter test")
