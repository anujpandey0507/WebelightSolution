from locust import HttpUser, TaskSet, task, between, LoadTestShape


class Website(TaskSet):

    @task
    def home_page(self):
        self.client.get("https://www.webelight.co.in/")

    @task
    def careers(self):
        self.client.get("https://www.webelight.co.in/career")

    @task
    def contact_us(self):
        self.client.get("https://www.webelight.co.in/contact-us")


class Customer(HttpUser):
    host = "https://www.webelight.co.in/"
    tasks = [Website]
    wait_time = (5)
