import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID: "bf494b4ee982443a8424c5dbf9668829"
SPOTIFY_CLIENT_SECRET: "e0c3101530ed4d278a6621ad2e316dd0"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(f"{URL}/{date}/")
webpage_html = response.text

soup = BeautifulSoup(webpage_html, "html.parser")

raw_song_list = []
song_list = []

songs = soup.find_all("h3", class_="a-no-trucate")

for tag in songs: raw_song_list.append(tag.getText())
for song in raw_song_list: song_list.append(song.replace("\n", "").replace("\t", ""))

print(song_list)

scope = "user-library-read"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="bf494b4ee982443a8424c5dbf9668829",
        client_secret="e0c3101530ed4d278a6621ad2e316dd0",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
