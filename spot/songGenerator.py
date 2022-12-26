# based off documentation from: https://spotipy.readthedocs.io/en/2.21.0/#

import spotipy
import random
from pprint import pprint

class SongGenerator:
    def __init__(self):
        self.sadsongs = None
        self.popsongs = None
        self.rnbsongs = None
        self.discoversongs = None

        username = '8kre5pga5ch5lwdkfwbt3b3fy'
        clientID = '08bbf67f3d544e0fa6af2a3afd3c7c64'
        clientSecret = '3e4b98f010b0404c93b30d537bccf282'
        redirect_uri = 'http://localhost:8888/callback/'
        oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
        token_dict = oauth_object.get_access_token()
        token = token_dict['access_token']

        self.spotifyObject = spotipy.Spotify(auth=token)
        user_name = self.spotifyObject.current_user()

    def assignSongs(self):
        pl_id = 'https://open.spotify.com/playlist/24lc14kwkIP8mFu9Toq9Tt?si=944f47ee2f0f40dd' 
        offset = 0
        sadPlaylistData = self.spotifyObject.playlist_items(pl_id,
                                        offset=offset,
                                        fields='items.track.id,total',
                                        additional_types=['track']) 

        sadPlaylist = sadPlaylistData['items']

        # pop playlist
        pl_id = 'https://open.spotify.com/playlist/24lc14kwkIP8mFu9Toq9Tt?si=944f47ee2f0f40dd' 
        offset = 0
        popPlaylistData = self.spotifyObject.playlist_items(pl_id,
                                        offset=offset,
                                        fields='items.track.id,total',
                                        additional_types=['track']) 

        popPlaylist = popPlaylistData['items']

        # discover playlist
        pl_id = 'https://open.spotify.com/playlist/24lc14kwkIP8mFu9Toq9Tt?si=944f47ee2f0f40dd' 
        offset = 0
        discoverPlaylistData = self.spotifyObject.playlist_items(pl_id,
                                        offset=offset,
                                        fields='items.track.id,total',
                                        additional_types=['track']) 

        discoverPlaylist = discoverPlaylistData['items']

        # rnb playlist
        pl_id = 'https://open.spotify.com/playlist/24lc14kwkIP8mFu9Toq9Tt?si=944f47ee2f0f40dd' 
        offset = 0
        rnbPlaylistData = self.spotifyObject.playlist_items(pl_id,
                                        offset=offset,
                                        fields='items.track.id,total',
                                        additional_types=['track']) 

        rnbPlaylist = rnbPlaylistData['items']
        
        self.popsongs = self.loadSongs(popPlaylist)
        self.sadsongs = self.loadSongs(sadPlaylist)
        self.discoversongs = self.loadSongs(discoverPlaylist)
        self.rnbsongs = self.loadSongs(rnbPlaylist)

    def loadSongs(self, playlist):
        counter = 0
        songsdict = dict()

        for song in playlist:
            counter += 1
            print(f"Loading song no. {counter}...")
            song_id = song['track']['id']
            track = self.spotifyObject.track(song_id)
            print(song['track']['id'])
            # print(track['artists'][0]['name'])
            # print(track['name'])
            # print(song)
            # tempdict = {"id": song['track']['id'],
            #             "artists": track['artists'][0]['name'],
            #             "name": track['name'],
            #             "art": track['album']['images'][0]['url'],
            #             "url": "https://open.spotify.com/track/" + song['track']['id'],
            #             "uri": "spotify:track:" + song['track']['id']}
            # songsdict[counter] = tempdict

        return songsdict

    def getSong(self, emotion):
        if emotion == "sad":
            number = random.randint(1, len(self.rnbsongs))
            return self.rnbsongs[number]
        elif emotion == "happy" or emotion == "surprise":
            number = random.randint(1, len(self.popsongs))
            return self.popsongs[number]
        elif emotion == "angry" or emotion == "disgust" or emotion == "fear":
            number = random.randint(1, len(self.sadsongs))
            return self.sadsongs[number]
        elif emotion == "neutral":
            number = random.randint(1, len(self.discoversongs))
            return self.discoversongs[number]

sg = SongGenerator()
sg.assignSongs()

