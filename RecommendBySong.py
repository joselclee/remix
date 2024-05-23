import requests
 
from GetAccessToken import get_access_token
from GetData import get_track_audio_features

access_token = get_access_token

def recommend_by_song(access_token, song):
    data = get_track_audio_features(access_token, song["id"])
    api_url = f"https://api.spotify.com/v1/recommendations"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {        
        "limit": 10,
        "market": "ES",
        # "seed_artists": song["artists"][0]["id"],
        # "seed_genres": song['genres'],
        "seed_tracks": song["id"],
        # "min_acousticness": data["acousticness"] - 0.1,
        # "max_acousticness": data["acousticness"] + 0.1,
        # "target_acousticness": data["acousticness"],
        "min_danceability": data["danceability"] - 0.35,
        # "max_danceability": data["danceability"] + 0.1,
        # "target_danceability": data["danceability"],
        "min_energy": data["energy"] - 0.25,
        # "max_energy": data["energy"] + 0.1,
        # "target_energy": data["energy"],
        # "min_instrumentalness": data["instrumentalness"] - 0.1,
        # "max_instrumentalness": data["instrumentalness"] + 0.1,
        # "target_instrumentalness": data["instrumentalness"],
        "min_liveness": data["liveness"] - 0.25,
        # "max_liveness": data["liveness"] + 0.1,
        # "target_liveness": data["liveness"],
        "min_loudness": data["loudness"] - 5,
        # "max_loudness": data["loudness"] + 0.1,
        "min_speechiness": data["speechiness"] - 0.1,
        # "max_speechiness": data["speechiness"] + 0.1,
        "min_tempo": data["tempo"] - 10,
        "max_tempo": data["tempo"] + 10,
        # "target_tempo": data["tempo"],
        "min_valence": data["valence"] - 0.1,
        "max_valence": data["valence"] + 0.1,
        # "target_valence": data["valence"],
        "min_time_signature": data["time_signature"] - 3,
        # "max_time_signature": data["time_signature"] + 2,
        # "target_time_signature": data["time_signature"],
    }
    response = requests.get(api_url, headers=headers, params=params)
    results = response.json()
    if response.status_code == 200:
        print("Recommended songs:")
        for track in results["tracks"]:
            print(f"{track['name']} by {track['artists'][0]['name']}")
    else:
        raise Exception("Couldn't get recommendations", results)