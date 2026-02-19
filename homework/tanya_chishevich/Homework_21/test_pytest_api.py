import pytest
import requests
import allure

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
def test_create_object(name, data):
    with allure.step('Prepare test data for creating'):
        body = {
            "name": name,
            "data": data
        }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Run request to create a post'):
        response = requests.post(
            'http://objapi.course.qa-practice.com/object',
            json=body,
            headers=headers
        )
    post_id = response.json()['id']
    print(post_id)
    with allure.step('Check name of create post'):
        assert response.json()['name'] == name
    with allure.step('Check create status 200'):
        assert response.status_code == 200


@allure.feature("Test API")
@allure.story("Get Posts")
@allure.title("Get posts with id user")
def test_get_object(new_post_id):
    with allure.step(f'Run get request for post with id {new_post_id}'):
        response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_post_id}').json()
    with allure.step(f'Check that post id is {new_post_id}'):
        assert response["id"] == new_post_id


@allure.feature("Test API")
@allure.story("Change Posts")
@allure.title("Change all parameters posts")
@pytest.mark.critical
def test_put_object(new_post_id):
    with allure.step('Prepare test data for puting'):
        body = {
            "name": "Tanya object update",
            "data": {"age": 36, "specialty": "Tester update"}
        }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Run request to put a post'):
        response = requests.put(
            f'http://objapi.course.qa-practice.com/object/{new_post_id}',
            json=body,
            headers=headers
        )
    with allure.step('Check put status 200'):
        assert response.status_code == 200
    with allure.step('Check name of put post'):
        assert response.json()['name'] == "Tanya object update"
    with allure.step('Check age of put post'):
        assert response.json()['data']['age'] == 36
    with allure.step('Check specialty of put post'):
        assert response.json()['data']['specialty'] == 'Tester update'


@allure.feature("Test API")
@allure.story("Change Posts")
@allure.title("Change the specified parameters posts")
@pytest.mark.medium
def test_patch_object(new_post_id):
    with allure.step('Prepare test data for patching'):
        body = {
            "name": "Tanya object - UPD patch"
        }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Run request to patch a post'):
        response = requests.patch(
            f'http://objapi.course.qa-practice.com/object/{new_post_id}',
            json=body,
            headers=headers
        )
    with allure.step('Check patch status 200'):
        assert response.status_code == 200
    with allure.step('Check name of patch post'):
        assert response.json()['name'] == 'Tanya object - UPD patch'
    with allure.step('Check age of patch post'):
        assert response.json()['data']['age'] == 33
    with allure.step('Check specialty of patch post'):
        assert response.json()['data']['specialty'] == 'Tester'


@allure.feature("Test API")
@allure.story("Delete Posts")
@allure.title("Delete posts with id user")
def test_delete_object(new_post_id):
    with allure.step(f'Run delete request for post with id {new_post_id}'):
        response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_post_id}')
    with allure.step('Check post status 200'):
        assert response.status_code == 200
    print(response.content)


@allure.feature("Print")
def test_other():
    print("Это проверочный тест")
