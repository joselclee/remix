from GetAccessToken import get_access_token
from RecommendBySong import recommend_by_song
from RecommendByPlaylist import recommend_by_playlist
from GetData import get_playlist_tracks, get_average_audio_features, get_multiple_audio_features

access_token = get_access_token()
if __name__ == "__main__":
    song = {
        # "id": "7fzHQizxTqy8wTXwlrgPQQ" # Million Dollar Baby by Tommy Richman
        # "id": "4o8EPKaCQ9BvdoEGyQ0lsF" # Beep by Pussy Cat Dolls
        # "id":"5HQEmiV2lKnSO6qa2fsR7x" # I'm not in love by 10cc
        # "id": "2OzhQlSqBEmt7hmkYxfT6m" # Fortnight by Taylor Swift
        "id": "2qSkIjg1o9h3YT9RAgYN75" # Espresso by Sabrina Carpenter
        # "id": "3IqcBL5yjJK3ri0TGaL3MC" # Less of you by Keshi
        # "id": "1upVvXlWQUwAPuLN3oh8lk" # Talk by beabadoobee
        # "id": "4qjLvvBh5ZeKEPyShKRf06" # narcissist by no rome
    }
    playlists = [
        {"id": "3cEYpjA9oz9GiPac4AsH4n"},
        {"id": "4DUUWyqWEXJv3JD0o5wmZf"}
    ]
# avg_features = get_average_audio_features(access_token, [playlist['id'] for playlist in playlists])
# print(avg_features)
recommend_by_playlist(access_token, [playlist['id'] for playlist in playlists])