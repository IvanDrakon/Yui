import requests
from datetime import datetime
from key import pixela_token

USERNAME = "drakon"
TOKEN = pixela_token
headers = {"X-USER-TOKEN": TOKEN}
pixela_endpoint = "https://pixe.la/v1/users"
graph_id = "graph2"
QUANTITY = 0


def create_account():
    parameters = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response_account = requests.post(pixela_endpoint, json=parameters)
    print(response_account.text)


def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    parameters_graph = {
        "id": graph_id,
        "name": "Programming Graph",
        "unit": "Minutes",
        "type": "int",
        "color": "sora",
    }
    response_graph = requests.post(graph_endpoint, json=parameters_graph, headers=headers)
    print(response_graph.text)


def update_graph(**kwargs):
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
    response_update = requests.put(update_endpoint, json=kwargs, headers=headers)
    print(response_update.text)


def create_pixel(quantity):
    post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
    today = datetime.today()
    today_formated = today.strftime("%Y%m%d")
    parameters_pixel = {
        "date": today_formated,
        "quantity": quantity
    }
    response_pixel = requests.post(post_pixel_endpoint, json=parameters_pixel, headers=headers)
    print(response_pixel.text)


def update_pixel(date, **kwargs):
    # quantity & optionalData
    update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{date}"
    response_update_pixel = requests.put(update_pixel_endpoint, json=kwargs, headers=headers)
    print(response_update_pixel.text)


def delete_pixel(date):
    delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{date}"
    response_delete_pixel = requests.delete(delete_pixel_endpoint, headers=headers)
    print(response_delete_pixel.text)
