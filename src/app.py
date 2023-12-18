import os
import base64
import requests
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Spotify API credentials
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def get_spotify_token(client_id, client_secret):
    """Get the access token from Spotify"""
    url = "https://accounts.spotify.com/api/token"

    # Encode Client ID and Secret
    client_creds = f"{client_id}:{client_secret}"
    client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

    payload = {'grant_type': 'client_credentials'}
    headers = {'Authorization': f'Basic {client_creds_b64}'}

    response = requests.post(url, headers=headers, data=payload)
    
    # Check if the request was successful
    if response.status_code != 200:
        return None

    return response.json().get('access_token')


def get_top_tracks(artist_id, token):
    """Get the top tracks of an artist from Spotify"""
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(url, headers=headers)
    return response.json()


# Replace with the artist's Spotify ID
artist_id = '20qISvAhX20dpIbOOzGK3q'

# Get access token
token = get_spotify_token(CLIENT_ID, CLIENT_SECRET)

# Get top tracks
top_tracks = get_top_tracks(artist_id, token)

# Print the top 10 tracks
for track in top_tracks['tracks'][:10]:
    print(track['name'])
