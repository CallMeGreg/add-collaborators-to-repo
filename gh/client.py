import requests
import logging
import json
import gh.gh as gh


class Client:
    def __init__(self, token):
        self.headers =  {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json"
        }
        self.base_url = "https://api.github.com"
        self.graphql_url = "https://api.github.com/graphql"
        self.user = gh.User(self)
        self.repo = gh.Repo(self)
        self.org = gh.Org(self)