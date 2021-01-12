import os
from youtube_client import YoutubeClient
from spotifyInfo import SpotifyClient
def run():
    #Get a list of playlists from youtube
    youtube_client = YoutubeClient('./credentials/client_secret.json')
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlists = youtube_client.get_playlists()

    #Ask which playlists we want to get music from youtube
    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")

    #Get song info for every song in the playlist from youtube
    songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print(f"Adding {len(songs)}")
    #Search for the song on spotify
    for song in songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                print(f"Added {song.artist} - {song.track} to your spotify liked songs")
    # If song found, add to spotify liked songs

if __name__ == '__main__':
    run()
