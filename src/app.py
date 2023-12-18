import requests
from dotenv import load_dotenv
import os
import spotipy


# Load environment variables from .env file
load_dotenv()


# Spotify API credentials
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

def get_spotify_token(client_id, client_secret):
    """Get the access token from Spotify"""
    url = "https://accounts.spotify.com/api/token"
    payload = {'grant_type': 'client_credentials'}
    headers = {'Authorization': f'Basic {client_id}:{client_secret}'}

    response = requests.post(url, headers=headers, data=payload)
    return response.json().get('access_token')

def get_top_tracks(artist_id, token):
    """Get the top tracks of an artist from Spotify"""
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(url, headers=headers)
    return response.json()

# Replace with your Spotify Client ID and Client Secret
client_id = CLIENT_ID
client_secret = CLIENT_SECRET

# Replace with the artist's Spotify ID
artist_id = 'YOUR_ARTIST_ID_HERE'

# Get access token
token = get_spotify_token(client_id, client_secret)

# Get top tracks
top_tracks = get_top_tracks(artist_id, token)

# Print the top 10 tracks
for track in top_tracks['tracks'][:10]:
    print(track['name'])
