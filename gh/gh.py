import requests
import logging

class Repo:
    def __init__(self, client):
        self.client = client
    
    def add_collaborator(self, name_with_owner, username, permission):
        url = f"{self.client.base_url}/repos/{name_with_owner}/collaborators/{username}"
        data = {"permission": permission}
        response = requests.put(url, headers=self.client.headers, json=data)
        if response.status_code == 201:
            logging.info(f"Successfully added {username} to {name_with_owner}")
            return
        else:
            e = f"Error adding {username} to {name_with_owner}.  Response: {response.json()}"
            logging.error(e)
            raise Exception(e)

class Org:
    def __init__(self, client):
        self.client = client

    def invite_member(self, user_id, org_name):
        url = f"{self.client.base_url}/orgs/{org_name}/invitations"
        data = {"invitee_id": user_id, "role": "admin"}

        response = requests.post(url, headers=self.client.headers, json=data)
        if response.status_code == 201:
            logging.info(f"Successfully invited {user_id} to {org_name}")
            return
        else:
            e = f"Error inviting user to organization. Response: {response.json()}"
            logging.error(e)
            raise Exception(e)

class User:
    def __init__(self, client):
        self.client = client

    def get_id(self, username):
        url = f"{self.client.base_url}/users/{username}"
        response = requests.get(url, headers=self.client.headers)
        if response.status_code == 200:
            id = response.json()["id"]
            logging.info(f"{username} ID: {id}")
            return id
        elif response.status_code == 404:
            e = f"User {username} does not exist"
            logging.error(e)
            raise Exception(e)
        else:
            e = f"Error getting user id: {response.json()}"
            logging.error(e)
            raise Exception(e)