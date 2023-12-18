import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import seaborn as sns


# Load environment variables from .env file
load_dotenv()


# Spotify API credentials
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# Set up Spotipy client with Client Credentials Flow
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_top_tracks(artist_id):
    """Get the top tracks of an artist from Spotify using Spotipy"""
    # Using Spotipy to get top tracks
    results = sp.artist_top_tracks(artist_id, country='US')

    # Extracting track details
    tracks_data = []
    for track in results['tracks'][:10]:
        track_details = {
            'Name': track['name'],
            'Album': track['album']['name'],
            'Release_Date': track['album']['release_date'],
            'Popularity': track['popularity'],
            'Duration_(ms)': track['duration_ms'],
            'Explicit': track['explicit'],
            'Spotify_URL': track['external_urls']['spotify']
        }
        tracks_data.append(track_details)

    return tracks_data


# Replace with the artist's Spotify ID
artist_id = '20qISvAhX20dpIbOOzGK3q'

# Get top tracks data using Spotipy
top_tracks_data = get_top_tracks(artist_id)

# Creating a DataFrame
df_tracks = pd.DataFrame(top_tracks_data)

# Display the DataFrame
print(df_tracks)

# Display the scatter plot
scatter_plot = sns.scatterplot(data = df_tracks, x = "Popularity", y = "Duration_(ms)")
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")
