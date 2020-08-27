import lyricsgenius
genius = lyricsgenius.Genius("my_client_access_token_here")
artist = genius.search_artist("J. Cole", max_songs=3, sort="title")
print(artist.songs)