import json


class UserEncoder(json.JSONEncoder):

    def default(self, obj):
        return obj.__dict__