from locust import task, HttpUser
import random


class ApiTestObject(HttpUser):
    created_object_ids = []

    def on_start(self):
        print("Start testing object")

    @task(3)
    def create_object(self):
        payload = {
            "name": "Tanya check object locust",
            "data": {"age": 33, "specialty": "Tester"}
        }

        response = self.client.post("/object", json=payload)

        if response.status_code == 200:
            object_id = response.json().get("id")
            if object:
                self.created_object_ids.append(object_id)
                print(f"Created object with ID: {object_id}")
        else:
            response.failure(f"Failed to create object with status code: {response.status_code}")

    @task(5)
    def get_all_objects(self):
        self.client.get(
            '/object'
        )

    @task(5)
    def get_object(self):
        if self.created_object_ids:
            object_id = random.choice(self.created_object_ids)
            self.client.get(
                f"/object/{object_id}"
            )

    @task(1)
    def put_object(self):

        payload = {
            "name": "Updated Tanya check object locust",
            "data": {"age": 36, "specialty": "Tester locust"}
        }

        if self.created_object_ids:
            object_id = random.choice(self.created_object_ids)
            response = self.client.put(f"/object/{object_id}", json=payload)
            if response.status_code == 200:
                response_name_json = response.json().get('name')
                response_data_json = response.json().get('data')
                print(f"Successfully updated object with ID: {object_id} with name: {response_name_json}"
                      f" and data: {response_data_json}")
            else:
                response.failure(f"Failed to create object with status code: {response.status_code}")

    @task(1)
    def patch_object(self):

        payload = {
            "name": "Tanya object - UPD patch"
        }

        if self.created_object_ids:
            object_id = random.choice(self.created_object_ids)
            response = self.client.patch(f"/object/{object_id}", json=payload)
            if response.status_code == 200:
                response_name_json = response.json().get('name')
                response_data_json = response.json().get('data')
                print(f"Successfully patched object with ID: {object_id} with name: {response_name_json}"
                      f" and data: {response_data_json}")
            else:
                response.failure(f"Failed to create object with status code: {response.status_code}")

    @task(1)
    def delete_object(self):
        if self.created_object_ids:
            object_id = self.created_object_ids.pop(0)
            self.client.delete(
                f"/object/{object_id}"
            )
            print(f"Deleted item with ID: {object_id}")

    def on_stop(self):
        print("Stop testing object")
