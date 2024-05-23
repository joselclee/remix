import requests
import numpy as np

from Encoder import encoded_credentials
from GetAccessToken import get_access_token

access_token = get_access_token()

def clean_playlist(playlist):
    cleaned_data = []
    for item in playlist['items']:
        track = item['track']
        cleaned_data.append({
            'track_id': track['id']
        })
    return cleaned_data

# This function gets a track.
def get_track(access_token, song_id):
    api_url = f"https://api.spotify.com/v1/tracks/{song_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(api_url, headers=headers)
    results = response.json()

    if response.status_code == 200:
        return results
    else:
        raise Exception("Couldn't get track", results)

# This function gets the audio features of a track.
def get_track_audio_features(access_token, song_id):
    api_url = f"https://api.spotify.com/v1/audio-features/{song_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(api_url, headers=headers)
    results = response.json()
    if response.status_code == 200:
        return results
    else:
        raise Exception("Couldn't get track audio features", results)
    
def get_multiple_audio_features(access_token, song_ids):
    api_url = f'https://api.spotify.com/v1/audio-features?ids={",".join(song_ids)}'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(api_url, headers=headers)
    results = response.json()
    if response.status_code == 200:
        return results
    else:
        raise Exception("Couldn't get track audio features", results)
    
# This function gets the tracks in a playlist.
def get_playlist_tracks(access_token, playlist_id):
    api_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(api_url, headers=headers)
    results = response.json()
    cleaned_results = clean_playlist(results)
    print(cleaned_results)
    
    if response.status_code == 200:
        return cleaned_results
    else:
        raise Exception("Couldn't get playlist tracks", cleaned_results)

# This function calculates the average audio features of the tracks in a list of playlists.
def get_average_audio_features(access_token, playlist_ids):
    all_features = []
    tracks = []
    
    for playlist in playlist_ids:
        
        tracks.extend(get_playlist_tracks(access_token, playlist))
        
        # Split track IDs into chunks of 100
        track_ids = [track['track_id'] for track in tracks]
        track_id_chunks = [track_ids[i:i + 100] for i in range(0, len(track_ids), 100)]
        
        # Get features for each chunk
        for chunk in track_id_chunks:
            features = get_multiple_audio_features(access_token, chunk)
            all_features.extend(features)
        
    average_features = {}
    
    for feature in all_features[0].keys():
        average_features[feature] = np.mean([track[feature] for track in all_features])
        
    return average_features