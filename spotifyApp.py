import requests
import json
import os


CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
'grant_type': 'client_credentials',
'client_id': os.environ.get('SPOTIFY_CLIENT_ID'),
'client_secret': os.environ.get('SPOTIFY_CLIENT_SECRET'),
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'
# track_url = input('Enter track url: ')
# start = track_url.find("track") + len("track") +1
# track_id = track_url[start:]

# r = requests.get(BASE_URL + 'tracks/' + track_id, headers=headers)
# tracks/
# audio-features/

# print(json.dumps(r.json(), indent=2))

song_ids = []

for i in range(5):
    url = input('Enter track {} url: '.format(i + 1))
    start = url.find("track") + len("track") +1
    track_id = url[start:]
    song_ids.append(track_id)  # Add each URL to the list

# print(json.dumps(song_ids, indent=3))
#https://open.spotify.com/track/2mqXKSieDASoq4N5739wCz

r = requests.get(BASE_URL + 'recommendations?seed_tracks=' + ','.join(song_ids), headers=headers)

# print(json.dumps(r.json(),indent=3))

data = r.json()
key = "tracks"
tracks = data[key]

for track in tracks:
  print(track['name'])


# for key in r.json().keys():
#   print(key)
#   break
# key = "tracks"
# r.json()[key]

# for i in range(len(r.json()[key])):
#   print(r.json()[key][i]['name'])