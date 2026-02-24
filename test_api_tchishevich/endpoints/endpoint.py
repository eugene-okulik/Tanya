import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check response value is the same as sent')
    def check_response_name_is_correct(self, name, value):
        assert self.response.json()[name] == value

    @allure.step('Check response 2 value is the same as sent')
    def check_response_data_is_correct(self, data, name, value):
        assert self.response.json()[data][name] == value

    @allure.step('Check response status code')
    def check_that_status(self, status_code):
        assert self.response.status_code == status_code
