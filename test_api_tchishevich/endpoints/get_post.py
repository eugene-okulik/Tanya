import requests
import allure

from test_api_tchishevich.endpoints.endpoint import Endpoint


class GetPost(Endpoint):
    post_id = None

    @allure.step('Get post with id')
    def get_post(self, post_id):
        self.response = requests.get(
            f'{self.url}/{post_id}'
        )
        return self.response
