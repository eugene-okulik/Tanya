import pytest

from endpoints.create_post import CreatePost
from endpoints.get_post import GetPost
from endpoints.update_post import UpdatePost, PatchPost
from endpoints.delete_post import DeletePost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def get_post_endpoint():
    return GetPost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


test_data = [
    ("Tanya object", {"age": 33, "specialty": "Tester"})
]


@pytest.fixture()
def post_id(create_post_endpoint, get_post_endpoint, delete_post_endpoint):
    payload = {
        "name": "Tanya object",
        "data": {"age": 33, "specialty": "Tester"}
    }
    create_post_endpoint.create_new_post(payload)
    yield create_post_endpoint.post_id
    obj = get_post_endpoint.get_post(create_post_endpoint.post_id)
    if obj:
        print('\ndeleting object')
        delete_post_endpoint.delete_post(create_post_endpoint.post_id)
