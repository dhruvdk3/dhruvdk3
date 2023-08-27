from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
Client_id = "client id"
Client_secret = "client secret"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com",
        client_id=Client_id,
        client_secret=Client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="Dhruv", 
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
year = date.split("-")[0]
web_data = response.text
soup = BeautifulSoup(web_data, 'html.parser')
data = soup.select(selector='li ul li h3', id = "title-of-a-story")
song_names = [(i.getText()).strip() for i in data]

song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
