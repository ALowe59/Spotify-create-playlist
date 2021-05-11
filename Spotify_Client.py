import json
import requests

from track import Track
from playlist import Playlist

class SpotifyClient:

    def __init__(self, auth_token, user_id):
        self._auth_token = auth_token
        self._user_id = user_id