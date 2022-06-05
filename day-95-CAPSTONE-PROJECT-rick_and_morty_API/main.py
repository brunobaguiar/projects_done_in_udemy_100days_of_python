import requests
import pandas as pd
from search import Search

# Rick and Morty endpoints
base_url = "https://rickandmortyapi.com/api/"
character_url = base_url + "character/"
location_url = base_url + "location/"
episode_url = base_url + "episode/"


# TODO 0 Uncomment TODOS 1, 2 e 3 in the first time you run the app, to build the csv files for database
# TODO 1 Database of all characters
# all_characters = {}
# for i in range(1, 827):
#     response = requests.get(f"{character_url}/{i}").json()
#     all_characters[i] = response
# characters_df = pd.DataFrame(all_characters).T
# characters_df.to_csv('rick_and_morty_characters.csv', index=False, encoding='utf-8')

# TODO 2 Database of all locations
# all_locations = {}
# for i in range(1, 127):
#     response = requests.get(f"{location_url}/{i}").json()
#     all_locations[i] = response
# characters_df = pd.DataFrame(all_locations).T
# characters_df.to_csv('rick_and_morty_locations.csv', index=False, encoding='utf-8')

# TODO 3 Database of all episodes
# all_episodes = {}
# for i in range(1, 52):
#     response = requests.get(f"{episode_url}/{i}").json()
#     all_episodes[i] = response
# characters_df = pd.DataFrame(all_episodes).T
# characters_df.to_csv('rick_and_morty_episodes.csv', index=False, encoding='utf-8')

# TODO 4 Characters Schema
character = Search("character")
print(character.schema)

# TODO 5 Locations Schema
location = Search("location")
print(location.schema)

# TODO 6 Episodes Schema
episode = Search("episode")
print(episode.schema)

# TODO 7 Get all characters ID's
character.get_all_names()

# TODO 8 Find character ID by name
character_name_to_find_ID = "Morty Smith"
character.find_ID_by_name(character_name_to_find_ID)

# TODO 9 Find character by ID
character_id_to_find = 2
print(character.find_by_id(character_id_to_find))

# TODO 10 Get all locations ID's
location.get_all_names()

# TODO 11 Find location ID by name
location_name_to_find_ID = "Slartivart"
location.find_ID_by_name(location_name_to_find_ID)

# TODO 12 Find location by ID
location_id_to_find = 124
print(location.find_by_id(location_id_to_find))

# TODO 10 Get all episodes ID's
episode.get_all_names()

# TODO 11 Find episode ID by name
episode_name_to_find_ID = "Rickdependence Spray"
episode.find_ID_by_name(episode_name_to_find_ID)

# TODO 12 Find episode by ID
episode_id_to_find = 45
print(episode.find_by_id(episode_id_to_find))
