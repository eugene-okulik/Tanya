import allure


def configure_data(name, data):
    with allure.step('Prepare test data for creating'):
        body = {
            "name": name,
            "data": data
        }
    return body
