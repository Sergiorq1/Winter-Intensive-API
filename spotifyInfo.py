import requests
import urllib.parse

class SpotifyClient(object):
    def __init__(self):
        self.token = token

    def search_song(self, artist, track):
        query = urllib.parse.quote(f'{artist} {track}')
        url = f"https://api.spotify.com/v1/search?q={url}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }
        )
        response_json = response.json()
        if results:
            #assuming the first result is the one desired
            return results[0]['id']
        else:
            raise Exception(f"No song found for {artist} = {track}")
    
    def add_song_to_spotify(self, song_id):
        url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(
            url,
            json={
                "ids": [song_id]
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }
        )
        return response.ok
