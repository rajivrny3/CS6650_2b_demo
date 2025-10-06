from locust import HttpUser, task, between

class ProductUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def get_products(self):
        self.client.get("/products")

    @task(1)
    def get_product_by_id(self):
        self.client.get("/products/1")  # change ID as needed

    @task(1)
    def create_product(self):
        self.client.post("/products", json={
            "name": "Test Product",
            "price": 9.99
            "stock": 5
        })