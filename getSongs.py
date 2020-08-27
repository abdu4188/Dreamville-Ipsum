import lyricsgenius
import json

artists = [
    {
        'name':'Cozz',
        'file': 'Cozz'
    }, 
    {
        'name':'Abbas Hamad',
        'file': 'Bas'
    },
    {
        'name': 'AriLennox',
        'file': 'AriLennox',
    },
    {
        'name': 'J. cole',
        'file': 'J.Cole',
    },
    {
        'name': 'JID',
        'file': 'JID',
    }, 
    {
        'name': 'Lute',
        'file': 'Lute',
    },
    {
        'name': 'EarthGang',
        'file': 'EARTHGANG',
    },
    {
        'name': 'Omen',
        'file': 'Omen',
    }
]

lyricsList = []

for selectedArtist in artists:
    genius = lyricsgenius.Genius(
    "HBLNRdl6oUI2cIduP-Ffs91AWBt0NV1lut7QHN6KE7M0jk_EGJ0SVd6lyl_nRU9A", timeout=500)
    artist = genius.search_artist(selectedArtist['name'], max_songs=100,)

    artist.save_lyrics()

    with open('Lyrics_'+selectedArtist['file']+'.json') as f:
        data = json.load(f)

    for song in data['songs']:
        if song['lyrics'] != None:
            lyrics_dict = {
                'title': song['title'],
                'artist': song['primary_artist']['name'],
                'lyrics': song['lyrics'].split("\n")
            }

            lyricsList.append(lyrics_dict)

with open('api/utils/songs.json', 'w') as json_file:
    json.dump(lyricsList, json_file)
