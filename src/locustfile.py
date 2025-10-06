from locust import FastHttpUser, task, between

class ProductUser(FastHttpUser):
    wait_time = between(1, 3)

    @task(5)
    def get_products(self):
        self.client.get("/products")

    @task(1)
    def create_product(self):
        self.client.post("/products", json={
            "name": "Test Product",
            "price": 9.99,
            "stock": 5
        })