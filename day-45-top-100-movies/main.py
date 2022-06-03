import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

movies_list = soup.find_all(name="h3", class_="title")
ordered_list = movies_list[::-1]
ordered_list_text = [movie.getText() for movie in ordered_list]

print(ordered_list_text)

with open("movies.txt", mode="w") as file:
    [file.write(f"{movie}\n") for movie in ordered_list_text]
