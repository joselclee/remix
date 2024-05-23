import requests

from GetAccessToken import get_access_token
from GetData import get_average_audio_features

access_token = get_access_token()

# This function recommends tracks based on the audio features of the tracks in a list of playlists.
def recommend_by_playlist(access_token, playlist_ids):
    data = get_average_audio_features(access_token, playlist_ids)
    api_url = f"https://api.spotify.com/v1/recommendations"
    headers = { 
        "Authentication": f"Bearer {access_token}"
    }
    params = {
        "limit": 10,
        "market": "ES",
        "min_acousticness": data["acousticness"] - 0.1,
        "max_acousticness": data["acousticness"] + 0.1,
        "target_acousticness": data["acousticness"],
        "min_danceability": data["danceability"] - 0.35,
        "max_danceability": data["danceability"] + 0.1,
        "target_danceability": data["danceability"],
        "min_energy": data["energy"] - 0.25,
        "max_energy": data["energy"] + 0.1,
        "target_energy": data["energy"],
        "min_instrumentalness": data["instrumentalness"] - 0.1,
        "max_instrumentalness": data["instrumentalness"] + 0.1,
        "target_instrumentalness": data["instrumentalness"],
        "min_liveness": data["liveness"] - 0.25,
        "max_liveness": data["liveness"] + 0.1,
        "target_liveness": data["liveness"],
        "min_loudness": data["loudness"] - 5,
        "max_loudness": data["loudness"] + 0.1,
        "target_loudness": data["loudness"],
        "min_speechiness": data["speechiness"] - 0.1,
        "max_speechiness": data["speechiness"] + 0.1,
        "target_speechiness": data["speechiness"],
        "min_tempo": data["tempo"] - 10,
        "max_tempo": data["tempo"] + 10,
        "target_tempo": data["tempo"],
        "min_valence": data["valence"] - 0.1,
        "max_valence": data["valence"] + 0.1,
        "target_valence": data["valence"],
        "min_time_signature": data["time_signature"] - 3,
        "max_time_signature": data["time_signature"] + 2,
        "target_time_signature": data["time_signature"],
    }