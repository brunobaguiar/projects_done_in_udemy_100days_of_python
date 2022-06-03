import requests
from datetime import datetime

USERNAME = "your_pixela_user_name"
TOKEN = "your_pixela_token"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora",
}

# Authenticating myself with a password, without open this to the browser
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

create_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

create_date = datetime(year=year, month=month, day=day)

create_pixel_config = {
    "date": create_date.strftime("%Y%m%d"),
    "quantity": input("How many hours did you studied today? "),
}

# POST RESPONSE
response = requests.post(url=create_pixel_endpoint, json=create_pixel_config, headers=headers)
print(response.text)



























update_date = datetime(year=2022, month=4, day=18)

update_pixel_endpoint = f"{create_pixel_endpoint}/{update_date.strftime('%Y%m%d')}"

update_pixel_config = {
    "quantity": "5",
}


# UPDATE RESPONSE
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

delete_date = datetime(year=2022, month=4, day=10)

delete_pixel_endpoint = f"{create_pixel_endpoint}/{delete_date.strftime('%Y%m%d')}"

#DELETE RESPONSE
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
