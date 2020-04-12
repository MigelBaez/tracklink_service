import json


class Config:
    url_backend_track_link = ""
    token_track_link = ""

    def __init__(self, config_name):
        with open(config_name, "r") as config:
            config_data = json.load(config)
            self.url_backend_track_link = config_data["URL_BACKEND_TRACK_LINK"]
            self.token_track_link = config_data["TOKEN_TRACK_LINK"]
