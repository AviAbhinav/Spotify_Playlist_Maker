import csv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_song_uri(sp, song_name):
    """Search for a song on Spotify and return its URI."""
    results = sp.search(q=song_name, limit=1, type='track')
    tracks = results['tracks']['items']
    return tracks[0]['uri'] if tracks else None

def read_songs_from_csv(file_path):
    """Read song names from a CSV file."""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader if row]

def create_spotify_playlist(file_path):
    """Read songs from CSV, fetch URIs, and create a Spotify playlist."""
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="your_client_id",  #Client ID from Spotify For Developers
        client_secret="your_client_secret",  #Client Secret Spotify For Developers
        redirect_uri="http://localhost:8888/callback",
        scope="playlist-modify-public"
    ))
    
    user = sp.current_user()
    playlist = sp.user_playlist_create(user['id'], "My Custom Playlist", public=True)  #Playlist Name
    
    song_names = read_songs_from_csv(file_path)
    song_uris = [get_song_uri(sp, song) for song in song_names]
    song_uris = [uri for uri in song_uris if uri]  
    
    if song_uris:
        sp.playlist_add_items(playlist['id'], song_uris)
        print(f"Playlist created: {playlist['external_urls']['spotify']}")
    else:
        print("No valid songs found.")

if __name__ == "__main__":
    csv_file_path = "songs_list.csv"  # CSV file path
    create_spotify_playlist(csv_file_path)
