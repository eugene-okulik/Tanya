from http import HTTPStatus

from test_api_tchishevich.utils.data import configure_data

import allure
import pytest

test_data = [
    ("Tanya", {"age": 33, "specialty": "Automation Tester"}),
    ("New Tanya", {"age": 34, "specialty": "New Tester"}),
    ("Update Tanya", {"age": 35, "specialty": "Updating Tester"}),
]


@allure.feature("Test API")
@allure.story("Create Posts")
@allure.title("Create 3 posts")
@pytest.mark.critical
@pytest.mark.parametrize("name, data", test_data)
def test_create_object(create_post_endpoint, name, data):
    create_post_endpoint.create_new_post(payload=configure_data(name, data))
    create_post_endpoint.check_that_status(HTTPStatus.OK)
    create_post_endpoint.check_response_name_is_correct(name='name', value=name)


@allure.feature("Test API")
@allure.story("Get Posts")
@allure.title("Get posts with id user")
def test_get_object(get_post_endpoint, post_id):
    get_post_endpoint.get_post(post_id)
    get_post_endpoint.check_that_status(HTTPStatus.OK)
    get_post_endpoint.check_response_name_is_correct(name='id', value=post_id)


test_data1 = [
    ("Tanya object update", {"age": 36, "specialty": "Tester update"})
]


@allure.feature("Test API")
@allure.story("Change Posts")
@allure.title("Change all parameters posts")
@pytest.mark.critical
@pytest.mark.parametrize("name, data", test_data1)
def test_put_object(update_post_endpoint, post_id, name, data):
    update_post_endpoint.update_post(post_id, payload=configure_data(name, data))
    update_post_endpoint.check_that_status(HTTPStatus.OK)
    update_post_endpoint.check_response_name_is_correct(name='name', value=name)
    update_post_endpoint.check_response_data_is_correct(data='data', name='age', value=36)
    update_post_endpoint.check_response_data_is_correct(data='data', name='specialty', value='Tester update')


@allure.feature("Test API")
@allure.story("Change Posts")
@allure.title("Change the specified parameters posts")
@pytest.mark.medium
def test_patch_object(patch_post_endpoint, post_id):
    body = {
        "name": "Tanya object - UPD patch"
    }
    patch_post_endpoint.patch_post(post_id, payload=body)
    patch_post_endpoint.check_that_status(HTTPStatus.OK)
    patch_post_endpoint.check_response_name_is_correct(name='name', value=body["name"])
    patch_post_endpoint.check_response_data_is_correct(data='data', name='age', value=33)
    patch_post_endpoint.check_response_data_is_correct(data='data', name='specialty', value='Tester')


@allure.feature("Test API")
@allure.story("Delete Posts")
@allure.title("Delete posts with id user")
def test_delete_object(delete_post_endpoint, post_id):
    delete_post_endpoint.delete_post(post_id)
    delete_post_endpoint.check_that_status(HTTPStatus.OK)
