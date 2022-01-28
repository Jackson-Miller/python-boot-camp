import os
import spotipy
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Ask the user for a date and then scrape the Billboard top 100 site for the song titles
date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_uri = f"https://www.billboard.com/charts/hot-100/{date_input}"
response = requests.get(billboard_uri)
soup = BeautifulSoup(response.text, "html.parser")
song_titles = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
top_100 = []

for song in song_titles:
    top_100.append(song.getText().strip())

# Search for each song on Spotify and add the songs to a playlist
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8080",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path=".cache"
    )
)
user_id = sp.current_user()["id"]
song_uris = []
for title in top_100:
    song_data = sp.search(type="track", q=title)
    try:
        song_uris.append(song_data["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"Spotify doesn't have this banger, {title}")

playlist = sp.user_playlist_create(user=user_id, public=False, name=f"{date_input} Billboard 100", description=f"The Billboard 100 list from {date_input}")
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(playlist["external_urls"])
