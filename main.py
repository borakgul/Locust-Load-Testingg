from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 10)

    @task
    def post_user_create(self):
        payload = {
            "id": 123312321,
            "username": "borakgul",
            "firstName": "test",
            "lastName": "akguk",
            "email": "boratest@test.com",
            "password": "123",
            "phone": "121312123123",
            "userStatus": 1
        }
        self.client.post("/v2/user", json=payload)

    @task
    def get_user_info(self):
        self.client.get("/v2/user/borakgul")

    @task
    def get_login(self):
        payload = {
            "username": "borakgul",
            "password": "123"
        }
        self.client.get("/v2/user/login", params=payload)

    @task
    def get_logout(self):
        self.client.get("/v2/user/logout")

    @task
    def put_user_update(self):
        payload = {
            "id": 123312321,
            "username": "borakgul",
            "firstName": "test",
            "lastName": "akguk",
            "email": "boratest@test.com",
            "password": "123",
            "phone": "121312123123",
            "userStatus": 1
        }
        self.client.put("/v2/user/borakgul", json=payload)

    @task
    def delete_user(self):
        payload = {
            "id": 123312321,
            "username": "borakgull",
            "firstName": "test",
            "lastName": "akguk",
            "email": "boratest@test.com",
            "password": "123",
            "phone": "121312123123",
            "userStatus": 1
        }
        self.client.put("/v2/user/borakgull", json=payload)
        self.client.delete("/v2/user/borakgull")

    @task
    def createWithArray(self):
        payload = [{
            "id": 0,
            "username": "sadsadsad",
            "firstName": "sdasd",
            "lastName": "strsadsding",
            "email": "stridsdng",
            "password": "strisdadng",
            "phone": "strisadsdng",
            "userStatus": 0
        }]
        self.client.post("/v2/user/createWithArray", json=payload)