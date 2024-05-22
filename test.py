import requests

from encoder import encoded_credentials
song = {
  "album": {
    "album_type": "album",
    "artists": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"
        },
        "href": "https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4",
        "id": "3TVXtAsR1Inumwj472S9r4",
        "name": "Drake",
        "type": "artist",
        "uri": "spotify:artist:3TVXtAsR1Inumwj472S9r4"
      }
    ],
    "available_markets": [
      "AE",
      "AU",
      "BB",
      "BF",
      "BH",
      "BN",
      "BY",
      "CA",
      "DZ",
      "EG",
      "GB",
      "GH",
      "ID",
      "IE",
      "IN",
      "IQ",
      "JO",
      "KG",
      "KR",
      "KW",
      "KZ",
      "LB",
      "LY",
      "MA",
      "MX",
      "MY",
      "NP",
      "OM",
      "PS",
      "QA",
      "SA",
      "SG",
      "TD",
      "TN",
      "TR",
      "UA",
      "US",
      "UZ"
    ],
    "external_urls": {
      "spotify": "https://open.spotify.com/album/42wvKYHFezpmDuAP43558f"
    },
    "href": "https://api.spotify.com/v1/albums/42wvKYHFezpmDuAP43558f",
    "id": "42wvKYHFezpmDuAP43558f",
    "images": [
      {
        "url": "https://i.scdn.co/image/ab67616d0000b273c185e37be2a06b5c6f2dc704",
        "width": 640,
        "height": 640
      },
      {
        "url": "https://i.scdn.co/image/ab67616d00001e02c185e37be2a06b5c6f2dc704",
        "width": 300,
        "height": 300
      },
      {
        "url": "https://i.scdn.co/image/ab67616d00004851c185e37be2a06b5c6f2dc704",
        "width": 64,
        "height": 64
      }
    ],
    "name": "Scorpion",
    "release_date": "2018-06-29",
    "release_date_precision": "day",
    "total_tracks": 25,
    "type": "album",
    "uri": "spotify:album:42wvKYHFezpmDuAP43558f"
  },
  "artists": [
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"
      },
      "href": "https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4",
      "id": "3TVXtAsR1Inumwj472S9r4",
      "name": "Drake",
      "type": "artist",
      "uri": "spotify:artist:3TVXtAsR1Inumwj472S9r4"
    }
  ],
  "available_markets": [
    "AE",
    "AU",
    "BB",
    "BF",
    "BH",
    "BN",
    "BY",
    "CA",
    "DZ",
    "EG",
    "GB",
    "GH",
    "ID",
    "IE",
    "IN",
    "IQ",
    "JO",
    "KG",
    "KR",
    "KW",
    "KZ",
    "LB",
    "LY",
    "MA",
    "MX",
    "MY",
    "NP",
    "OM",
    "PS",
    "QA",
    "SA",
    "SG",
    "TD",
    "TN",
    "TR",
    "UA",
    "US",
    "UZ"
  ],
  "disc_number": 2,
  "duration_ms": 217925,
  "explicit": "false",
  "external_ids": {
    "isrc": "USCM51800207"
  },
  "external_urls": {
    "spotify": "https://open.spotify.com/track/0h1W19pS59KtEd7aDzF58i"
  },
  "href": "https://api.spotify.com/v1/tracks/0h1W19pS59KtEd7aDzF58i",
  "id": "0h1W19pS59KtEd7aDzF58i",
  "is_local": "false",
  "name": "In My Feelings",
  "popularity": 50,
  "preview_url": "https://p.scdn.co/mp3-preview/dd67abd521bc069758ab0708ccaed608401fe5f5?cid=cfe923b2d660439caf2b557b21f31221",
  "track_number": 9,
  "type": "track",
  "uri": "spotify:track:0h1W19pS59KtEd7aDzF58i"
}

def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    
    if response.status_code == 200:
        return response_data["access_token"]
    else:
        raise Exception("Couldn't get access token", response_data)

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
    
# recommend song via content based filtering
def recommend_song(access_token, song):
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
        "min_loudness": data["loudness"] - 0.3,
        # "max_loudness": data["loudness"] + 0.1,
        # "min_speechiness": data["speechiness"] - 0.1,
        # "max_speechiness": data["speechiness"] + 0.1,
        "min_tempo": data["tempo"] - 10,
        "max_tempo": data["tempo"] + 10,
        # "target_tempo": data["tempo"],
        "min_valence": data["valence"] - 0.2,
        "max_valence": data["valence"] + 0.2,
        # "target_valence": data["valence"],
        "min_time_signature": data["time_signature"] - 4,
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
    
    
if __name__ == "__main__":
    song1 = {
        # "id": "7fzHQizxTqy8wTXwlrgPQQ"
        # "id": "4o8EPKaCQ9BvdoEGyQ0lsF"
        # "id":"5HQEmiV2lKnSO6qa2fsR7x"
        "id": "2OzhQlSqBEmt7hmkYxfT6m" # Fortnight Taylor Swift
        # "id": "2qSkIjg1o9h3YT9RAgYN75" # Espresso Sabrina Carpenter
    }
    recommend_song(get_access_token(), song1)