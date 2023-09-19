from dotenv import load_dotenv
import os
import base64
from requests import post
import json
import requests


class api:

    #load the env file
    load_dotenv()

    def __init__(self) -> None:
        #get IDs from .env file
        self.clientID = os.getenv("CLIENT_ID")
        self.clientSecret = os.getenv("CLIENT_SECRET")
        self.token = self.getToken()

        self.artist_name = "kesha"
        self.songs = self.getArtistSongs(self.artist_name, self.token)


    def getToken(self):
        authString = self.clientID + ":" + self.clientSecret
        authBytes = authString.encode("utf-8")
        authBase64 = str(base64.b64encode(authBytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + authBase64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data=data)
        jsonResult = json.loads(result.content)
        token = jsonResult["access_token"]
        return token

    def getAuthHeader(self, token):
        return {"Authorization": "Bearer " + self.token}


    def getArtistSongs(self, artist_name, token):
        base_url = "https://api.spotify.com/v1/search"
        headers = self.getAuthHeader(token)

        params = {
            "q": f"artist:{artist_name}",
            "type": "track",
            "limit": 50  # You can adjust the limit as needed
        }

        try:
            response = requests.get(base_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            # Extract and return the list of tracks
            if "tracks" in data and "items" in data["tracks"]:
                return data["tracks"]["items"]
            else:
                return []

        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return []

    # Print the list of songs
    def printSongs(self):
        for song in self.songs:
            print(song["name"])

    def getTopSongURI(self):
    # sort the songs by popularity
        self.sorted_songs = sorted(self.songs, key=lambda x: x["popularity"], reverse=True)

        # check if there are songs
        if self.sorted_songs:
            # return the URI of the top song
            return self.sorted_songs[0]["uri"]
        else:
            return None
    