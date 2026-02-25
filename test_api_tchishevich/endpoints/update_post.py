import requests
import allure

from test_api_tchishevich.endpoints.endpoint import Endpoint


class UpdatePost(Endpoint):

    @allure.step('Update a post')
    def update_post(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response


class PatchPost(Endpoint):

    @allure.step('Patch a post')
    def patch_post(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{post_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
